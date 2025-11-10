cad = input("Escribe una cadena codificada (ej. A3B2C4): ")

res = ""
count = 0
num = 0

for i in range(0, len(cad), 2):
    letra = cad[i]
    num = int(cad[i + 1])
    rep = 0
    while rep != num:
        res += letra
        rep += 1

print(res)
