#El Diario Persistente (Sistema I/O)

def añadir_entrada():
    with open("diario.txt", "a") as archivo:
        entrada = input("Escribe tu entrada para el diario: ")
        archivo.write(entrada + "\n")

def leer_diario():
    with open("diario.txt", "r") as archivo:
        print("\nContenido del diario:")
        contenido = archivo.read()
        print(contenido)

def buscar_entrada(palabra_clave):
    with open("diario.txt", "r") as archivo:
        entradas = archivo.readlines()
        resultados = [entrada for entrada in entradas if palabra_clave in entrada]
        return resultados

def borrar_diario():
    with open("diario.txt", "w") as archivo:
        archivo.write("")

while True:
    print("\n--- Diario Persistente ---")
    print("1. Añadir entrada")
    print("2. Leer diario")
    print("3. Buscar entrada")
    print("4. Borrar diario")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        añadir_entrada()
    elif opcion == "2":
        leer_diario()
    elif opcion == "3":
        palabra = input("Ingresa la palabra clave para buscar: ")
        resultados = buscar_entrada(palabra)
        if resultados:
            print("Entradas encontradas:")
            for res in resultados:
                print(res.strip())
        else:
            print("No se encontraron entradas con esa palabra clave.")
    elif opcion == "4":
        borrar_diario()
        print("Diario borrado.")
    elif opcion == "5":
        print("Saliendo del diario.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
