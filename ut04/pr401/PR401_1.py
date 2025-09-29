num = int(input("Acierta el número: "))

while (num != 1):

    print("Has fallado, vuelve ha intentarlo")
    num = int(input("Acierta el número: "))

print("Acertaste")

# Correccion 

while ( not input ("Dime un número: ").isdigit ):
    pass
print("Numero valido")