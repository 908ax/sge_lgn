n = int(input("Número asteriscos (impar): "))

while n % 2 == 0:
    n = int(input("Debe ser impar. Número asteriscos: "))

ast = "*"
rep = 1
esp = ""

while rep <= n:
    esp = " " * ((n - rep) // 2)
    print(esp + ast)
    ast = "*" + ast + "*"
    rep += 2