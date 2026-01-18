
def HolaMundo(nombre):

    return f"Hola, ¿cómo estás? Bienvenido al módulo de prueba de calculadora {nombre}"


def calculadora(num1,num2,operacion):

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


if __name__ == "__main__":
    num1= input("ingrese el primer número: ")
    num2= input("ingrese el segundo número: ")
    print("Para realizar el cálculo debe ingresar una de las siguientes opciones para realizar la operación: ")
    print("\n + , - , x , / \n")
    operacion = input("ingrese la operación que desea realizar: ")
    print(HolaMundo("Carlos"))
    calculadora(num1,num2,operacion)
