import os 

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("La carpeta ya existe")

# Eliminar carpeta
"""
os.rmdir("./mi_carpeta") # Solo si la carpeta existe
"""
#
print("Contenido de mi carpeta")
contenido= os.listdir("./mi_carpeta")
print(contenido)
