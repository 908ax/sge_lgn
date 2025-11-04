lista = [[1, 2, 3, 4],
         [9, 5, 2, 5],
         [6, 2, 5, 5]]

sumaFilas = []
for fila in lista:
    suma = 0
    for num in fila:
        suma += num
    sumaFilas.append(suma)

sumaColumnas = lista[0]
for fila in lista[1:]:
    for i in range(0, len(fila)):
        sumaColumnas[1] += fila[i]

print(sumaFilas)
print(sumaColumnas)