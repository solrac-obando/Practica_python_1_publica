"""
Ejercicio 3. escribir un programa que muestre el cuadrado de un numero de los primero 60 
numeros naturales.

"""
# ejercici en el bucle while
num= 0
while num<=60:
    cuadrado = num*num
    print(f"el cuadrado de {num} es el numero {cuadrado}")
    num += 1
# ejercicio en el bucle for

for contador in range(61):
    cuadrado = contador*contador
    print(f"el cuadrado de {contador} es el numero {cuadrado}")

