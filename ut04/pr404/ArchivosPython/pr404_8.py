departamentos = {
    "Recursos Humanos": {
        "Ana": "Gerente de Recursos Humanos",
        "Luis": "Especialista en Reclutamiento",
        "Elena": "Asistente de Recursos Humanos"
    },
    "Tecnología": {
        "Carlos": "Desarrollador Backend",
        "María": "Desarrolladora Frontend",
        "Pedro": "Administrador de Sistemas"
    },
    "Marketing": {
        "Sofía": "Directora de Marketing",
        "Jorge": "Especialista en SEO",
        "Laura": "Community Manager"
    },
    "Finanzas": {
        "Juan": "Analista Financiero",
        "Lucía": "Contadora",
        "Raúl": "Asesor Financiero"
    }
}

while True:
    print("\nOpciones:")
    print("1. Mostrar empleados de un departamento")
    print("2. Añadir empleado")
    print("3. Eliminar empleado")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        dept = input("Escribe el nombre del departamento: ")
        if dept in departamentos:
            print("Empleados en", dept, ":")
            for i in departamentos[dept]:
                print(i, "-", departamentos[dept][i])
        else:
            print("Departamento no encontrado.")

    elif opcion == "2":
        dept = input("Escribe el nombre del departamento: ")
        if dept in departamentos:
            nombre = input("Nombre del empleado: ")
            puesto = input("Puesto del empleado: ")
            departamentos[dept][nombre] = puesto
            print(nombre, "añadido a", dept)
        else:
            print("Departamento no encontrado.")

    elif opcion == "3":
        dept = input("Escribe el nombre del departamento: ")
        if dept in departamentos:
            nombre = input("Nombre del empleado a eliminar: ")
            if nombre in departamentos[dept]:
                del departamentos[dept][nombre]
                print(nombre, "eliminado de", dept)
            else:
                print("Empleado no encontrado en", dept)
        else:
            print("Departamento no encontrado.")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")
