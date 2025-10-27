# [UT04](./index.md)
# PR0402

## Ejercicio 1
```
cad = input("Escribe una cadena string").lower()
voc = ["a","e","i","o","u"]
car = list(cad)
numVoc = 0
numCon = 0

for letra in car:

    if letra in (voc):
        numVoc+=1
    else:
        numCon+=1
    

print(numCon)
print(numVoc)
```


## Ejercicio 2

```
cad = input("Escribe una cadena: ")
car = list(cad)
inv = ""

for car in cad:
    inv = car + inv

print("Cadena invertida:", inv)

```

## Ejercicio 3

```
cad = input("Escribe una cadena: ")

tex = cad.lower().replace(" ", "")

inv = ""
for car in tex:
    inv = car + inv

if tex == inv:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

```

## Ejercicio 4

```
cad = input("Escribe una cadena: ")

palabras = cad.split()
cantidad = len(palabras)

print("La cadena tiene", cantidad, "palabras")
```

## Ejercicio 5

```
cad = input("Escribe una cadena: ")

nueva_cad = ""
for c in cad:
    if c not in nueva_cad:
        nueva_cad += c

print("Cadena sin caracteres repetidos:", nueva_cad)
```

## Ejercicio 6

```
cad = input("Escribe una cadena: ")

nueva_cad = ""
for c in cad:
    if c.islower():
        nueva_cad += c.upper()
    elif c.isupper():
        nueva_cad += c.lower()
    else:
        nueva_cad += c

print("Cadena con mayúsculas y minúsculas invertidas:", nueva_cad)
```

## Ejercicio 7

```
cad = input("Escribe una cadena: ")
n = int(input("¿Cuántas veces quieres rotarla hacia la izquierda? "))

n = n % len(cad)
nueva_cad = cad[n:] + cad[:n]

print("Cadena rotada:", nueva_cad)
```

## Ejercicio 8

```
cad1 = input("Escribe una cadena: ")
cad2 = input("Escribe otra cadena: ")
anagrame = True 
if len(cad1) == len (cad2):
    for c in cad1:
        anagrama = False
    for c in cad2:
        anagrama = False
else:
    anagrama = False
print("Es anagrama" if anagrama else "No es un anagrama")
```

## Ejercicio 10

```
cad = input("Escribe una cadena")

res = ""
for c in cad:
    if c.isalnum() or c == ' ':
        res += c

print(res)
```

## Ejercicio 11

```
cad = input("Escribe una cadena: ").title().replace(" ", "").replace("-", "")

cad = cad[0].lower() + cad[1:]

print(cad)
```

## Ejercicio 12

```
cadena = input("Escribe una cadena: ")
count = 0
prev = ""
res = ""

for c in cadena:
    if prev == c:
        count += 1
    else:
        if prev:
            res = res + prev
            res = res + str(count)
        prev = c
        count = 1


res = res + prev
res = res + str(count)
print(res)
```

## Ejercicio 16

```
cadena = input("Introduce una cadena: ")

palabras = cadena.split()

if not palabras:
    longitud = 0
else:
    longitud = max(len(palabra) for palabra in palabras)

print("La longitud de la palabra más larga es:", longitud)
```