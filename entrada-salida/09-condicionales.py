"""
Qué es una condicional es una estructura de control que me permite controlar el flujo de un
programa , eso quiere decir que si se cumple una condición se ejecuta un bloque de código
y si no se cumple la condición inicial se ejecuta un bloque de código diferente en consecuencia
de que no se cumplió la primera condición.


# hoy vamos a realizar prácticas de if y else
ejemplo de condición, en español
Si se cumple la condición:
    ejecuta el grupo de instrucciones o el bloque de código
Si no se cumple la condición:
    ejecuta el grupo de instrucciones o el bloque de código que se utiliza en el caso
    de que la primera condición no se cumplió.

ejemplo en inglés y el oficial de python:
if condicion:
    ejecuta las instrucciones;
else:
    ejecuta las instrucciones de contingencia;

    operadores de comparación en  las condicionales:
 == igual que
 != diferente
 < menor que
 > mayor que
 <= menor o igual que
 >= mayor o igual que
and (esto de que cumplan con 2 condiciones en un mismo if) 
or ()
not ()
&&

"""
print("\n######################## Ejemplo 1 de condicional ###################### ")
name = input("¿Cuál es tu nombre?: ")
color = input("adivina cuál mi color favorito?: ")
edad = int(input("¿Cuál es tu edad?: "))
country = input("¿Cuál es tu país?: ")
continente = input("¿Cuál es tu continente?: ")

if edad >= 18:
    print(f"\n {name} eres mayor de edad {edad}")
    if continente.lower() == "america":
        print (f"{name} es americano y es del país {country}")
    else:
        print(f"\n{name} no es americano el usuario es de {country}")
else:
    print(f"{name} es menor de edad")


if color == "azul":
    print(f"{name} adivinaste correctamente {color}, es mi color favorito ")
else:
    print("! Error no adivinaste mi color favorito correctamente ", name, "!!!")


print("\n######################## Ejemplo 2 de condicional ###################### ")

year = int(input("¿En qué año estamos?: "))
nacido = int(input("¿En qué año naciste?: "))
edad = year - nacido

if edad >= 18:
    print(f"\n{name} eres mayor de edad {edad}")
else:
    print(f"{name} es menor de edad")


print("\n######################## Ejemplo 3 de condicional ###################### ")

# if o condiciones anidadas una dentro de la otra

if edad >= 18:
    print(f"{name} eres mayor de edad {edad}")
    if edad >= 65:
        print("y además eres un adulto mayor, por lo que en los aeropuertos tienes descuento de la tercera edad")
    else:
        print("todavía eres un adulto joven ponte a trabajar o mínimo estudia algo no seas vago")
else:
    print(f"{name} es menor de edad")
    if edad < 13:
        print("y además eres un niño, por lo que estudia y juega como un verdadero niño")
    else:
        print(f"{name} eres un adolescente consigue novia pero no beban alcohol todavía")


print("\n######################## Ejemplo 4 de condicional ###################### ")

# el elif es un controlador de condicionales más limpio y organizado
dia = input("¿Qué día de la semana es?:  ") # input() siempre devuelve una cadena
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("No es un día de la semana")  