'''Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
encuentran en dicha frase.
'''

frase = input("Por favor, ingresa una frase: ")

# Inicializar el contador de vocales
contador_vocales = 0

vocales = "aeiouAEIOU"

# Recorrer cada carácter en la frase
for caracter in frase:
    # Verificar si el carácter es una vocal
    if caracter in vocales:
        contador_vocales += 1

# Imprimir la cantidad de vocales en la frase
print("La cantidad de vocales en la frase es:", contador_vocales)
