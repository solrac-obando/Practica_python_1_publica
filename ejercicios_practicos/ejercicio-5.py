"""
Ejercicio 5. Hacer un programa que muestre todos los números que hay entre los datos que
ingrese el usuario

"""
num1= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))

for contador in range(num1,num2):
    print(contador)
    contador += 1