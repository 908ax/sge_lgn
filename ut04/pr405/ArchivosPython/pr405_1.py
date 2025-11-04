numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = []
numero = 0
def pares(x):
    for i in range(len(numeros)):
        return x%2 == 0

res = list(filter(pares, numeros)) 
print(res)