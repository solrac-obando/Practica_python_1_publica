"""
Ejercicio 6.
Mostrar todas las tablas de multiplicar del 1 al 10 y con el título de cada tabla
"""
contador= 1
tabla=1
while tabla <= 10:
    print(f"\nLa tabla de multiplicar del número {tabla} es:")
    while contador <= 10:
        print(f"{tabla} x {contador} = {tabla*contador}")
        contador += 1
    tabla += 1
    contador = 1    