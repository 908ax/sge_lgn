from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]

pares = filter(lambda num: num % 2 == 0, numeros)
pares = map(lambda x: x, pares)

def multiplica(acum, num):
    return acum * num

res = reduce(multiplica, pares, 1)

print(res)