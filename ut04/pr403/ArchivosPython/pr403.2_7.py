num = input("Escribe la primera lista de números separados por espacios: ")
num2 = input("Escribe la segunda lista de números separados por espacios: ")

num = num.split()
num2 = num2.split()

for i in range(len(num)):
    num[i] = int(num[i])
for i in range(len(num2)):
    num2[i] = int(num2[i])

res = []
l = min(len(num), len(num2))

for i in range(l):
    res.append(num[i])
    res.append(num2[i])

for i in range(l, len(num)):
    res.append(num[i])
for i in range(l, len(num2)):
    res.append(num2[i])

print("Intercalada:", res)