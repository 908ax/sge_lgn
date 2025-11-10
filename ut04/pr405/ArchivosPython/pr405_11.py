alumnos = [("Ana", 4), ("Bruno", 7), ("Clara", 5), ("David", 8)]

aprobados = list(map(lambda i: i[0], filter(lambda i: i[1] >= 5, alumnos)))

print(aprobados)