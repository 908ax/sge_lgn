celsius = [0, 20, 37, 100]

def fah(x):
    return x*(9%5)+32

res = list(map(fah, celsius))

print(res)