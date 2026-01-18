import clases
persona = clases.Persona()
persona.setNombre("Carlos")
persona.setApellido("Obando")
persona.setAltura("178 Cm")
persona.setEdad("26 Year")
print(f"La persona es: {persona.getNombre()} {persona.getApellido()}")
print(persona.Hablar())
print("--------------------------------------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Luis")
informatico.setApellido("Peres")
print(f"La persona es: {informatico.getNombre()} {informatico.getApellido()}")
print(informatico.Hablar())
print(informatico.Dormir())
print(informatico.getExperiencia())

print("--------------------------------------------------------------")
tecnico = clases.TecnicoRedes()
print(tecnico.auditorRedes, tecnico.getLenguajes())


