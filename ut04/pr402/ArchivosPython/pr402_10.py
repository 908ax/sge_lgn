cad = input("Escribe una cadena")

res = ""
for c in cad:
    if c.isalnum() or c == ' ':
        res += c

print(res)