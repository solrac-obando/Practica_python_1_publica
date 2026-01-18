# estructura de control de bucles ejercicios del bucle for

"""
el bucle for es una estructura de control que repite una instrucción o código una cantidad determinada de
veces, la estructura del bucle for es:
for variable in elemento_iterable pueden ser (listas, diccionarios, tuplas, cadenas de texto y principalmente rangos)
    bloque de instrucciones

"""

print("\n######################## Ejercicio 1 de bucle for ###################### ")

contador = 0
resultado = 0
for contador in range(0,10):
    print(f" Voy por el número {contador}")
    resultado += contador

print("la suma de todos los números es: ", resultado)

print("\n######################## Ejercicio 2 de bucle for ######################")
print("\n#### tabla de multiplicar ####")
numero_usuario = int(input("¿De qué número quieres la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1
print(f"#### Tabla de multiplicar del número {numero_usuario} ####")    
for numero_table in range(1,11):
    # se puede crear un if dentro del propio bucle para crear una restricción o condición si el
    # programa lo amerita el ejemplo es la tabla del número 45
    if numero_usuario == 45:
        print(f"la tabla de multiplicar del número {numero_usuario} no está disponible")
        break
    
    print(f"{numero_usuario} x {numero_table} = {numero_usuario * numero_table}")
else:
    print("\ntabla terminada")



#print("\n######################## Ejercicio 3 de bucle for ######################")
# se puede usar la función len() para saber la cantidad de elementos que hay en una lista o una cadena de texto



