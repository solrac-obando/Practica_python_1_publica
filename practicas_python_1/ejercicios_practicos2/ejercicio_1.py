"""
crear un programa con un lista de 8 numeros enteros o naturales que la recorra en un bucle 
y la imprima por pantalla, por ultimo buscar un elemento en la lista deacuerdo a lo que el 
usuario ingrese en un input y mostrarlo por pantalla.


"""
Lista_numeros=[
    13,25,31,49,5,16,37,68,
]

#hacer una funcion que recorra la lista y devuelva un string
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
busqueda= int(input("Introduces un numero para verificar en la lista: "))
comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda= int(input("Introduces un numero para verificar en la lista"))
else:
    print(f"has Introducido el numero: {busqueda}", "\n")

search = Lista_numeros.index(busqueda)
print(f"##### El numero buscado  si existe en la lista es: {busqueda}", "############\n")
print(f" El numero en ingresdo en la busqueda existe en la lista, con el indice: {search}")





