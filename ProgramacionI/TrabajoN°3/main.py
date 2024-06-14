'''Crear un programa que almacene en una lista las materias de esta u otra carrera y que las
muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario).'''

# Lista de materias
materias = {
    "Introducción a la Informática",
    "Programación I",
    "Diseño Gráfico",
    "Arquitectura de Computadoras",
    "Programación II",
    "Sistemas Operativos",
    "Introducción al Desarrollo Web",
    "Beses de Datos",
    "Redes de Datos",
    "Programación III",
    "Ingenieria de Software",
    "Desarrollo de Aplicaciones Web",
    "Desarrollo para Móviles",
    "Multimedia y Juegos en Web",
}

# Para mostrar las materias por pantalla
print("Materias de la Tecnicatura en Desarrollo Web:")
for materia in materias:
    print(f"- {materia}")
