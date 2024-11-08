lista = []
numeros = input("Ingresa números separados por espacio: ")
lista.extend(map(int, numeros.split()))
lista.sort()
print("Lista ordenada:", lista)
lista.reverse()
print("Lista invertida:", lista)
