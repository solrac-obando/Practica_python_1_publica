"""
Crear una lista con el contenido de esta tabla:
ACCION | AVENTURA|  |DEPORTES
GTA    | CRASH   | F1       |
COD     |ASSINS  |FIFA 21  |
PUGD   |TOMB RAIDER| FIFA 


"""
tabla=[
    {
        "categoria":"ACCION",
        "juegos":["GTA", "COD","PUBG"]
    },
    {
        "categoria":"AVENTURA",
        "juegos":["CRASH", "ASSASSINS", "TOMB RAIDER"]

    },
    {
        "categoria":"DEPORTES",
        "juegos":["F1", "FIFA 21","FIFA"]
    }
]
for categoria in tabla:
    print(f"--------------{categoria["categoria"]}-----------------")
    for juego in categoria["juegos"]:
        print(juego)
