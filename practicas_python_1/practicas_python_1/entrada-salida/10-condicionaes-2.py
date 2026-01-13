# programa para determina si el usuario es apto para trabajar deacuardo a las leyes del pais
""" opreadores de logicos en las condicionales:
and (esto es que se debe de cumplir con 2 condiciones en un mismo if) significa Y 
or (es para que se cumpla una de las 2 condiciones) significa O
not () significa NO


"""
 

print("\n######################## Ejercicio 1 de condiciones ###################### ")
edad_minima = 18
edad_maxima = 65
edad_usuario = int(input("¿Cuál es tu edad?: "))
if edad_usuario >= edad_minima and edad_usuario <= edad_maxima:
    print(f"¡tienes la edad necesaria para trabajar!")
else:
    print("Entendemos que deseas trabajar pero eres muy joven para ello en este pais")


print("\n######################## Ejercicio 2 de condiciones avanzadas ###################### ")
edad_trabajador = int(input("¿Cuál es la edad actual del empleado?: "))

if edad_trabajador >= edad_minima and edad_trabajador <= edad_maxima:
    print(f"El empleado tiene la edad legal para trabajar")
else:
    print("El empleado no tiene la edad legal para trabajar")


print("\n######################## Ejercicio 3 de condiciones avanzadas ###################### ") 

# determinar si el pais es de habla hispana
pais = input("Nos puedes decir de que pais eres?: ")
if pais == "argentina" or pais == "Venezuela" or pais == "mexico" or pais == "colombia" or pais == "Espana":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} no es un país de habla hispana")


print("\n######################## Ejercicio 4 de condiciones avanzadas ###################### ")