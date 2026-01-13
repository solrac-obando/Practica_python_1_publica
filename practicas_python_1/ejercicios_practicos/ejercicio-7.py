"""
Ejercicio 7: Crear un programa que muestre los numero imperes de los numero que el usuario ingrese


"""

num1= int(input("ingrese el primer numero: "))
num2= int(input("ingrese el segundo numero: "))
if num1 < num2:
    for contador in range(num1,num2):
        if contador % 2 != 0:
            print(contador)
        contador += 1
else:
    print("el primer numero debe ser menor al segundo numero")