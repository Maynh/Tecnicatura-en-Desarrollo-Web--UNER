'''
Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el
resultado.
'''

def elevar_a_potencia(numero, potencia):
    if numero < 0:
        return "El número debe ser entero positivo"
    return numero ** potencia

resultado = elevar_a_potencia(2, 3)
print(resultado)
