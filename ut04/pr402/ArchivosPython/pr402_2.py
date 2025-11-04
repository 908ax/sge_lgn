cad = input("Escribe una cadena: ")
car = list(cad)
inv = ""

for car in cad:
    inv = car + inv

print("Cadena invertida:", inv)