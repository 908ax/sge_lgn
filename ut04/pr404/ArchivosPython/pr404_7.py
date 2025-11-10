emple = {"Ana": 1200, 
         "Luis": 900, 
         "Marta": 1500, 
         "Juan": 800
        }
umbral = int(input("Ingresa el salario mínimo: "))

res = {}

for i in emple:
    if emple[i] > umbral:
        res[i] = emple[i]

print("Empleados con salario mayor a", umbral, ":", res)