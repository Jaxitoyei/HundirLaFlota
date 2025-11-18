"""
Ejercicios

- Análisis de películas:
    Tienes una lista de películas con su nombre, valoración y duración.
        - Ordena las películas de mayor a menor en valoración. Luego ordénalas también alfabéticamente.
        - Obtener solo las películas que duren más de 120 minutos.
        - Crea una lista solo con los nombres de las películas.
"""
from functools import reduce

peliculas = [
    {"nombre": "El padrino", "valoracion": 9.2, "duracion": 175},
    {"nombre": "Toy Story", "valoracion": 8.9, "duracion": 154},
    {"nombre": "El señor de los anillos", "valoracion": 8.3, "duracion": 81},
    {"nombre": "Forrest Gump", "valoracion": 8.8, "duracion": 142},
]



valoracion_ordenadaNum = sorted(peliculas,key=lambda emp: emp["valoracion"], reverse=True)

valoracion_ordenadaAlfabeticamente= sorted(peliculas,key=lambda emp: emp["nombre"], reverse=True)

print("Valoración ordenada",valoracion_ordenadaNum)
print("Valoración ordenada",valoracion_ordenadaAlfabeticamente)
print("valoración sin ordenar" , peliculas)




peliculas_120Minutos = list(filter(lambda  emp : emp ["duracion"] > 120, peliculas))

print(peliculas_120Minutos)

listaPeliculas = list(map(lambda pelicula:  pelicula["nombre"], peliculas))

print("ListaPelículas: " , listaPeliculas)


nombrePeliculas = []

for  pelicula in  peliculas:
    nombrePeliculas.append( pelicula["nombre"])

print("Lista de nombres de la película", nombrePeliculas)


"""
- Procesamiento de ventas
    Dada una lista de ventas, calcula el total de ventas y también obten las ventas mayores a 1000.
"""
ventas = [1500, 800, 2200, 600, 3500, 950, 1200, 450]


TotalVentas = reduce(lambda contador, venta: contador + venta, ventas,0)

VentasMayores100 = list(filter(lambda  venta: venta > 1000, ventas))

print("Total ventas: " , TotalVentas)
print("Ventas superiores a 1000: ", VentasMayores100)

"""
- Procesamiento de texto
    Dada una lista de frases:
        - Convertir todas las frases a mayúsculas
        - Obtener solo las frases con más de 3 palabras
        - ¿Cuántas palabras tienen todas mis frases en total?
"""



frases = [
    "Python es genial",
    "Me gusta programar",
    "Hola mundo",
    "La programación funcional es interesante",
    "Hola"
]

frasesMayusculas = list(map(lambda  frase : str(frase).upper(), frases))

print("Frases en mayusclas,", frasesMayusculas)


frasesSuperior3Palabras = list(filter(lambda frase: len(str(frase).split()) >= 3 , frases ))

print("Frases con más de 3 palabras ", frasesSuperior3Palabras)


# Primero se pone lambda, después el contador
# después la frase
#después toda la condición de la variable,
# después la frase,
frases_en_Total = reduce(lambda contador, frase: contador  + len(str(frase).split()) , frases,0 )


print("Frases en total; ", frases_en_Total)