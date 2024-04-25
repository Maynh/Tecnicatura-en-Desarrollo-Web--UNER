'''
Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y
luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
forma: “La respuesta es XX”.

'''

num1 = float(input("Por favor, ingresa el primer número: "))
num2 = float(input("Ahora ingresa el segundo número: "))
num3 = float(input("Por último, ingresa el tercer número: "))

suma = num1 + num2

resultado = suma * num3

print("La respuesta es", resultado)
