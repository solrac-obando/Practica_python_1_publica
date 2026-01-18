"""
Docstring for OOP-constructor.main

"""
from carro import carro

carro1 = carro("Amarillo", "Renault", "Clio", 150, 300, 4)
carro2 = carro("Azul", "Renault", "Logan", 250, 450, 5)
carro3 = carro("Negro", "Toyota", "Corolla", 250, 500, 5)
carro4 = carro("Rojo", "Chevrolet", "Aveo", 280, 500, 6)

print(carro1.getinfo())
print(carro2.getinfo())
print(carro3.getinfo())
print(carro4.getinfo())

# carro3 = "Prueba de condicional"

if type(carro3) == carro:
    print("Es Un Objeto que pertenece a la clase de carro")
else:
    print("No es un objeto de tipo Carro")

# Visibilidad de una clase, detro de una class se pueden definir
# los metodos tanto publicos como pribados para restringir la modificacion de datos.

print(carro1.soy_publico)
print(carro1.getPrivado()) # cuidado con los nombres de las variables que si no lo colocas de forma correcta ocurre erroes