def main():
    pila = []

    while True:
        respuesta = input("¿Agregar URL? (si/no): ").strip().lower()

        if respuesta == "si":
            url = input("Ingresa la URL: ").strip()
            pila.append(url)
        elif respuesta == "no":
            if pila:
                pila.pop()
        else:
            print("Respuesta no válida.")

        print("Historial:", pila)

if __name__ == "__main__":
    main()
