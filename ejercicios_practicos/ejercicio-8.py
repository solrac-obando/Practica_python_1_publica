"""
Ejercicio 8. Crear un programa para extraer el porcentaje de 2 números que el usuario ingrese

"""

num= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el valor del porcentaje del primer número: "))

porcentaje = (num*(num2/100))

print(f"El porcentaje de {num2}% de {num} es igual a {int(porcentaje)}")
