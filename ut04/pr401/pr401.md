# [UT04](./index.md)
# PR0401

## Ejercicio 1
```
python
num = int(input("Acierta el número: "))

while (num != 1):

    print("Has fallado, vuelve ha intentarlo")
    num = int(input("Acierta el número: "))

print("Acertaste")
```


## Ejercicio 2

```
n = int(input("Número que se multiplica: "))
k = int(input("Número de veces que se multiplica: "))
rep = 1

while (rep <= k):
    res=n*rep
    print(n,"*",rep,"=",res)
    rep+=1

#Correccion

n = int(input("Valor n: "))
k = int(input("Valor k: "))
for iter in range(1, k+1):
    print(n+"+"+iter+"="+n*iter)

```

## Ejercicio 3

```
n = int(input("Número de filas: "))
rep = 1
ast=""

while (rep <= n):
    ast+="*"
    print(ast)
    rep+=1

```

## Ejercicio 4

```
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
```

## Ejercicio 5

```
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
n4 = int(input("Número 4: "))
n5 = int(input("Número 5: "))

mayor = n1
menor = n1

if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
if n4 > mayor:
    mayor = n4
if n5 > mayor:
    mayor = n5

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
if n5 < menor:
    menor = n5

print("El número mayor es", mayor, "y el menor es", menor)
```

## Ejercicio 6

```
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
```

## Ejercicio 7

```
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
```

## Ejercicio 8

```
j1 = input("Di la elección del jugador 1: ").lower()
j2 = input("Di la elección del jugador 2: ").lower()
match j1:
    case "piedra":
        res = ("Gana jugador 1" if j2 in ['lagarto', 'tijeras' ] else
        "Gana jugador 2" if j2 in ['papel', 'spock'] else
        "Empate")
    
    case "papel":
        res = ("Gana jugador 1" if j2 in ['piedra', 'spock' ] else
        "Gana jugador 2" if j2 in ['tijera', 'lagarto'] else
        "Empate")
    case "tijera":
        res = ("Gana jugador 1" if j2 in ['papel', 'lagarto' ] else
        "Gana jugador 2" if j2 in ['piedra', 'spock'] else
        "Empate")
    case "lagarto":
        res = ("Gana jugador 1" if j2 in ['spock', 'papel' ] else
        "Gana jugador 2" if j2 in ['piedra', 'tijera'] else
        "Empate")
    case "spock":
        res = ("Gana jugador 1" if j2 in ['tijera', 'piedra' ] else
        "Gana jugador 2" if j2 in ['papel', 'lagarto'] else
        "Empate")
    case _:
        res = "Elección no válida"
print(res)
```

## Ejercicio 9

```
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
```

## Ejercicio 10

```
num = int(input("Introduce un número: "))

if num < 2:
    print(num, "no es primo")
else:
    primo = True
    i = 2
    while i <= num // 2:
        if num % i == 0:
            primo = False
        i += 1
    if primo:
        print(num, "es primo")
    else:
        print(num, "no es primo")
```

## Ejercicio 19

```
from random import *

lon = input("Dime la longitud de la contraseña")
chars = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789-.,;:;_"
password = ""

for i in range(lon):
    password = password + chars[ randint(0, len(chars)-1)]

print(password)
```