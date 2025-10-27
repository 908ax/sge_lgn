cad = input("Escribe una cadena: ")

tex = cad.lower().replace(" ", "")

inv = ""
for car in tex:
    inv = car + inv

if tex == inv:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")