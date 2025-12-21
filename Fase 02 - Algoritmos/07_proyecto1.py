#Sistema de Gestión Académica (SGA)
diccionario_estudiantes = [
    {"nombre": "Ana Pérez", "apellido": "Gómez", "notas": [15, 18, 20]},
    {"nombre": "Luis Martínez", "apellido": "Rodríguez", "notas": [12, 14, 16]},
    {"nombre": "María López", "apellido": "Hernández", "notas": [19, 20, 18]},
]

def registar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    estudiante = {"nombre": nombre, "apellido": apellido, "notas": notas}
    diccionario_estudiantes.append(estudiante)
    print("Estudiante registrado exitosamente.")

def calificar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a calificar: ")
    for estudiante in diccionario_estudiantes:
        if estudiante["nombre"] == nombre:
            notas = []
            for i in range(3):
                nota = float(input(f"Ingrese la nota {i+1}: "))
                notas.append(nota)
            estudiante["notas"] = notas
            print("Notas actualizadas exitosamente.")
            return
    print("Estudiante no encontrado.")

def mostrar_promedios():
    print("Promedios de los estudiantes:")
    for estudiante in diccionario_estudiantes:
        promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
        print(f"{estudiante['nombre']} {estudiante['apellido']}: {promedio:.2f}")

def mostrar_estudiantes():
    print("Lista de estudiantes:")
    for estudiante in diccionario_estudiantes:
        print(f"{estudiante['nombre']} {estudiante['apellido']} - Notas: {estudiante['notas']}")

def main():
    while True:
        print("\n--- Sistema de Gestión Académica ---")
        print("1. Registrar Estudiante")
        print("2. Calificar Estudiante")
        print("3. Mostrar Promedios")
        print("4. Mostrar Estudiantes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registar_estudiante()
        elif opcion == "2":
            calificar_estudiante()
        elif opcion == "3":
            mostrar_promedios()
        elif opcion == "4":
            mostrar_estudiantes()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()#Sistema de Gestión Académica (SGA)