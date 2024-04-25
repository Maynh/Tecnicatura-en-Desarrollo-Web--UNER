''''
Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
derecho que al revés. Por ejemplo: rayar, kayak, somos.
'''

def es_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]
texto = input("Ingrese un texto: ")

if es_palindromo(texto):
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")
