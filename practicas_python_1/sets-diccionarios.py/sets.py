"""
Los sets son un tipo de datos que son similares a las lista un conjuntos de elemento o datos
pero que a diferencia de las listas los sets no poseen un indice o orden, en resumen 
los sets son una colección de elementos únicos y desorganizados. para definir un sets es con {}

"""
personas = {
    "Carlos",
    "Juan",
    "Maria",
    "Ana",
    "Ayllen",
    "Victor"
}
print(personas)
personas.add("Paco")
print(personas)
print(type(personas))
personas.remove("Maria")
print(personas)

