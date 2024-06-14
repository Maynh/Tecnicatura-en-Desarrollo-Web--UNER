''''Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son
múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos
ejemplos de posiblesrespuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900
no es bisiesto'''

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
