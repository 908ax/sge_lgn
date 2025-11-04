asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

print("1.-Listar estudiantes matriculados: ")
print("2.-Matricular un estudiante en una asignatura: ")
print("3.-Dar de baja un estudiante de una asignatura: ")

eleccion = int(input("Escoge escribiendo un numero: "))

count = 0

if eleccion==1:
    eleccion2 = input("Escoge una asignatura: ")
    count += len(asignaturas[eleccion2])
    print("En total hay ", count, " alumnos matriculados en ", eleccion2)

if eleccion==2:
    alumno = input("Nombre del alumno: ")
    eleccion3 = input("Escoge una asignatura: ")
    asignaturas[eleccion3].append(alumno)
    print("El alumno ", alumno, " se ha matriculado en ", eleccion3)

if eleccion==3:
    alumno2 = input("Nombre del alumno: ")
    eleccion4 = input("Escoge una asignatura: ")
    asignaturas[eleccion4].remove(alumno2)
    print("El alumno ", alumno2, " se ha dado de baja en ", eleccion4)