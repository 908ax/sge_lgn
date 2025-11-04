numeros = [1, 2, 3, 4, 5]


def suma(x):
    x+=(x-1)

res = filter(suma, numeros)
print(res)
