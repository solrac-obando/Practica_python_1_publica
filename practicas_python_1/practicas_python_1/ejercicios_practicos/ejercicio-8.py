"""
Ejercicio 8: crear un programa para extraer el porcentaje de 2 numeros que usuario ingrese

"""

num= int(input("ingrese el primer numero: "))
num2= int(input("ingrese el el valor del porcentage del primer numero: "))

porcentaje = (num*(num2/100))

print(f"el porcentaje de {num2}% de {num} es igual a {int(porcentaje)}")
