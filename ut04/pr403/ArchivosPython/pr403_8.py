nombres = ["Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"]

nombresMin = [nombre.lower() for nombre in nombres]

vocalA = 0
letraB = 0
letraC = 0
letraD = 0
vocalE = 0
letraF = 0
letraG = 0
letraH = 0
vocalI = 0
letraJ = 0
letraK = 0
letraL = 0
letraM = 0
letraN = 0
letraÑ = 0
vocalO = 0
letraP = 0
letraQ = 0
letraR = 0
letraS = 0
letraT = 0
vocalU = 0
letraV = 0
letraW = 0
letraX = 0
letraY = 0
letraZ = 0

for nombre in nombres:
    for i in nombre:
        if i == "a" or i == "á":
            vocalA += 1
        if i == "b":
            letraB += 1
        if i == "c":
            letraC += 1
        if i == "d":
            letraD += 1
        if i == "e" or i == "é":
            vocalE += 1
        if i == "f":
            letraF += 1
        if i == "g":
            letraG += 1
        if i == "h":
            letraH += 1
        if i == "i" or i == "í":
            vocalI += 1
        if i == "j":
            letraJ += 1
        if i == "k":
            letraK += 1
        if i == "l":
            letraL += 1
        if i == "m":
            letraM += 1
        if i == "n":
            letraN += 1
        if i == "ñ":
            letraÑ += 1
        if i == "o" or i == "ó":
            vocalO += 1
        if i == "p":
            letraP += 1
        if i == "q":
            letraQ += 1
        if i == "r":
            letraR += 1
        if i == "s":
            letraS += 1
        if i == "t":
            letraT += 1
        if i == "u" or i == "ú":
            vocalU += 1
        if i == "v":
            letraV += 1
        if i == "w":
            letraW += 1
        if i == "x":
            letraX += 1
        if i == "y":
            letraY += 1
        if i == "z":
            letraZ += 1

print("El numero a que hay en los nombres es: ")
print(vocalA)
print("El numero b que hay en los nombres es: ")
print(letraB)
print("El numero c que hay en los nombres es: ")
print(letraC)
print("El numero d que hay en los nombres es: ")
print(letraD)
print("El numero e que hay en los nombres es: ")
print(vocalE)
print("El numero f que hay en los nombres es: ")
print(letraF)
print("El numero g que hay en los nombres es: ")
print(letraG)
print("El numero h que hay en los nombres es: ")
print(letraH)
print("El numero i que hay en los nombres es: ")
print(vocalI)
print("El numero j que hay en los nombres es: ")
print(letraJ)
print("El numero k que hay en los nombres es: ")
print(letraK)
print("El numero l que hay en los nombres es: ")
print(letraL)
print("El numero m que hay en los nombres es: ")
print(letraM)
print("El numero n que hay en los nombres es: ")
print(letraN)
print("El numero ñ que hay en los nombres es: ")
print(letraÑ)
print("El numero o que hay en los nombres es: ")
print(vocalO)
print("El numero p que hay en los nombres es: ")
print(letraP)
print("El numero q que hay en los nombres es: ")
print(letraQ)
print("El numero r que hay en los nombres es: ")
print(letraR)
print("El numero s que hay en los nombres es: ")
print(letraS)
print("El numero t que hay en los nombres es: ")
print(letraT)
print("El numero u que hay en los nombres es: ")
print(vocalU)
print("El numero v que hay en los nombres es: ")
print(letraV)
print("El numero w que hay en los nombres es: ")
print(letraW)
print("El numero x que hay en los nombres es: ")
print(letraX)
print("El numero y que hay en los nombres es: ")
print(letraY)
print("El numero z que hay en los nombres es: ")
print(letraZ)
