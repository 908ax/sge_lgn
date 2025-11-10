num = input("Escribe una lista de números separados por espacios: ")
num = num.split()

for i in range(len(num)):
    num[i] = int(num[i])

pares = []

for n in num:
    if n % 2 == 0:
        pares.append(n)

print("Números pares:", pares)
