import random as ran

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


def castCordY(cordXletra, letras):
    for i in range(len(letras)):
        if cordXletra == letras[i]:
            return i + 1


def AjustarCoordenadaX(coordx):
    coordXs = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    coordResultante = 0
    for i in range(len(coordXs)):
        if coordXs[i] == coordx:
            coordResultante = i + 1

    return coordResultante







def dispara(tabla, cordX, cordY, barco):
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if i == cordX and j == cordY:
                tabla[cordX][cordY] = 'X'

    if cordX == barco.getCordX() and cordY == barco.getCordY():
        tabla[cordX][cordY] = '*'


def seleccionaBarco(barcos):
    print("  Acorazado ")
    print("  Lancha")
    print("  Portaviones")
    print("  Fragatas ")
    print("  Corvetas")
    miBarco = input("Introduce el nombre del barco que quieres colocar?\n>> ").lower()


    for i in range(len(barcos)):
        if barcos[i].getName() == miBarco:
            miBarco = barcos[i]


            letraCordY = input("Introduce la cordenada X del barco (A-J)\n >> ").upper()

            cordY = castCordY(letraCordY, letras)
            cordX = int(input("Introduce la cordenada Y del barco (1-10)\n >> "))


            miBarco.setCordY(cordY)
            miBarco.setCordX(cordX)

            barcos.pop(i)
            return miBarco




def ponBarco(barcos, tabla):  # Defecto visual al ser izq
    barco = seleccionaBarco(barcos)
    direccion = input("Hacia que direccion lo quieres poner?\n>> ").lower()
    barco.setOrientation(direccion)

    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "derecha":
                for k in range(barco.getSize()):
                    tabla[barco.getCordX()][barco.getCordY() + k] = 'Ç'
            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "izquierda":
                for k in range(barco.getSize()):
                    tabla[barco.getCordX()][barco.getCordY() - k] = 'Ç'

            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "abajo":
                for k in range(barco.getSize()):
                    tabla[barco.getCordX() + k][barco.getCordY()] = 'Ç'

            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "arriba":
                for k in range(barco.getSize()):
                    tabla[barco.getCordX() - k][barco.getCordY()] = 'Ç'

    print()
    imprimirMatrizInvicible(tabla)
    print()


def comienzas(num):
    ranL = num
    ranE = ran.randint(0, 1)  # esto sera remplazado por el resultado de la llamada del socket del otro juagdor
    if ranL == ranE:
        while ranL == ranE:
            ranL = ran.randint(0, 1)
        return comienzas(ranL)
    elif ranL > ranE:
        return True
    elif ranE > ranL:
        return False


def loHundieron(barco, tabla):
    contAssrt = 0
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "derecha":
                for k in range(barco.getSize()):
                    if tabla[barco.getCordX()][barco.getCordY() + k] == '*':
                        contAssrt += 1

            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "izquierda":
                for k in range(barco.getSize()):
                    if tabla[barco.getCordX()][barco.getCordY() - k] == '*':
                        contAssrt += 1

            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "abajo":
                for k in range(barco.getSize()):
                    if tabla[barco.getCordX() + k][barco.getCordY()] == '*':
                        contAssrt += 1

            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "arriba":
                for k in range(barco.getSize()):
                    if tabla[barco.getCordX() - k][barco.getCordY()] == '*':
                        contAssrt += 1

    if contAssrt == barco.getSize():
        return f"{barco.getName()}, ha sido hundido"
    else:
        return "Todo pasifico"


def colocalo(barco, tabla):  # Variable de test, sera borrada luego de eso, no servira
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "derecha":
                for k in range(barco.getSize()):
                    tabla[barco.getCordX()][barco.getCordY() + k] = '[]'
            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "izquierda":
                for k in range(barco.getSize()):
                    tabla[barco.getCordX()][barco.getCordY() - k] = '[]'

            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "abajo":
                for k in range(barco.getSize()):
                    tabla[barco.getCordX() + k][barco.getCordY()] = '[]'

            if i == barco.getCordX() and j == barco.getCordY() and barco.getOrientation() == "arriba":
                for k in range(barco.getSize()):
                    tabla[barco.getCordX() - k][barco.getCordY()] = '[]'


letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numeros = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']


piezas = []
barquitos = []
portaviones = Barco("portaviones", 5)
acorazado = Barco("acorazado", 4)
destructor = Barco("destructor", 4)
submarino = Barco("submarino", 3)
crucero = Barco("crucero", 2)


lancha = Barco("lancha", 12)

barquitos.append(portaviones)
barquitos.append(acorazado)
barquitos.append(destructor)
barquitos.append(submarino)
barquitos.append(crucero)

for barco in barquitos:
    piezas.append(barco)

mapajugador1 = []
mapajugador2 = []
creaMapaVacio(mapajugador1)
creaMapaVacio(mapajugador2)


imprimirMatrizInvicible(mapajugador1)

print()

for i in range(len(piezas)):
    ponBarco(piezas, mapajugador1)

'''if comienzas(ran.randint(0,1)):
    print("Eres el jugador 1\nAhora comienza atacando al jugador 2.")
    imprimirMatrizInvicible(mapajugador2)
    dispara(mapajugador2,3,3)
    print("Tu disparo acerto? ",lediste(mapajugador2,crucero,3,3))

    imprimirMatrizInvicible(mapajugador2)
else:
    print("Eres el jugador 2, espera a que el jugador uno termine su turno.")'''

while True:

    atX = int(input("igreseconr X"))
    atY = int(input("igreseconr Y"))

    for barco in barquitos:
        dispara(mapajugador1, atX, atY, barco)
        loHundieron(barco, mapajugador1)

    imprimirMatrizInvicible(mapajugador1)
