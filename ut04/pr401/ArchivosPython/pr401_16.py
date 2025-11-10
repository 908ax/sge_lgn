num = input("Introduce un número entero: ")

suma = 0
ind = 0

while ind < len(num):
    suma = suma + int(num[ind])
    ind += 1

print(suma)