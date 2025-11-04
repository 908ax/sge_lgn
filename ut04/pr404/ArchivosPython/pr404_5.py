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