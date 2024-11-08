lista = []

while True:
    print("\nMenú de opciones:")
    print("1. Ver elementos")
    print("2. Agregar elemento")
    print("3. Modificar elemento")
    print("4. Eliminar elemento")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Elementos en la lista:", lista)
        
    elif opcion == "2":
        while True:
            print("Elementos en la lista:", lista)
            elemento = input("Inserta el elemento que deseas agregar: ")
            lista.append(elemento)
            print("Nuevo arreglo con el elemento agregado:", lista)
            continuar = input("¿Deseas agregar otro elemento? (s/n): ")
            if continuar.lower() != 's':
             break
                
    elif opcion == "3":
        print("Elementos en la lista:", lista)
        index = int(input("Elige el índice del elemento que deseas modificar: "))
        if 0 <= index < len(lista):
            nuevo_valor = input("Inserta el nuevo valor: ")
            lista[index] = nuevo_valor
            print("Lista modificada:", lista)
        else:
            print("Índice inválido.")
            
    elif opcion == "4":
        print("Elementos en la lista:", lista)
        index = int(input("Elige el índice del elemento que deseas eliminar: "))
        if 0 <= index < len(lista):
            lista.pop(index)
            print("Lista después de eliminar el elemento:", lista)
        else:
            print("Índice inválido.")
            
    elif opcion == "5":
        print("Saliendo...")
        break
        
    else:
        print("Opción no válida, intenta de nuevo.")
        print("Opcion no valida,ingresa un numero valido por favor.")
        