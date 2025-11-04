n = int(input("Cuántos números de Fibonacci quieres: "))

a = 1
b = 1
rep = 1

while rep <= n:
    print(a)
    c = a + b
    a = b
    b = c
    rep += 1