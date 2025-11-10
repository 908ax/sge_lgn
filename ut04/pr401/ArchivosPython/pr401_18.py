num = int(input("Introduce un número entero: "))
ori = input("Introduce grados Celsius, Fahrenheit y Kelvin: ").lower()
des = input("Introduce grados Celsius, Fahrenheit y Kelvin: ").lower()

res = 0

if ori == "celsius":
    if des == "fahrenheit":
        res = (num * 9/5) + 32
    if des == "kelvin":
        res = num + 273.15
    print(res)

elif ori == "fahrenheit":
    if des == "celsius":
        res = (num - 32) * 5/9
    if des == "kelvin":
        res = (num - 32) * 5/9 + 273.15
    print(res)

elif ori == "kelvin":
    if des == "celsius":
        res = num - 273.15
    if des == "fahrenheit":
        res = (num - 273.15) * 9/5 + 32
    print(res)

else:
    print("Error 1. No se reconoce la cadena")

