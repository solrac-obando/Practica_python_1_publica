"""
Crear un programa que compruebe si una variable está vacía, y si está vacía rellenar la
variable con texto, en minúscula y en mayúscula, por último mostrar en pantalla

"""
variable = ""  # Variable vacía
if len(variable.strip()) <=0: # se utiliza len para ver la longitud y strip para eliminar espacios.
    print("La variable está vacía")
    variable = input("Por favor introduce un texto para la variable: ")
    print(f"Gracias por llenar la variable y te confirmo que el texto es: {variable.lower()}")
    print(f"Gracias por llenar la variable y te confirmo que el texto es: {variable.upper()} en letras mayúsculas.")
else:
    print("La variable ya tiene contenido")
    print("Gracias por participar!")
    print(variable)