'''Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
usuario:
a. Agregar nuevas tareas pendientes.
b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
de la lista de pendientes a la de terminadas.'''


def mostrar_menu():
    print("\nMenu:")
    print("a. Agregar una nueva tarea pendiente.")
    print("b. Marcar una tarea pendiente como terminada.")
    print("c. Mostrar tareas pendientes.")
    print("d. Mostrar tareas terminadas.")
    print("e. Salir.")


def main():
    pendientes = []
    terminadas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").lower()

        if opcion == 'a':
            tarea = input("Ingrese la nueva tarea pendiente: ")
            pendientes.append(tarea)
            print(f"Tarea '{tarea}' agregada a pendientes.")

        elif opcion == 'b':
            if pendientes:
                print("Tareas pendientes:")
                for idx, tarea in enumerate(pendientes, 1):
                    print(f"{idx}. {tarea}")
                tarea_num = int(input("Ingrese el número de la tarea que ha terminado: "))
                if 1 <= tarea_num <= len(pendientes):
                    tarea_terminada = pendientes.pop(tarea_num - 1)
                    terminadas.append(tarea_terminada)
                    print(f"Tarea '{tarea_terminada}' marcada como terminada.")
                else:
                    print("Número de tarea no válido.")
            else:
                print("No hay tareas pendientes.")

        elif opcion == 'c':
            print("Tareas pendientes:")
            if pendientes:
                for tarea in pendientes:
                    print(f"- {tarea}")
            else:
                print("No hay tareas pendientes.")

        elif opcion == 'd':
            print("Tareas terminadas:")
            if terminadas:
                for tarea in terminadas:
                    print(f"- {tarea}")
            else:
                print("No hay tareas terminadas.")

        elif opcion == 'e':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")


if __name__ == "__main__":
    main()
