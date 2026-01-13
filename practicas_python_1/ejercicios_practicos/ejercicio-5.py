"""
Ejercicio 5, Hacer un programa que muestre toso los numeros que hay entre los datos que 
ingrese el usuario

"""
num1= int(input("ingrese el primer numero: "))
num2= int(input("ingrese el segundo numero: "))

for contador in range(num1,num2):
    print(contador)
    contador += 1