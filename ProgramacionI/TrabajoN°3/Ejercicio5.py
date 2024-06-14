''' Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno
de los números ingresados por el usuario deberá ser almacenado en una lista. A
continuación, realice las siguientes tareas:
a. Determinar el máximo.
b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
c. Determinar el mínimo.
d. Calcular la multiplicación de todos los números de la lista.
e. Contar los valores pares e impares.
f. Remover los elementos repetidos.
'''

numeros = []

# Solicitar al usuario el ingreso de números enteros
while True:
    entrada = input("Ingrese un número entero o 'fin' para terminar: ")
    if entrada.lower() == "fin":
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Verificar si la lista de números no está vacía
if not numeros:
    print("No se ingresaron números.")
else:
    # a. Determinar el máximo
    maximo = max(numeros)
    print("Máximo:", maximo)

    # b. Obtener segundo valor máximo
    if len(numeros) > 1:
        numeros_sin_maximo = [num for num in numeros if num != maximo]
        if numeros_sin_maximo:
            segundo_maximo = max(numeros_sin_maximo)
            print("Segundo valor máximo:", segundo_maximo)
        else:
            print("No hay un segundo valor máximo distinto.")
    else:
        print("No hay suficientes números para determinar un segundo valor máximo.")

    # c. Determinar el mínimo
    minimo = min(numeros)
    print("Mínimo:", minimo)

    # d. Calcular la multiplicación de todos los números de la lista
    multiplicacion = 1
    for num in numeros:
        multiplicacion *= num
    print("Multiplicación de todos los números:", multiplicacion)

    # e. Contar los valores pares e impares
    pares = sum(1 for num in numeros if num % 2 == 0)
    impares = len(numeros) - pares
    print("Cantidad de valores pares:", pares)
    print("Cantidad de valores impares:", impares)

    # f. Remover los elementos repetidos
    numeros_sin_repetidos = list(set(numeros))
    print("Lista sin elementos repetidos:", numeros_sin_repetidos)
