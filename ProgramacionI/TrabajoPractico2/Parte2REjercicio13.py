'''. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
el grupo que le corresponde.'''

nombre = input("Por favor, ingresa tu nombre: ").strip().capitalize()

# Solicitar al usuario que ingrese su sexo (M para mujer, H para hombre)
sexo = input("Por favor, ingresa tu sexo (M para mujer, H para hombre): ").strip().upper()

# Determinar el grupo al que pertenece el usuario
if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

# Mostrar el grupo correspondiente
print("Te corresponde el grupo:", grupo)
