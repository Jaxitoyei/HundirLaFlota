import random as ran
import socket as sk
from Barco import *

def mostrarTabla(tablero):
    for fila in tablero:
        print(fila)

def imprimirMatrizInvicible(matriz):  # Robado de un video de youtube.
    for fila in matriz:
        print('  '.join(map(str, fila)))

def creaMapaVacio(tablero):
    for i in range(11):
        tablero.append([])
        for j in range(11):
            if i == 0 and j == 0:
                tablero[i].append('  ')
            if i == 0 and j != 0:
                tablero[i].append(letras[j - 1])
            if j == 0 and i != 0:
                tablero[i].append(numeros[i - 1])
            if i != 0 and j != 0:
                tablero[i].append('.')

def castLetrCordY(cordXletra,letras):
    for i in range(len(letras)):
        if cordXletra==letras[i]:
            return i+1

def dispara(tabla,barcos,cordX,cordY):
    cords=cordX,cordY
    for barco in barcos:
        if cords in barco.getCords:
            tabla[cordX][cordY]='*'
        print(barco.getName)
        print(barco.getCords)

def validaX():
    cordXtxt = input("Introduce la cordenada Y del barco (1-10)\n >> ")
    while not cordXtxt.isnumeric():
        cordXtxt = input("La cordenada Y del barco tiene que ser un numero entre el 1 al 10 no una letra.\n >> ")
    cordX=int (cordXtxt)
    while cordX<1 or cordX>10:
        cordXtxt=input("La cordenada Y del barco tiene que ser un numero entre el 1 al 10.\n >> ")
        cordX=int(cordXtxt)
    return cordX

def seleccionaBarco(barcos):
    mostrarTabla(barcos)
    print()
    miBarco=input("Introduce el nombre del barco que quieres colocar?\n>> ").lower()
    for i in range(len(barcos)):
        if barcos[i].getName==miBarco:
            miBarco=barcos[i]

            letraCordY = input("Introduce la cordenada X del barco (A-J)\n >> ").upper()

            while letraCordY.isnumeric() or letraCordY not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                letraCordY=input("La cordenada X del barco no puede ser un numero tiene que ser una letra de la A a la J\n >> ").upper()
            cordY = castLetrCordY(letraCordY, letras)

            try:
                cordX=validaX()
            except ValueError as e:
                print(e)


            miBarco.setCordY(cordY)
            miBarco.setCordX(cordX)

            barcos.pop(i)
            return miBarco

def ponEnDireccion(tabla, barco, icono):
    if barco.getOrientation== "derecha":
        for k in range(barco.getSize):
            tabla[barco.getCordX][barco.getCordY+ k] = icono
            barco.agregaCords((barco.getCordX,barco.getCordY+k))
    if barco.getOrientation== "izquierda":
        for k in range(barco.getSize):
            tabla[barco.getCordX][barco.getCordY- k] = icono
            barco.agregaCords((barco.getCordX, barco.getCordY-k))

    if barco.getOrientation== "abajo":
        for k in range(barco.getSize):
            tabla[barco.getCordX + k][barco.getCordY] = icono
            barco.agregaCords((barco.getCordX+k, barco.getCordY))

    if barco.getOrientation== "arriba":
        for k in range(barco.getSize):
            tabla[barco.getCordX- k][barco.getCordY] = icono
            barco.agregaCords((barco.getCordX-k, barco.getCordY))

def ponBarco(barcos,tabla): # Defecto visual al ser izq
    barco=seleccionaBarco(barcos)
    direccion=input("Hacia que direccion lo quieres poner?\n>> ").lower()
    while direccion not in ["derecha","izquierda","arriba","abajo"]:
        direccion = input("La direccion introducida es incorrecta introduzca una direccion valida: [derecha,izquierda,arriba,abajo]\n >> ").lower()

    barco.setOrientation(direccion)
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            ponEnDireccion(tabla,barco,'Ç')

    print()
    imprimirMatrizInvicible(tabla)
    print()

def loHundieron(barco,tabla):
    contAssrt=0
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if i==barco.getCordX and j==barco.getCordY and barco.getOrientation=="derecha":
                for k in range(barco.getSize):
                    if tabla[barco.getCordX][barco.getCordY+k]=='*':
                        contAssrt += 1

            if i==barco.getCordX and j==barco.getCordY and barco.getOrientation=="izquierda":
                for k in range(barco.getSize):
                    if tabla[barco.getCordX][barco.getCordY-k]=='*':
                        contAssrt += 1

            if i==barco.getCordX and j==barco.getCordY and barco.getOrientation=="abajo":
                for k in range(barco.getSize):
                    if tabla[barco.getCordX+k][barco.getCordY]=='*':
                        contAssrt += 1

            if i==barco.getCordX and j==barco.getCordY and barco.getOrientation=="arriba":
                for k in range(barco.getSize):
                    if tabla[barco.getCordX-k][barco.getCordY]=='*':
                        contAssrt += 1

    if contAssrt == barco.getSize:
        barco.hundido

def comienzas(num):
    ranL=num
    enviaCosa(ranL)
    ranEtxt=recibeCosa() #esto sera remplazado por el resultado de la llamada del socket del otro juagdor
    ranE=int (ranEtxt)

    print(ranE)

    if ranL==ranE:
        while ranL==ranE:
            ranL=ran.randint(0,1)
            enviaCosa(ranL)
        return comienzas(ranL)
    elif ranL>ranE:
        return True
    elif ranE>ranL:
        return False

def enviaCosa(cosa):
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    puerto = ("127.0.0.1", 5005)

    casteo=str(cosa).encode()

    sock.sendto(casteo, puerto)
    sock.close()


def recibeCosa():
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 5025))
    print("Esperando por el.")

    info, direccion = sock.recvfrom(1024)
    print(f"info recibida de: {direccion}")

    dato=info.decode()
    sock.close()

    return dato



letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numeros = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']

piezas=[]
barquitos=[]
portaviones=Barco("portaviones",5)
acorazado=Barco("acorazado",4)
destructor=Barco("destructor",4)
submarino=Barco("submarino",3)
crucero=Barco("crucero",2)

#barquitos.append(portaviones)
#barquitos.append(acorazado)
#barquitos.append(destructor)
barquitos.append(submarino)
barquitos.append(crucero)

for barco in barquitos:
    piezas.append(barco)

mapajugador1 = []
mapajugador2=[]
creaMapaVacio(mapajugador1)
creaMapaVacio(mapajugador2)

imprimirMatrizInvicible(mapajugador1)

print()
'''
for i in range(len(piezas)):
    ponBarco(piezas,mapajugador1)'''


if comienzas(ran.randint(0,1)): #Esto lo quiero ver con sockets
    print("Eres el jugador 1\nAhora comienza atacando al jugador 2.")


else:
    print("Eres el jugador 2, espera a que el jugador uno termine su turno.")

    '''while True:

        atX = int(input("igreseconr X"))

        atY = input("igreseconr Y (A-J)").upper()
        atYN=castLetrCordY(atY,letras)


        dispara(mapajugador1,barquitos, atX, atYN)

        imprimirMatrizInvicible(mapajugador1)'''