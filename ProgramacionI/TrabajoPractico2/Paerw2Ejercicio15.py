''''Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe
validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
informarle que no se puede procesar el dato.'''


year = int(input("Por favor, ingresa un año: "))

# Determinar si el año es bisiesto
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    es_bisiesto = True
else:
    es_bisiesto = False

# Mostrar el resultado
if es_bisiesto:
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")
