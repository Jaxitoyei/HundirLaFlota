def ajustarTexto(texto):
    texto = texto.upper().strip()

    return texto


def AjustarCoordenadaX(coordx):
    coordXs = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    coordResultante = 0
    for i in range(len(coordXs)):
        if coordXs[i] == coordx:
            coordResultante = i + 1

    return coordResultante


def AjustarCoordenadaY(coordY):
    return coordY


def generarMapa():
    matriz = []
    for i in range(11):
        matriz.append([])
        for j in range(11):

            if j == 0:
                if i == 10:
                    matriz[i].append("10")

                else:

                    cadena = " " + str(i)

                    matriz[i].append(cadena)

            if j == 1:

                if i == 0:
                    matriz[i].append(" A")
                else:
                    matriz[i].append("  ")
            if j == 2:
                if i == 0:
                    matriz[i].append(" B")
                else:
                    matriz[i].append("  ")
            if j == 3:
                if i == 0:
                    matriz[i].append(" C")
                else:
                    matriz[i].append("  ")
            if j == 4:
                if i == 0:
                    matriz[i].append(" D")
                else:
                    matriz[i].append("  ")
            if j == 5:
                if i == 0:
                    matriz[i].append(" E")
                else:
                    matriz[i].append("  ")
            if j == 6:
                if i == 0:
                    matriz[i].append(" F")
                else:
                    matriz[i].append("  ")
            if j == 7:
                if i == 0:
                    matriz[i].append(" G")
                else:
                    matriz[i].append("  ")
            if j == 8:
                if i == 0:
                    matriz[i].append(" H")
                else:
                    matriz[i].append("  ")
            if j == 9:
                if i == 0:
                    matriz[i].append(" I")
                else:
                    matriz[i].append("  ")

            if j == 10:
                if i == 0:
                    matriz[i].append(" J")
                else:
                    matriz[i].append("  ")

    return matriz


def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        print()
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")


def pintar(coordenadaX, coordenadaY, matriz):
    posicion = input("Seleccione una orientación (Horizontal/Vertical")

    if posicion.lower().strip() == "horizontal":

        orientacion = input("Seleccione la horientación (Derecha/Izquierda)")

        if orientacion == "derecha":
            matriz[coordenadaX][coordenadaY] = "[]"
            print(coordenadaX, coordy)
        elif orientacion == "izquierda":
            matriz[coordenadaX][coordenadaY] = "[]"
            print(coordenadaX, coordenadaY)
        else:
            print("Opción incorrecta")



    elif posicion.lower().strip() == "vertical":

        orientacion = input("Seleccione la horientación (Arriba/Abajo)")
        orientacion = orientacion.lower().strip()

        if orientacion == "arriba":
            matriz[coordenadaX][coordenadaY] = "[]"
            print(coordenadaX, coordenadaY)
        elif orientacion == "abajo":
            matriz[coordenadaX][coordenadaY] = "[]"
            print(coordenadaX, coordenadaY)
        else:
            print("Opción incorrecta")
    else:
        print("Opción incorrecta: ")

    return  matriz


mapa = generarMapa()

imprimirMatriz(mapa)

print("Elija una opción de barco")

print(" A) 1 Acorazado ")
print(" B) 3 Lancha")
print(" C) 1 Portaviones")
print(" D) 2 Fragatas ")
print(" E) 3 Corvetas")
print(" q- 4 Salir")

opcionElegida = input("Introduzca una de las opciones A - E ")
opcionElegida = ajustarTexto(opcionElegida)

if opcionElegida == "A":
    size = 5
    nombre = "Acorazado"
    coordx = input("Indique la coordenada X: (A-J)")
    coordx = ajustarTexto(coordx)
    coordx = AjustarCoordenadaX(coordx)
    coordy = int(input("Indique la coordenada Y: (1-10)"))
    # Justo aquí iría el objeto: barco = Barco(cordx, cordy, size, nombre, posicion)
    # Pintar
    mapa = pintar(coordx, coordy, mapa)

elif opcionElegida == "B":
    size = 1
    nombre = "Lancha"
    coordx = input("Indique la coordenada X: (A-J)")
    coordx = ajustarTexto(coordx)
    coordx = AjustarCoordenadaX(coordx)
    coordy = int(input("Indique la coordenada Y: (1-10)"))
    # Justo aquí iría el objeto: barco = Barco(cordx, cordy, size, nombre, posicion)
    # Pintar
    mapa = pintar(coordx, coordy, mapa)
elif opcionElegida == "C":
    size = 4
    nombre = "Portaviones"
    coordx = input("Indique la coordenada X: (A-J)")
    coordx = ajustarTexto(coordx)
    coordx = AjustarCoordenadaX(coordx)
    coordy = int(input("Indique la coordenada Y: (1-10)"))
    # Justo aquí iría el objeto: barco = Barco(cordx, cordy, size, nombre, posicion)
    # Pintar
    mapa = pintar(coordx, coordy, mapa)
elif opcionElegida == "D":
    size = 3
    nombre = "Fragata"
    coordx = input("Indique la coordenada X: (A-J)")
    coordx = ajustarTexto(coordx)
    coordx = AjustarCoordenadaX(coordx)
    coordy = int(input("Indique la coordenada Y: (1-10)"))
    # Justo aquí iría el objeto: barco = Barco(cordx, cordy, size, nombre, posicion)
    # Pintar
    mapa = pintar(coordx, coordy, mapa)
elif opcionElegida == "E":
    size = 2
    nombre = "Corveta"
    coordx = input("Indique la coordenada X: (A-J)")
    coordx = ajustarTexto(coordx)
    coordx = AjustarCoordenadaX(coordx)
    coordy = int(input("Indique la coordenada Y: (1-10)"))
    # Justo aquí iría el objeto: barco = Barco(cordx, cordy, size, nombre, posicion)
    # Pintar
    mapa = pintar(coordx, coordy, mapa)

salir = True
while (salir):

    print("\n-----DISPARAR-------")

    disparox = input("Introduzca una coordenada:  (A-J)")
    disparoy = int(input("Introduzca una coordenada (1-10)"))

    disparox = ajustarTexto(disparox)
    disparox = AjustarCoordenadaX(disparox)

    disparoy = AjustarCoordenadaY(disparoy)

    if mapa[disparoy][disparox] == "[]":

        print("Barco dado ")
        mapa[disparoy][disparox] = "X"


    else:

        mapa[disparoy][disparox] = "Ç"

    imprimirMatriz(mapa)