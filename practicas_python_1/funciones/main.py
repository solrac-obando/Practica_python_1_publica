"""
Las funciones son un bloque de codigo agrupago bajo un nombre concreto, o como un titulo 
del conjunto de instruciones por ejemplo print(),
para ejecutar o reutilizar un conjunto de codigo de forma indefinida, esto a travez de llamar
al nombre de la funcion de tiene como titulo

estructura: para definir una nueva funcion se utiliza el comando (def) que se usa para
definir el numbre de la nueva funcion y luego del def el nombre de la funcion, por ultimo los ()
que se utiliza para definir parametros de la funcion,
def nombre_Alumno():
    codigo reutilizable del conjunto a ejecutar
"""
# Ejemplo 1

print("############ Ejemplo 1 ###############")

def muestraDatos():
    name= input("Cual es tu nombre:? ")
    print(name)
    #print(name)
    #print(name)
    print("\n")

#muestraDatos()




# Ejemplo 2 Paramentros normales


print("############# Ejemplo 2 ####################")

nombre = "Victor Obando" # o con un input("Cual es tu nombre:? ") 
edad = int(input("Cual es tu edad:? "))
def mostrarTuNombre (nombre, edad): # parametro nombre
    print(f"Tu nombre es {nombre}")
    if edad >=18:
        print(f"Hola {nombre}, un gusto eres Mayor de edad tienes {edad}")
    print("\n")
# variable 
#mostrarTuNombre(nombre, edad)




print("############# Ejemplo 3 ####################")

numero= int(input("selecciona un numero para visualizar la tabla: "))
def tabla(numero):
    print(f"tabla de muntiplicar del numero: {numero}")
    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} es igual a {operacion}")
    contador += 1

    print("\n")
tabla(numero)

for numero_tabla in range(10):
    tabla(numero_tabla)

print("############# Ejemplo 4 ####################")
def getEmpleado(nombre, dni =None):
    print("Empleado")
    print(f"Nombre: {nombre}, puesto tutor de programacion")

    if dni != None:
        print(f"El Numero de identificacion o Dni Es: {dni}")
getEmpleado(nombre,)# ejemplo sin datos en el parametro dni para demostrar que es un parametro opcional
getEmpleado(nombre, 528468128)# ejemplo con datos en el parametro dni

