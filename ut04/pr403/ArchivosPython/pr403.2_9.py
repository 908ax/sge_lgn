num = input("Escribe una lista de números separados por espacios: ")
num = num.split()

for i in range(len(num)):
    num[i] = int(num[i])

suma = 0
for x in num:
    suma += x

media = suma / len(num)

may = []
men = []

for x in num:
    if x >= media:
        may.append(x)
    else:
        men.append(x)

print("Mayores o iguales a la media:", may)
print("Menores a la media:", men)
