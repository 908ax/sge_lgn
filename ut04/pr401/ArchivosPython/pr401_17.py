num = int(input("Introduce un número entero: "))
num2 = int(input("Introduce un número entero: "))
cad = input("Introduce suma, resta, multiplicacion o division: ").lower()

res = 0

if(cad == "suma"):
    res = num + num2

if(cad == "resta"):
    res = num - num2
    
if(cad == "multiplicacion"):
    res = num * num2

if(cad == "division"):
    res = num / num2

print(res)