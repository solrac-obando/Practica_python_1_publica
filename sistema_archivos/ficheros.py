from io import open
import pathlib # es una libreria que ayuda a encontrar la posición absoluta de un archivo o fichero
import shutil # es para copiar o mover archivos, tanto dentro como fuera de otras carpetas
import os # es para la eliminacion de archivo
import os.path # es para comprobar si un archivo existe o no 

# abrir o crear un Archivo
"""
archivo = open('./sistema_archivos/archivo.txt') esta variable no logra abrir el
fichero porque le faltaban los permisos requeridos para el manejo de ficheros ejemplo '+a'

la forma de encontra y abrir cualquier fichero de forma segura es con la ruta absoluta
para encontrar la ruta absoluta se puede usar la funcion os.path o pathlib.Path().absolute() 
"""

print("########## Ejercicio 1 abrir o crear  ##############")

ruta = './archivo.txt'
#print(ruta)
"""
archivo = open(ruta,"+a")

archivo.write("Hola mundo estoy escribiendo texto en un archivo/fichero desde un codigo \n" \
"en python, es una prueba de ejercicos de manipulacion de archivos/ficheros.")
archivo.close()
"""

# leer contenido
print("########## Ejercicio 2 leer contenido ##############")

archivo_lectura = open(ruta,"r")
#contenido= archivo_lectura.readline()
#print(contenido)
lista = archivo_lectura.readlines()

for frase in lista:
    print("- " +frase.upper())
archivo_lectura.close()

"""
#copiar archivo

ruta_original = './archivo.txt'
ruta_nueva = str(pathlib.Path().absolute()) + '/sistema_archivos/archivo_copiado.txt'
ruta_alternativa = str(pathlib.Path().absolute()) + "./paquetes/archivo_copiado.txt"

# Logs para depuración
print(f"Ruta original: {ruta_original}")
print(f"Ruta nueva (no usada): {ruta_nueva}")
print(f"Ruta alternativa: {ruta_alternativa}")

shutil.copyfile(ruta_original, ruta_alternativa)

"""

#mover archivos

"""

shutil.move(ruta_original, ruta_nueva)



"""
print(os.path.abspath("../"))

# comprobar si existe un fichero
if os.path.isfile(ruta):
    print("El archivo existe")
else:
    print("El archivo no existe")

# eliminar un fichero


