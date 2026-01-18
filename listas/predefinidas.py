
cantantes =["Michael Jackson", "Bey", "Jennifer Lopez"]
numeros=[1,2,3,0,5,9,4]

# ordenar

print(cantantes)
print(numeros)
numeros.sort()
print("\n")
print(numeros)

#añadir elementos
print("Agregar elementos a las listas\n")
cantantes.append("Juanes")
print(cantantes)
cantantes.insert(1,"Beyoncé")
print(cantantes)

#eliminar elementos
print("Eliminación de elementos en listas\n")
#numeros.pop(6)
#print(numeros)
cantantes.remove("Juanes")
print(cantantes)

# Dar la vuelta a la lista
print("Invertir el orden de los elementos en las listas\n")

print(f"lista con los números ordenados: {str(numeros)}")
numeros.reverse()
print(f"Lista con los números Invertidos: {str(numeros)}")

print("Indicar cuántas veces aparece un elemento o en este caso un número en la lista")
print(numeros.count(2))# la función count() es válido para todos los tipos de datos.

print("Unión de elementos entre 2 o más listas o en otras palabras unir listas")

#unir listas
cantantes.extend(numeros)
print(cantantes)