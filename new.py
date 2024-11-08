nombre = input("Escribe el nombre del estudiante: ")
edad = input("Dame la edad del estudiante: ")
codigo = input("Código de estudiante: ")
origen = input("¿De dónde es el estudiante? ")
correo = input("Correo electrónico del estudiante: ")
#diccionario
estudiante = {
    "Nombre": nombre,
    "Edad": edad,
    "Código": codigo,
    "Origen": origen,
    "Correo": correo
}
print("\nInformación del estudiante:")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
