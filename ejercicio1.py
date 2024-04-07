# Leer tres números
numeros = []

for i in range(3):
    numero = float(input("Ingrese el número {}: ".format(i + 1)))
    numeros.append(numero)

# Ordenar los números ascendentemente
numeros_ordenados = sorted(numeros)

# Imprimir los números ordenados
print("Números ordenados ascendentemente:", numeros_ordenados)
