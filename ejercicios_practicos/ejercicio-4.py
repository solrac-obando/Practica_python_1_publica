"""
Ejercicio 4. Crear una calculadora con los números que le solicita al usuario


"""

num1= input("Ingrese el primer número: ")
num2= input("Ingrese el segundo número: ")
print("Para realizar el cálculo debe ingresar una de las siguientes opciones para realizar la operación: ")
print("\n + , - , x , / \n")

operacion = input("Ingrese la operación que desea realizar: ")
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
    print("Operación no válida")