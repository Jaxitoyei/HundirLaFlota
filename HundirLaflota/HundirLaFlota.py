def generarMapa():
    matriz = []
    for i in range(11):
        matriz.append([])
        for j in range(11):

            if j == 0:
                if i == 10:
                    matriz[i].append("10")

                else:

                    cadena =  " " +str(i)

                    matriz[i].append(cadena)




            if j == 1:

                if i == 0:
                    matriz[i].append(" A")
                else:
                    matriz[i].append(" *")
            if j == 2:
                if i == 0:
                    matriz[i].append(" B")
                else:
                    matriz[i].append(" *")
            if j == 3:
                if i == 0:
                    matriz[i].append(" C")
                else:
                    matriz[i].append(" *")
            if j == 4:
                if i == 0:
                    matriz[i].append(" D")
                else:
                    matriz[i].append(" *")
            if j == 5:
                if i == 0:
                    matriz[i].append(" E")
                else:
                    matriz[i].append(" *")
            if j == 6:
                if i == 0:
                    matriz[i].append(" F")
                else:
                    matriz[i].append(" *")
            if j == 7:
                if i == 0:
                    matriz[i].append(" G")
                else:
                    matriz[i].append(" *")
            if j == 8:
                if i == 0:
                    matriz[i].append(" H")
                else:
                    matriz[i].append(" *")
            if j == 9:
                if i == 0:
                    matriz[i].append(" I")
                else:
                    matriz[i].append(" *")

            if j == 10:
                if i == 0:
                    matriz[i].append(" J")
                else:
                    matriz[i].append(" *")



    return matriz


def imprimiirMatriz(matriz):
    for i in range(len(matriz)):
        print()
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")


mapa = generarMapa()

imprimiirMatriz(mapa)
