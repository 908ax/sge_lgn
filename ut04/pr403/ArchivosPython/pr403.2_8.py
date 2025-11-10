num = input("Escribe la primera lista de números separados por espacios: ")
num2 = input("Escribe la segunda lista de números separados por espacios: ")

num = num.split()
num2 = num2.split()

for i in range(len(num)):
    num[i] = int(num[i])
for i in range(len(num2)):
    num2[i] = int(num2[i])

res = []

for x in num:
    if x in num2 and x not in res:
        res.append(x)

print("Comunes:", res)
