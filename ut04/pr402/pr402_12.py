cadena = input("Escribe una cadena: ")
count = 0
prev = ""
res = ""

for c in cadena:
    if prev == c:
        count += 1
    else:
        if prev:
            res = res + prev
            res = res + str(count)
        prev = c
        count = 1


res = res + prev
res = res + str(count)
print(res)