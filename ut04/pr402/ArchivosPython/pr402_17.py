cad = input("Escribe un número: ")

res = ""
cont = 0

for i in range(len(cad) - 1, -1, -1):
    res = cad[i] + res
    cont = cont + 1
    if cont == 3 and i != 0:
        res = "." + res
        cont = 0

print(res)
