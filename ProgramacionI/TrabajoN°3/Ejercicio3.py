'''Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
debajo la misma lista pero sólo con las frutas que añadió el usuario.'''



frutas = ["banana", "manzana", "pera"]

# Lista para almacenar las frutas añadidas por el usuario
frutas_usuario = []

# Pedir al usuario que ingrese 3 frutas
for i in range(3):
    fruta = input(f"Ingrese la fruta {i+1}: ")
    frutas.append(fruta)
    frutas_usuario.append(fruta)

# Mostrar la lista completa
print("Lista completa de frutas:", frutas)

# Mostrar la lista con las frutas añadidas por el usuario
print("Frutas añadidas por el usuario:", frutas_usuario)
