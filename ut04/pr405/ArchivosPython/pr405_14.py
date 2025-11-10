palabras = ["HOLA", "MUNDO", "SOL", "CIELO", "mar"]

res = list(map(lambda i: i[0].lower() + i[1:], filter(lambda i: len(i) > 3 and i.isupper(), palabras)))

print(res)