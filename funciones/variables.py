"""
funciones con variables globales y locales, las variables globales se definen fuera de
las funciones permitiendo que estas variables sean o puedan ser utilizadas por todas
las funciones que llamen las variables globales
las variables locales son aquellas que se definen dentro de una función por lo tanto son
variables locales de la función en la que fueron definidas, estas variables no pueden ser
utilizadas por otras funciones ya que operan y se definieron dentro de una función en
específico se podría decir que son privadas de la función en donde se definió o creó

"""
print("\n########## Ejercicios 8 - funciones con variables locales y globales ########")

frace= "Ni los genios son tan genios, y la personas mediocres no son tan mediocres\n"
print(frace)
def holaMundo():
    frace= "hola mundo" # si se comenta esta variable entonces el print de la función usa la variable global con el nombre frase
    print("\nDentro de una funcion")
    print(frace)
    year= 2026
    print(year)

    global webside
    webside = "carlosObandoweb.ve"
    print(f"Dentro de la funcion {webside}")


    return "Dentro de la funcion " + str(year)
holaMundo()
#print(year) # este print genera un error porque la variable que quiere usa solo esta definida dentro de la funcion

print(f"Probando como transformar una variable local a una global dentro de una función: {webside}")