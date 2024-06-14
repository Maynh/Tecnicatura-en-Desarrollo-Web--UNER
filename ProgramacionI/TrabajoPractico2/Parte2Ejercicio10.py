'''Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
a. Todoslos númerosimpares desde 1 hasta ese número separados por comas.
b. La cuenta atrás desde ese número hasta cero separados por comas.
c. Que indique si es primo o no.
d. Por último,su factorial.'''


# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Por favor, ingresa un número entero positivo: "))

# a. Mostrar todos los números impares desde 1 hasta el número ingresado, separados por comas
impares = []
for i in range(1, numero + 1):
    if i % 2 != 0:
        impares.append(str(i))
print("Números impares desde 1 hasta {}: {}".format(numero, ", ".join(impares)))

# b. Mostrar la cuenta atrás desde el número ingresado hasta cero, separados por comas
cuenta_atras = []
for i in range(numero, -1, -1):
    cuenta_atras.append(str(i))
print("Cuenta atrás desde {} hasta 0: {}".format(numero, ", ".join(cuenta_atras)))

# c. Verificar si el número ingresado es primo
es_primo = True
if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("{} es un número primo.".format(numero))
else:
    print("{} no es un número primo.".format(numero))

# d. Calcular el factorial del número ingresado
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print("El factorial de {} es: {}".format(numero, factorial))
