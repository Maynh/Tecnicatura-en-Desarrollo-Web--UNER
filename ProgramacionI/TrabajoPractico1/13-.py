'''
Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de
usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:
1985 -> Usuario: mfrancisconi, Contraseña: mf.1985
'''

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
anio_nacimiento = input("Ingrese su año de nacimiento: ")

usuario = (nombre[0] + apellido).lower()
contrasena = nombre[0].lower() + apellido[0].lower() + '.' + anio_nacimiento

print(f"Usuario sugerido: {usuario}")
print(f"Contraseña sugerida: {contrasena}")
