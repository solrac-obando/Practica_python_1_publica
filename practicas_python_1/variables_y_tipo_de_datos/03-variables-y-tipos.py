"""
variables son valores que pueden ser alterados o modificados en un programa y tambien se utiliza para 
reprecentar un valor de algun dato o una informacion.
 una definicion concreta es un contenedor de infromacion que dentro guarda
 un dato, se pueden crear mutiples variables y cada una puede tener un dato distinto
"""
# ejemplo de variable en python
# esos ejercicios son crear variables
texto = "hola mundo, Master en python"
texto2 = "soy Carlos Obando, y mi tutor es Victor Robles"
numero = 10
decimal = 10.5
# mostrar los valosres de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------------------------------------------")
# modificar el valor o los datos de las Variables existentes
numero = 45
decimal = 36.78
print(numero)
print(decimal)

print("------------------------------------------------")

# concatenacion de 2 variables

nombre = "Carlos"
apellido = "Obando"
Web ="carlosobandoweb.com"

print(nombre + " " + apellido + "la pagina web es: " + Web)
# concatenacion con la f"" ejemplo:

print(f"{nombre} {apellido} la pagina web es: {Web}")

# concatenacion con e metodo format:
print("Hola yo soy {} {} y mi pagina web es: {}".format(nombre,apellido,Web))

