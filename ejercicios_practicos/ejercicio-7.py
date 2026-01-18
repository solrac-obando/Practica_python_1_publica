"""
Ejercicio 7. Crear un programa que muestre los números impares de los números que el usuario ingrese


"""

num1= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))
if num1 < num2:
    for contador in range(num1,num2):
        if contador % 2 != 0:
            print(contador)
        contador += 1
else:
    print("El primer número debe ser menor que el segundo número")