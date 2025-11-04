# [UT04](./index.md)
# PR0404

## Ejercicio 1
```
frutas = {
    "manzana": ["1.25"],
    "limon": ["2.00"],
    "fresa": ["0.50"],
    "platano": ["1.75"],
}

fruta = input("Ingresa el nombre de una fruta: ").lower()

if fruta in frutas:
    print("El precio de la", fruta, "es de", frutas[fruta], "€")
else:
    print("Lo sentimos, la fruta", fruta, "no está disponible.")

```

## Ejercicio 2
```
productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

count = 0
countCat = 0

for categ in productos:
    print(categ, " tiene ", len(productos[categ]), " productos")
    count+=len(productos[categ])
    countCat+=1

print("Hay un total de ", countCat, " categorias")
print("En total hay ", count, "productos")
```

## Ejercicio 3
```
frase = input("Ingresa una frase: ").lower()

palabras = frase.lower().split()

frec = {}

for palabra in palabras:
    if palabra in frec:
        frec[palabra] += 1
    else:
        frec[palabra] = 1

print("La frecuencia de las palabras: ")

for palabra, count in frec.items():
    print(palabra, ": ", count)
```

## Ejercicio 4
```
asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

print("1.-Listar estudiantes matriculados: ")
print("2.-Matricular un estudiante en una asignatura: ")
print("3.-Dar de baja un estudiante de una asignatura: ")

eleccion = int(input("Escoge escribiendo un numero: "))

count = 0

if eleccion==1:
    eleccion2 = input("Escoge una asignatura: ")
    count += len(asignaturas[eleccion2])
    print("En total hay ", count, " alumnos matriculados en ", eleccion2)

if eleccion==2:
    alumno = input("Nombre del alumno: ")
    eleccion3 = input("Escoge una asignatura: ")
    asignaturas[eleccion3].append(alumno)
    print("El alumno ", alumno, " se ha matriculado en ", eleccion3)

if eleccion==3:
    alumno2 = input("Nombre del alumno: ")
    eleccion4 = input("Escoge una asignatura: ")
    asignaturas[eleccion4].remove(alumno2)
    print("El alumno ", alumno2, " se ha dado de baja en ", eleccion4)
```
## Ejercicio 5
```
asignaturas = {
    "Matemáticas": ["Ana", "Marcos"],
    "Física": ["Elena"],
    "Programación": ["Oscar"],
    "Historia": ["María"],
    "Inglés": ["Carlos"],
}

def invDic(dic):
    invertido = {}
    for asignatura, alumnos in dic.items():
        for alumno in alumnos:
            invertido[alumno] = asignatura
    return invertido

inv = invDic(asignaturas)
print(inv)
```
## Ejercicio 6
```
prod1 = {
    "Pan": 1.5,
    "Leche": 2.0,
    "Huevos": 3.5
}

prod2 = {
    "Leche": 1.8,
    "Arroz": 2.5,
    "Huevos": 3.0
}

def combDic(dic1, dic2):
    combinado = dic1.copy()
    for producto, precio in dic2.items():
        if producto in combinado:
            combinado[producto] += precio
        else:
            combinado[producto] = precio
    return combinado

comb = combDic(prod1, prod2)
print(comb)
```