'''Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
realizar lo siguiente:
a. Imprimir la cantidad de elementos que tiene la lista.
b. Imprimir el primer y último elemento.
c. Imprimir el resto.
d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
la lista. Quitar el elemento correspondiente de esa posición.
f. Imprimir la lista en orden inverso.
g. Vaciar la lista.'''

paises = ["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]

# a. Imprimir la cantidad de elementos que tiene la lista
print("Cantidad de elementos en la lista:", len(paises))

# b. Imprimir el primer y último elemento
print("Primer elemento:", paises[0])
print("Último elemento:", paises[-1])

# c. Imprimir el resto
print("Resto de los elementos:", paises[1:-1])

# d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista
pais_ingresado = input("Ingrese un país: ")
if pais_ingresado in paises:
    print(f"El índice de {pais_ingresado} es:", paises.index(pais_ingresado))
else:
    print(f"{pais_ingresado} no se encuentra en la lista.")

# e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición.
numero_ingresado = int(input(f"Ingrese un número (0 a {len(paises)-1}): "))
if 0 <= numero_ingresado < len(paises):
    pais_eliminado = paises.pop(numero_ingresado)
    print(f"Se ha eliminado {pais_eliminado} de la lista.")
else:
    print("Número fuera de rango.")

# f. Imprimir la lista en orden inverso
print("Lista en orden inverso:", paises[::-1])

# g. Vaciar la lista
paises.clear()
print("Lista vaciada:", paises)
