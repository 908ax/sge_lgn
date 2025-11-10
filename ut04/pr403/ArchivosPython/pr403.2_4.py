numeros = input("Escribe una lista de números separados por espacios: ")
numeros = numeros.split()

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

mayor = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

print("Valor máximo:", mayor)
print("Valor mínimo:", menor)
