"""
ejercicio 4 crear una calculadora con los numero de que le solicitan al usuario


"""

num1= input("ingrese el primer numero: ")
num2= input("ingrese el segundo numero: ")
print("Para realizar el calculo debe ingresar una de las siguinetes opciones para realizar la operacion: ")
print("\n + , - , x , / \n")

operacion = input("ingrese la operación que desea realizar: ")
print("############ Calculadora ##############")
if operacion == "+":
    print(int(num1)+int(num2))
elif operacion == "-":
    print(int(num1)-int(num2))
elif operacion == "x":
    print(int(num1)*int(num2))
elif operacion == "/":
    print(int(num1)/int(num2))
else:
    print("operación no válida")