lista = []
numeros = input("Ingresa números separados por espacio: ")
lista.extend(map(int, numeros.split()))
N = input("ingresa un numero: ")
veces = numeros.count(N)
print("El numero",N,"aparece unas",veces,"en la lista")
numeros_eliminados = list(set(numeros))
print(numeros_eliminados)