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

def disparar(coordenadas):

    if mapajugador1[coordenadas[0]][coordenadas[1]] == "Ç":
        print("Barco dado ")
        mapajugador1[coordenadas[0]][coordenadas[1]] = "*"
    else:
        print("Agua")
        mapajugador1[coordenadas[0]][coordenadas[1]] = "X"

def validaX():
    cordXtxt = input("Introduce la cordenada Y del barco (1-10)\n >> ")
    while not cordXtxt.isnumeric():
        cordXtxt = input("La cordenada Y del barco tiene que ser un numero entre el 1 al 10 no una letra.\n >> ")
    cordX=int (cordXtxt)
    while cordX<1 or cordX>10:
        cordXtxt=input("La cordenada Y del barco tiene que ser un numero entre el 1 al 10.\n >> ")
        cordX=int(cordXtxt)
    return cordX

def seleccionaBarco(barcos,listaBarcos):
    mostrarTabla(barcos)
    print()
    miBarco=input("Introduce el nombre del barco que quieres colocar?\n>> ").lower()

    while miBarco not in listaBarcos:
        print("Ese barcos no está en el menú de opciones")
        miBarco = input("Seleccione un barco del menú: ")

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


def noPuedesPonerlo(barco):
    if barco.getCordX==1 and barco.getOrientation=="arriba":
        return True

    if barco.getCordY==1 and barco.getOrientation=="izquierda":
        return True

    if barco.getCordX==10 and barco.getOrientation=="abajo":
        return True

    if barco.getCordY==10 and barco.getOrientation=="derecha":
        return True

    return False


def ponBarco(barcos,tabla,listaBarcos): # Defecto visual al ser izq

    barco = seleccionaBarco(barcos, listaBarcos)

    direccion=input("Hacia que direccion lo quieres poner?\n>> ").lower()
    while direccion not in ["derecha","izquierda","arriba","abajo"]:
        direccion = input("La direccion introducida es incorrecta introduzca una direccion valida: [derecha,izquierda,arriba,abajo]\n >> ").lower()
    barco.setOrientation(direccion)

    if noPuedesPonerlo(barco):
        nueva_direccion = input("No se puede poner un barco en esa direccion, cambia de direccion.\n>> ").lower()
        while nueva_direccion not in ["derecha", "izquierda", "arriba", "abajo"]:
            nueva_direccion = input("La direccion introducida es incorrecta introduzca una direccion valida: [derecha,izquierda,arriba,abajo]\n >> ").lower()
        barco.setOrientation(nueva_direccion)


    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if i == barco.getCordX and j == barco.getCordY and barco.getOrientation == "derecha":
                for k in range(barco.getSize):
                    tabla[barco.getCordX][barco.getCordY + k] = 'Ç'
            if i == barco.getCordX and j == barco.getCordY and barco.getOrientation == "izquierda":
                for k in range(barco.getSize):
                    tabla[barco.getCordX][barco.getCordY - k] = 'Ç'

            if i == barco.getCordX and j == barco.getCordY and barco.getOrientation == "abajo":
                for k in range(barco.getSize):
                    tabla[barco.getCordX + k][barco.getCordY] = 'Ç'

            if i == barco.getCordX and j == barco.getCordY and barco.getOrientation == "arriba":
                for k in range(barco.getSize):
                    tabla[barco.getCordX - k][barco.getCordY] = 'Ç'

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

def addCoordenadas(coordenadas, mapa):
    if coordenadas in mapa:
        print("No puedes volver a seleccionar la misma coordenada")
    else:
        mapa.append(coordenadas)

    return mapa

def pedirCoordenadas():
    atX = (input("ingresa la coordenada X"))
    atX = atX.upper()

    while not atX in letras:
        print("Coordeanda x, incorrecta")
        atX = (input("ingresa la coordenada X"))
        atX = atX.upper()

    atX = AjustarCoordenadaX(atX)
    atY = int(input("ingresa la coordenada Y"))

    while atY < 1 or atY > 10:
        print("Coordenada Y incorrecta")
        atY = int(input("ingresa la coordenada Y"))

    coordenadas = (atY, atX)
    return coordenadas


def comienzas():
    miNum = ran.randint(0,1)
    print("Tu número es:", miNum)

    numEnemigo = int(recibeYEnviaCosa(miNum))
    print("Rival envió:", numEnemigo)

    if miNum == numEnemigo:
        print("Empate! repitiendo...")
        return comienzas()

    return miNum > numEnemigo



def recibeYEnviaCosa(cosa):
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

    mensaje = str(cosa).encode()
    sock.sendto(mensaje, ('127.0.0.1', 5005))

    info, server = sock.recvfrom(1024)

    dato = info.decode()
    sock.close()

    return dato

def AjustarCoordenadaX(coordx):
    coordXs = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    coordResultante = 0
    for i in range(len(coordXs)):
        if coordXs[i] == coordx:
            coordResultante = i + 1

    return coordResultante

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numeros = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']


barcosDisponibles = ["portaviones","acorazado","destructor","submarino","lancha"]
coordenadasMapa = []
piezas = []
barquitos = []
portaviones = Barco("portaviones", 5)
acorazado = Barco("acorazado", 4)
destructor = Barco("destructor", 4)
submarino = Barco("submarino", 3)
lancha = Barco("lancha", 2)

barquitos.append(portaviones)
barquitos.append(acorazado)
barquitos.append(destructor)
barquitos.append(submarino)
barquitos.append(lancha)

for barco in barquitos:
    piezas.append(barco)

mapajugador1 = []
mapajugador2=[]
creaMapaVacio(mapajugador1)
creaMapaVacio(mapajugador2)

imprimirMatrizInvicible(mapajugador1)

print("--------COLOCAR BARCOS---------")
while len(piezas) != 0:
    ponBarco(piezas, mapajugador1,barcosDisponibles)


'''
for i in range(len(piezas)):
    ponBarco(piezas,mapajugador1)'''

barcosHundidos = []



while len(barcosHundidos) !=len(barcosDisponibles):

    coordenadasJugador = pedirCoordenadas()

    coordenadasMapa = addCoordenadas(coordenadasJugador, coordenadasMapa)

    disparar(coordenadasJugador)

    for barco in barquitos:
        if barco not in barcosHundidos:
            hundido = loHundieron(barco, mapajugador1)
            if hundido is not None:
                barcosHundidos.append(barco)
                print(hundido)
    print()
    imprimirMatrizInvicible(mapajugador1)

print(">>>>>>>>>>>HAS PERDIDO<<<<<<<<<<")
print("Fin del programa")

"""salir = True
while (salir):
    print("\n-----DISPARAR-------")

    disparox = input("Introduzca una coordenada:  (A-J)")
    disparoy = int(input("Introduzca una coordenada (1-10)"))

    disparox = ajustarTexto(disparox)
    disparox = AjustarCoordenadaX(disparox)

    disparoy = AjustarCoordenadaY(disparoy)
"""

'''
if comienzas():
    print("Eres el jugador 1 — comienzas atacando.")
else:
    print("Eres el jugador 2 — espera al jugador 1.")'''