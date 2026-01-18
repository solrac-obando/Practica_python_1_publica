"""
Ejercicio 3. Escribir un programa que muestre el cuadrado de un número de los primeros 60
números naturales.

"""
# ejercicio en el bucle while
num= 0
while num<=60:
    cuadrado = num*num
    print(f"el cuadrado de {num} es el número {cuadrado}")
    num += 1
# ejercicio en el bucle for

for contador in range(61):
    cuadrado = contador*contador
    print(f"el cuadrado de {contador} es el número {cuadrado}")

