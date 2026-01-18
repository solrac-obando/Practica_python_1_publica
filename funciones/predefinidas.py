diccionario_de_funciones = {
    "print": "Imprime valores en la consola.",
    "input": "Lee una entrada del usuario desde la consola.",
    "len": "Devuelve la longitud de un objeto iterable.",
    "range": "Genera una secuencia de números.",
    "sum": "Suma los elementos de un iterable.",
    "max": "Devuelve el valor máximo de un iterable.",
    "min": "Devuelve el valor mínimo de un iterable.",
    "abs": "Devuelve el valor absoluto de un número.",
    "append": "Agrega un elemento al final de una lista.",
    "index": "Devuelve el índice de la primera ocurrencia de un elemento en una lista.",
    "extend": "Extiende una lista agregando elementos de un iterable.",
    "type": "Devuelve el tipo de un objeto.",
    "isinstance": "Verifica si un objeto es una instancia de una clase.",
    "sorted": "Devuelve una lista ordenada de un iterable.",
    "filter": "Filtra elementos de un iterable basándose en una función.",
    "map": "Aplica una función a cada elemento de un iterable.",
    "str": "Convierte un objeto a una cadena de texto.",
    "int": "Convierte un objeto a un entero.",
    "float": "Convierte un objeto a un número de punto flotante.",
    "bool": "Convierte un objeto a un valor booleano.",
    "list": "Crea una lista a partir de un iterable.",
    "dict": "Crea un diccionario.",
    "tuple": "Crea una tupla a partir de un iterable.",
    "set": "Crea un conjunto a partir de un iterable.",
    "open": "Abre un archivo y devuelve un objeto de archivo.",
    "enumerate": "Devuelve un iterador con índices y valores de un iterable.",
    "zip": "Combina varios iterables en tuplas.",
    "all": "Devuelve True si todos los elementos de un iterable son verdaderos.",
    "any": "Devuelve True si al menos un elemento de un iterable es verdadero.",
    "round": "Redondea un número a un número específico de decimales.",
    "pow": "Calcula la potencia de un número."
}
print("\n", diccionario_de_funciones ,"\n")


nombre= "Carlos Obando"

# funciones generales
print(type(nombre))
# Detectar el tipado
comprobar = isinstance(nombre, str)

if comprobar:
    print("Esta variable es un string")
else:
    print("Esta variable no es un string")

if not isinstance(nombre, float):
    print("La variable no es un número flotante o decimal")

frase = "    contenido      "   
frace = "la vida es bella" 
print(frace.replace("vida", "mundo"))
print(frase.strip())