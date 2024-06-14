'''Que muestre todoslos números primos entre 0 y 100 e imprima cuántos números primos hay.'''

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Lista para almacenar los números primos
primos = []

# Buscar números primos entre 0 y 100
for num in range(101):
    if es_primo(num):
        primos.append(num)

# Imprimir los números primos
print("Números primos entre 0 y 100:", primos)

# Imprimir la cantidad de números primos
print("Cantidad de números primos entre 0 y 100:", len(primos))
