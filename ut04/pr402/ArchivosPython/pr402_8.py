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