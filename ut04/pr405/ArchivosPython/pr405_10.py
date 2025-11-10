from functools import reduce

lista1 = ['a', 'b', 'c']
lista2 = ['x', 'y', 'z']

listas = [lista1] + [[i] for i in lista2]

def unir(a, b):
    for i in b:
        a.append(i)
    return a

resultado = reduce(unir, listas)

print(resultado)
