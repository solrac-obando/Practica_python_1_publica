mejores_practicas_programacion = {
    "nombres_descriptivos": "Usa nombres de variables, funciones y clases que sean descriptivos y signifiquen lo que representan.",
    "comentarios": "Agrega comentarios en el código para explicar la lógica compleja o el propósito de secciones específicas.",
    "pep8": "Sigue las guías de estilo PEP 8 para Python, incluyendo indentación, espacios y convenciones de nomenclatura.",
    "funciones_modulares": "Divide el código en funciones pequeñas y modulares que realicen una sola tarea.",
    "manejo_excepciones": "Usa bloques try-except para manejar errores y excepciones de manera elegante.",
    "evitar_codigo_duplicado": "Reutiliza código mediante funciones, clases o módulos para evitar duplicación.",
    "pruebas_unitarias": "Escribe pruebas unitarias para verificar que el código funcione correctamente.",
    "version_control": "Usa un sistema de control de versiones como Git para rastrear cambios y colaborar.",
    "documentacion": "Documenta tu código con docstrings para funciones y clases.",
    "seguridad": "Considera aspectos de seguridad, como validación de entradas y manejo de datos sensibles.",
    "rendimiento": "Optimiza el código para rendimiento cuando sea necesario, pero prioriza la legibilidad.",
    "consistencia": "Mantén consistencia en el estilo de codificación a lo largo del proyecto.",
    "evitar_variables_globales": "Minimiza el uso de variables globales; pasa datos como parámetros en su lugar.",
    "orden_codigo": "Organiza el código en orden lógico: imports, constantes, funciones, clase principal.",
    "comprensiones_listas": "Usa comprensiones de listas para crear listas de manera concisa y legible.",
    "imports_proper": "Importa solo lo necesario y usa imports absolutos para evitar conflictos.",
    "entornos_virtuales": "Usa entornos virtuales para gestionar dependencias y evitar conflictos entre proyectos.",
    "revisiones_codigo": "Realiza revisiones de código por pares para mejorar calidad y detectar errores.",
    "integracion_continua": "Implementa integración continua para automatizar pruebas y despliegues.",
    "logging": "Usa el módulo logging en lugar de print para depuración y monitoreo de aplicaciones.",
    "type_hints": "Agrega type hints para mejorar la legibilidad y permitir detección temprana de errores.",
    "funciones_cortas": "Mantén las funciones cortas; idealmente menos de 20 líneas para facilitar la lectura."
}

print("\nMejores prácticas en programación estándar:\n")
for clave, descripcion in mejores_practicas_programacion.items():
    print(f"{clave}: {descripcion}")
    print()  # Salto de línea para mayor legibilidad