'''
Programe una aplicación de consola que pregunte el precio total de la cuenta, luego
pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el
número de comensales y mostrar cuánto debe pagar cada persona
'''
precio_total = float(input("Ingrese el precio total de la cuenta: "))
comensales = int(input("Ingrese la cantidad de comensales: "))

monto_por_persona = precio_total / comensales

print("Cada persona debe pagar: $", monto_por_persona)
