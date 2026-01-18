"""
crear un programa con una lista de 8 números enteros o naturales que la recorra en un bucle
y la imprima por pantalla, por último buscar un elemento en la lista de acuerdo a lo que el
usuario ingrese en un input y mostrarlo por pantalla.


"""
Lista_numeros=[
    13,25,31,49,5,16,37,68,
]

#hacer una función que recorra la lista y devuelva un string
def mostraLista(lista):
    resultado=""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado



# Recorrer y mostrar
print(f"La lista de numeros es {Lista_numeros}")
"""for numero in Lista_numeros:
    print(f"Los numeros en la listas son: {numero}")"""



print(mostraLista(Lista_numeros))
print(mostraLista(["Victor", "Carlos","Juan"]))

print("############### Ordena y mostrar ##############\n")

Lista_numeros.sort()
print(mostraLista(Lista_numeros))

print("############### mostrar la longitud ##############\n")
print(len(Lista_numeros))

print("############### busqueda ##############\n")
busqueda= int(input("Introduce un número para verificar en la lista: "))
comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda= int(input("Introduce un número para verificar en la lista"))
else:
    print(f"has introducido el número: {busqueda}", "\n")

search = Lista_numeros.index(busqueda)
print(f"##### El número buscado sí existe en la lista es: {busqueda}", "############\n")
print(f" El número ingresado en la búsqueda existe en la lista, con el índice: {search}")





