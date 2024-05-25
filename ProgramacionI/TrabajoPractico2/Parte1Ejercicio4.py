'''
Que dada la base y altura de un triángulo nos calcule su área
'''

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


area = calcular_area_triangulo(5, 10)
print(area)  # Debería imprimir 25.0
