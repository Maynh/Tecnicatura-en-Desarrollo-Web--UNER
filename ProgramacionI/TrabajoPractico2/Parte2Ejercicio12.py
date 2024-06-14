'''Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
ingresado no es ninguno de esos, imprimir otro mensaje'''



# Solicitar al usuario que ingrese un día de la semana
dia = input("Por favor, ingresa un día de la semana: ").strip().lower()

# Verificar el día ingresado y mostrar el mensaje correspondiente
if dia == "lunes":
    print("¡Es lunes! Una nueva semana comienza.")
elif dia == "viernes":
    print("¡Es viernes! El fin de semana está cerca.")
elif dia == "sábado" or dia == "sabado" or dia == "domingo":
    print("¡Es fin de semana! Disfruta tu día.")
else:
    print("Es un día entre semana. ¡Sigue adelante!")
