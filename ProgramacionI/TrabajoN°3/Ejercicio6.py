'''Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
de una lista vacía:
a. Agregar un elemento al final.
b. Agregar un elemento al principio.
c. Quitar un elemento al final.
d. Quitar un elemento al principio.'''


def mostrar_menu():
    print("\nMenu:")
    print("a. Agregar un elemento al final.")
    print("b. Agregar un elemento al principio.")
    print("c. Quitar un elemento al final.")
    print("d. Quitar un elemento al principio.")
    print("e. Salir.")


def main():
    lista = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").lower()

        if opcion == 'a':
            elemento = input("Ingrese el elemento a agregar al final: ")
            lista.append(elemento)
            print(f"Lista actualizada: {lista}")

        elif opcion == 'b':
            elemento = input("Ingrese el elemento a agregar al principio: ")
            lista.insert(0, elemento)
            print(f"Lista actualizada: {lista}")

        elif opcion == 'c':
            if lista:
                elemento = lista.pop()
                print(f"Elemento '{elemento}' quitado del final.")
            else:
                print("La lista está vacía. No hay elementos para quitar.")
            print(f"Lista actualizada: {lista}")

        elif opcion == 'd':
            if lista:
                elemento = lista.pop(0)
                print(f"Elemento '{elemento}' quitado del principio.")
            else:
                print("La lista está vacía. No hay elementos para quitar.")
            print(f"Lista actualizada: {lista}")

        elif opcion == 'e':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")


if __name__ == "__main__":
    main()
a