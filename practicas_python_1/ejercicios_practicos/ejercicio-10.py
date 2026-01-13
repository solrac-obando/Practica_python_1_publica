"""
Ejercicio 10: crear un programa que pida al usuario la notas de 15 alumnos 
y mostrar quiene aprobo y reprobo

"""
# Pedir nombres y notas para 15 alumnos
"""notas = {}  # Diccionario para almacenar nombre: nota

for i in range(15):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    notas[nombre] = nota

# Mostrar aprobados y reprobados
print("\nAlumnos aprobados:")
for nombre, nota in notas.items():
    if nota >= 60:  # Asumiendo que 60 es la nota de aprobación
        print(f"{nombre}: {nota}")

print("\nAlumnos reprobados:")
for nombre, nota in notas.items():
    if nota < 60:
        print(f"{nombre}: {nota}")
"""

contador = 1
aprobados=0
reprobados=0
numero_de_alumnos= int(input("ingrese el numero de alumnos: "))
while contador < numero_de_alumnos:
    nombre = input(f"Ingrese el nombre del alumno {contador+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    if nota >= 5:
        aprobados += 1
    else:
        reprobados += 1 
    contador += 1

print(f"Alimnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")
    

   