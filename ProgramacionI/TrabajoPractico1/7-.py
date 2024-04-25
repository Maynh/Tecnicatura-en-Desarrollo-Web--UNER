'''
Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y
segundos son esos números de días.
'''

dias = int(input("Ingrese un número de días: "))

horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print(f"{dias} días son equivalentes a:")
print(f"{horas} horas")
print(f"{minutos} minutos")
print(f"{segundos} segundos")
