est = {
    "Ana": {"Matemáticas": 8.5, "Física": 9.0, "Programación": 7.8},
    "Carlos": {"Matemáticas": 9.2, "Física": 8.8, "Programación": 9.4},
    "Luis": {"Matemáticas": 7.6, "Física": 8.0, "Programación": 8.5},
    "María": {"Matemáticas": 9.5, "Física": 10.0, "Programación": 9.8},
    "Jorge": {"Matemáticas": 8.8, "Física": 8.4, "Programación": 7.9},
    "Sofía": {"Matemáticas": 9.1, "Física": 8.9, "Programación": 9.3}
}

prom_est = {}
prom_mat = {}

asigs = []
for i in est:
    for j in est[i]:
        if j not in asigs:
            asigs.append(j)

for i in est:
    suma = 0
    cont = 0
    for j in est[i]:
        suma += est[i][j]
        cont += 1
    prom_est[i] = suma / cont

for i in asigs:
    suma = 0
    cont = 0
    for j in est:
        suma += est[j][i]
        cont += 1
    prom_mat[i] = suma / cont

print("Promedio por estudiante:", prom_est)
print("Promedio por asignatura:", prom_mat)
