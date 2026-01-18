"""
Los módulos son funcionalidades que ya fueron creadas por la comunidad de Python o por
el propio creador del lenguaje que están disponibles para utilizar en cualquier momento,
algunas ya están preconfiguradas en las versiones más recientes del lenguaje y otras hay
que importarlas por cuenta propia, también los módulos con funciones que yo como programador
puedo crear y empaquetar para mi propio uso futuro o para compartir, en resumen son
paquetes de funciones de código reutilizables para aplicar en programas escritos o creados
en Python.

Puedes consultar los módulos en la documentación oficial de Python en el siguiente
enlace: https://docs.python.org/es/3.14/py-modindex.html
"""
#Importar Módulo Propio
from mimodulo import HolaMundo
import datetime
print(HolaMundo("Juan"))
print("\n ")
print("########### Ejemplo de modulo de fecha ############")
#modulo fechas
print(datetime.date.today())
fecha_completa = datetime.datetime.now() # es una propiedad que extrae la fecha, hora y segundos actuales
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, ")
print("\n ")
"""
día es = (%d) la "d" en minúscula, mes es = (%m) la "m" en minúscula, año es = (%Y) la "Y" en mayúscula
para hora es = (%H) con la "H" en mayúscula y para minutos es = (%M) la "M" en mayúscula
los segundos son = (%S) con la "S" en mayúscula
"""
print(fecha_personalizada)

# módulo de matemáticas
import math
print("########### Ejemplo de módulo de Matemáticas ############")

print(f"Raíz cuadrada de 25 es = {math.sqrt(25)}")
print("\n ")
print(f"Numero pi es = {math.pi}")
print("\n ")
print(f"Redondear = {math.ceil(5.8186516181516)}")


