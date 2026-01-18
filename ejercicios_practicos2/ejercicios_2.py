"""
crear un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar
la lista por pantalla.


"""
lista=[]

for contador in range(1, 121):
    print(contador)
    lista.append(contador)
print("Añadiendo un nuevo valor a la lista")

print(f"La lista actual es: {lista}") 

"""numero = 0
while numero <= 119:
    numero = numero + 1
    print(numero)
    lista.append(numero)

print(f"La lista actual es: {lista}")"""

    