cant = float(input("Cantidad: "))
u1 = input("Unidad origen (mm, cm, m, km): ")
u2 = input("Unidad destino (mm, cm, m, km): ")

if u1 == "mm":
    valor = cant / 1000
    valor = valor / 100  # primero a m
    if u2 == "cm":
        res = cant / 10
    if u2 == "m":
        res = cant / 1000
    if u2 == "km":
        res = cant / 1000000
    if u2 == "mm":
        res = cant

if u1 == "cm":
    if u2 == "mm":
        res = cant * 10
    if u2 == "m":
        res = cant / 100
    if u2 == "km":
        res = cant / 100000
    if u2 == "cm":
        res = cant

if u1 == "m":
    if u2 == "mm":
        res = cant * 1000
    if u2 == "cm":
        res = cant * 100
    if u2 == "km":
        res = cant / 1000
    if u2 == "m":
        res = cant

if u1 == "km":
    if u2 == "mm":
        res = cant * 1000000
    if u2 == "cm":
        res = cant * 100000
    if u2 == "m":
        res = cant * 1000
    if u2 == "km":
        res = cant

print(cant, u1, "son", res, u2)