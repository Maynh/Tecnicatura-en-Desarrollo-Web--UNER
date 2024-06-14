'''Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
en que ambos números son iguales.'''

# Solicitar al usuario que ingrese dos números
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))

# Comparar los números y mostrar cuál es menor
if numero1 < numero2:
    print(f"El primer número ({numero1}) es menor que el segundo número ({numero2}).")
elif numero1 > numero2:
    print(f"El segundo número ({numero2}) es menor que el primer número ({numero1}).")
else:
    print("Ambos números son iguales.")
