"""
Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano.
Luego debe imprimir el tipo de variable por pantalla.

"""

num1= int(input("Introduce el primer dígito: "))
num2 = int(input("Introduce el segundo dígito: "))
mayor = num1 > num2
def test(dato, tipo):
    comprobar = isinstance(dato, tipo)
    resul=""
    if comprobar:
        resul = f"Este dato es de tipo {type(dato)}"
    else:
        resul = f"Es un tipo de dato incorrecto"
    return resul


if mayor == True:
    print(f"el dígito {num1}, es mayor que {num2}", f"Y la operacion es un {type(mayor)} {mayor}")
    print("\n")
else:
    print(f"El dígito {num2} es mayor que {num1} Y la operacion es un {type(mayor)} {mayor}")
    print("\n")

cantantes =["beyonce","rihanna","katy perry",]
nombre= "Carlos :)"

print(f"Lista de Cantantes: {cantantes}, " + test(cantantes, list))
print("\n")
print(f"Lista de Cantantes: {nombre}, "  + test(nombre, str)) 
print("\n")
print("También recuerda que los tipo de datos que introduciste son: " + test(num1, int))
print("\n")
print(f"También recuerda que los tipo de datos que introduciste son: " + test(num2, str)) # este es incorrecto como ejemplo de la funcion
print("\n")
print(f"También recuerda que los tipo de datos que introduciste son: " + test(num2, int))