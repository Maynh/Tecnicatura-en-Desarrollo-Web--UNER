'''
Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Sise invoca
la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
'''

def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total

total1 = calcular_total_factura(100)  # Aplicando el IVA por defecto del 21%
total2 = calcular_total_factura(100, 10)  # Aplicando un IVA del 10%

print(total1)
print(total2) 
