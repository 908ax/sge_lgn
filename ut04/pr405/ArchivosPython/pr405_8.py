lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

comunes = list(filter(lambda i: i in lista2, lista1))

print(comunes)