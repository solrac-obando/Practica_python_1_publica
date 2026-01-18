#Tipos de datos en Python del curso o Master en Python de Víctor Robles:


nada = None
cadena = "cadena o string"
entero = 500
flotante = 10.5
booleano = True
booleano2 = False
lista = [10,20,30,40]
tupla = (10,20,30,40)
# los diccionarios son un conjunto de datos que se conforman con una clave y un valor correspondiente a la clave:
diccionario = {
    "nombre": "Carlos",
    "apellido": "Obando",
    "web": "carlosobandoweb.com"
}
rango = range(9)    

print(type(nada), nada)
print(type(cadena), cadena)
print(type(entero), entero)
print(type(flotante), flotante)
print(type(booleano), booleano)
print(type(booleano2), booleano2)
print(type(lista), lista)
print(type(tupla), tupla)
print(type(diccionario), diccionario)
print(type(rango), rango)

""" 
ahora vamos a transformar los tipos de datos: para ello se debe colocar la abreviatura del
tipo de dato y luego el dato que se desea transformar, por ejemplo:
"""
nuevaCadena =str(entero)
print(type(nuevaCadena), nuevaCadena)