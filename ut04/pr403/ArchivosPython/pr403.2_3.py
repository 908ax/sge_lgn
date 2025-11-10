num = input("Escribe una lista de números separados por espacios: ")

num = num.split()
list = []

for n in num:
    if n not in list:
        list.append(n)

print("Lista sin duplicados:", list)
