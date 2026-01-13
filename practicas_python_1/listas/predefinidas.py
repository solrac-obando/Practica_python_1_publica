
cantantes =["Michael Jackson", "Bey", "Jennifer Lopez"]
numeros=[1,2,3,0,5,9,4]

# ordenar

print(cantantes)
print(numeros)
numeros.sort()
print("\n")
print(numeros)

#añadir elementos
print("Agregar elementos a la  listas\n")
cantantes.append("Juanes")
print(cantantes)
cantantes.insert(1,"Beyoncé")
print(cantantes)

#eliminar elementos
print("Elimininacion de elementos en listas\n")
#numeros.pop(6)
#print(numeros)
cantantes.remove("Juanes")
print(cantantes)

# Dar la vuelta a la lista
print("Invertir el orden de los elementos en la listas\n")

print(f"lista con los numeros ordenados: {str(numeros)}")
numeros.reverse()
print(f"Lista con los numeros Invertidos: {str(numeros)}")

print("Indicar cuantas veces aparece un elemento o en este caso un numero en la lista")
print(numeros.count(2))# la funcion count() es valido para todos los tipos de datos.

print("Union de elementos entre 2 o mas listas o en otras palabrar unir listas")

#unir listas
cantantes.extend(numeros)
print(cantantes)