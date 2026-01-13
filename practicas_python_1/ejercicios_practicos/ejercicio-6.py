"""
Ejercicio 6.
mostrar todas las tablas de multiplicar del 1 al 10 y con el titulo de cada tabla
"""
contador= 1
tabla=1
while tabla <= 10:
    print(f"\nla tabla de multiplicar del numero {tabla} es:")
    while contador <= 10:
        print(f"{tabla} x {contador} = {tabla*contador}")
        contador += 1
    tabla += 1
    contador = 1    