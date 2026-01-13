"""
que es una condicional es una estructura de control que me permite controlar el flujo de un 
programa , eso quiere decir que si se cumple una condicion se ejecuta un bloque de codigo
y si no se cumple la condicion inicial se ejecuta un bloque de codigo diferente en consecuencia 
de que no se cumplio la primera condicion.


# hoy vamos a realizar practicas de if y else 
ejemplo de condicion, en espanol
Si se cumple la condicion:
    ejecuta el grupo de instrucciones o el bloque de codigo
Si no se cumple la condicion:
    ejecuta el grupo de instrucciones o el bloque de codigo que se utiliza en el caso 
    de que la primera condicion no se cumplio.

ejemplo en ingles y el oficciall de python:
if condicion:
    ejecuta las instruciones;
else:
    ejecuta las instrucciones de contigencia;

    operadores de comparacion en  las condicionales:
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
color = input("adivina Cuál mi color favorito?: ")
edad = int(input("¿Cuál es tu edad?: "))
country = input("¿Cuál es tu país?: ")
continente = input("¿Cuál es tu continente?: ")

if edad >= 18:
    print(f"\n {name} eres mayor de edad {edad}")
    if continente.lower() == "america":
        print (f"{name} es americano y es del pais {country}")
    else:
        print(f"\n{name} no es americano el usuario es de {country}")
else:
    print(f"{name} es menor de edad")


if color == "azul":
    print(f"{name} adivinaste correctamente {color}, es mi color favorito ")
else:
    print("! Error no adibinaste mi color favorito correctamente ", name, "!!!")


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
        print("y además eres un adulto mayor, por lo que en los aeropuertos tienes descuento de la 3ra edad")
    else:
        print("todavias eres un adulto joven ponte a trabajar o minimo estudia algo no seas vago")
else:
    print(f"{name} es menor de edad")
    if edad < 13:
        print("y además eres un niño, por lo que estudia y juega como un verdadero niño")
    else:
        print(f"{name} eres un adolecente consige novia pero no beban alcol todavia")


print("\n######################## Ejemplo 4 de condicional ###################### ")

# el elif es un controlador de condicionales mas limpio y organizado
dia = input("¿Qué día de la semana es?:  ") # input() siempre devuelve una cadena
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("No es un día de la semana")  