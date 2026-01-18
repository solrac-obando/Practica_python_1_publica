# estructura de control de bucles ejercicios del bucle while

"""
el bucle while es una estructura de control que itera o repite una instrucción tantas veces como sean necesarias
en base a una condición, los bucles while requieren de un contador para no generar un bucle infinito,
la estructura del bucle while es:
while condición:
    bloque de instrucciones

"""

print("\n######################## Ejercicio 1 de bucle while ###################### ")
contador = 1
while contador <= 50:
    print(f"Estoy en el número: {contador}")
    contador +=1

numero=1
muestrame=str(0)
while numero <=90:
    muestrame = muestrame + ", " + str(numero)
    numero +=1
print(muestrame)

print("\n######################## Ejercicio 2 de bucle while ###################### ")
print("\n#### tabla de multiplicar ####")
numero_usuario = int(input("¿De qué número quieres la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1 
print(f"#### Tabla de multiplicar del número {numero_usuario} ####")    
numero_tabla = 1 #
while numero_tabla <= 10:
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
    numero_tabla += 1
else:
    print("\ntabla terminada") 