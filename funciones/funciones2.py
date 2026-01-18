print("#############################Ejemplo 5 de funciones ##########################")

# ejemplo 5 de return o devolución de datos
def saludame(nombre):
    saludo = f"Hola {nombre}, bienvenido"
    return saludo
print(saludame("Carlos Obando"))
print("\n")

"""num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

def calculadora(num1, num2, basicos = False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divi = num1 / num2  

    cadena= ""
    if basicos == True:
        cadena += "Suma =: " + str(suma)
        cadena += "\n"
        cadena += f"Resta =: " + str(resta)
    else:
        cadena += f"Multiplicacion =: " + str(multi)
        cadena += "\n"
        cadena += f"Division =:" + str(divi)
    
    return cadena

print(calculadora(num1, num2, True))"""

print("\n###################### Ejercicios 6 ####################")
def getNombre(nombre):
    texto = f"El  Nombre es: {nombre}"
    return texto

def getApellido(apellidos):
    texto = f"los Apellidos son: {apellidos}"
    return texto

def mostrarTodo(nombre, apellido):
    texto= getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(mostrarTodo("Carlos","Obando Aure"))

print("\n###################### Ejercicios 7 ####################")
# funciones lambda, son funciones anónimas para realizar código simple o operaciones concretas
dime_el_year =lambda year: f"the year is {year * 2}"
#year= 2026
print(dime_el_year(1013))# se debe de imprimir con la variable que se definió en la función lambda



