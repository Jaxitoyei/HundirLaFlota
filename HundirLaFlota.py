def mostrarTabla(tablero):
    for fila in tablero:
        print(fila)


def imprimirMatrizInvicible(matriz):  # Robado de un video de youtube.
    for fila in matriz:
        print('  '.join(map(str, fila)))


def ponBarco(tabla, barco):
    print()


letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numeros = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']

mapajugador1 = []

for i in range(11):
    mapajugador1.append([])
    for j in range(11):
        if i == 0 and j == 0:
            mapajugador1[i].append('  ')
        if i == 0 and j != 0:
            mapajugador1[i].append(letras[j - 1])
        if j == 0 and i != 0:
            mapajugador1[i].append(numeros[i - 1])

        if i != 0 and j != 0:
            mapajugador1[i].append('*')

imprimirMatrizInvicible(mapajugador1)

acorazado = Barco()