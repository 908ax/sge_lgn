cad = input("Introduce una cadena de texto: ")

inv = ""
ind = len(cad) - 1

while ind >= 0:
    inv = inv + cad[ind]
    ind -= 1

print(inv)