"""
variables son valores que pueden ser alterados o modificados en un programa y también se utiliza para
representar un valor de algún dato o una información.
 una definición concreta es un contenedor de información que dentro guarda
 un dato, se pueden crear múltiples variables y cada una puede tener un dato distinto
"""
# ejemplo de variable en Python
# estos ejercicios son para crear variables
texto = "hola mundo, Master en python"
texto2 = "soy Carlos Obando, y mi tutor es Victor Robles"
numero = 10
decimal = 10.5
# mostrar los valores de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------------------------------------------")
# modificar el valor o los datos de las variables existentes
numero = 45
decimal = 36.78
print(numero)
print(decimal)

print("------------------------------------------------")

# concatenación de 2 variables

nombre = "Carlos"
apellido = "Obando"
Web ="carlosobandoweb.com"

print(nombre + " " + apellido + "la página web es: " + Web)
# concatenación con f-string, ejemplo:

print(f"{nombre} {apellido} la página web es: {Web}")

# concatenación con el método format:
print("Hola yo soy {} {} y mi página web es: {}".format(nombre,apellido,Web))

