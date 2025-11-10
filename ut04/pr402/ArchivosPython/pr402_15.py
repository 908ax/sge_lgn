cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")

valor1 = 0
for c in cadena1:
    valor1 = valor1 + ord(c)

valor2 = 0
for c in cadena2:
    valor2 = valor2 + ord(c)

if valor1 > valor2:
    print("La primera cadena tiene un valor ASCII total mayor " + str(valor1))
elif valor2 > valor1:
    print("La segunda cadena tiene un valor ASCII total mayor " + str(valor2))
else:
    print("Ambas cadenas tienen el mismo valor ASCII total " + str(valor1))
