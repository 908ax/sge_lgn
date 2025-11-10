lista1 = [1, 2]
lista2 = [3, 4]

res = []
for i in lista1:
    res += list(map(lambda x: (i, x), lista2))

print(res)