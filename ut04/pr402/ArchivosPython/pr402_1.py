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