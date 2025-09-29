from random import *

num = randint(0,100)
acertado = False

while acertado == False:
    intento = int(input("Adivina el número (0-100): "))
    if intento == num:
        print("¡Correcto! El número era", num)
        acertado = True
    else:
        if intento < num:
            print("El número es más alto")
        else:
            print("El número es más bajo")