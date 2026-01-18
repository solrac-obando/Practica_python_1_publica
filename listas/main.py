"""
listas o (arrays)
las Listas son colecciones o conjuntos de datos que están agrupados bajo un único nombre
para acceder a estos valores podemos utilizar un índice que se crea por defecto en este conjunto de datos
recordar que el índice comienza desde 0, para el primer valor y así sucesivamente.
para definir una lista es con []
"""
print("\n##################### Ejercicio 1 de listas #################\n")

pelicula = "batman"
print(pelicula)

peliculas = ["Batman", "El señor de los anillos", "Spiderman"]

# este método requiere que se le pase una tupla por eso requiere los paréntesis dobles
cantantes = list(("Michael Jackson", "Bey", "Jennifer Lopez")) 


year = list(range(2020, 2031))# este método crea una lista de números desde el primer número hasta el último sin incluirlo

print(pelicula)
print(peliculas) #imprime toda la lista
print(peliculas[0]) #imprime el primer valor en este caso batman
# ejemplo 2 con las función predefinida list

print(cantantes)

print(year)
print("\n##################### Ejercicio 2 de listas #################\n")

# índices en las listas positivos y negativos
print(cantantes[1])
print(cantantes[-2])
print(cantantes[1:3])
print(peliculas[-3:-1])
print(year[-3:])

# Añadir y editar elementos en una lista:

cantantes[1]= "juanes"
print("\n Modificando datos en una lista")
print(cantantes)
cantantes.append("Bey")
print("\n Agregando nuevos datos a la lista")
print(cantantes)

#Recorrido de listas con bucles:
print("############## Ejercicio 4 ###############\n")
print("\n**************** Lista de Películas *************\n")
"""
nueva_pelicula=""
while nueva_pelicula != "parar":
    nueva_pelicula= input("Introduce el nombre de la Película: ")
    if nueva_pelicula == "parar":
        print("\n Fin del programa Gracias por participar\n")
    else:
        peliculas.append(nueva_pelicula)



for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
print("\n")
"""

#listas multidimensionales, o como ejemplo piensa en una muñeca matriosca
#Una lista multidimensional es una lista dentro de listas:

print("############## Ejercicio 4 ###############\n")
print("\n**************** Lista de Contactos *************\n")

contactos= [

    [
        "Antonio", "antonio@example.com"
    ],
    [
        "Jose", "jose@example.com"
    ],
    [
        "Ayllen", "ayllen70@example.com"
    ],
    [
        "Maria", "mariaf@example.com"
    ]
]
print(contactos[1]) #
print(contactos[1][1])
print(contactos[0][1])
print(contactos[3][0])