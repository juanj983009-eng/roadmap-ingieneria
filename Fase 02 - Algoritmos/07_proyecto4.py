#La Enciclopedia Jujutsu (Deck Builder)
hechiceros = [
    {"nombre": "Yuji Itadori", "tipo": "Cuerpo a Cuerpo", "poder": 9100},
    {"nombre": "Megumi Fushiguro", "tipo": "Técnico", "poder": 7000},
    {"nombre": "Nobara Kugisaki", "tipo": "Rango Medio", "poder": 5000},
    {"nombre": "Satoru Gojo", "tipo": "Apoyo", "poder": 9999},
    {"nombre": "Maki Zenin", "tipo": "Cuerpo a Cuerpo", "poder": 9500},
    {"nombre": "Toge Inumaki", "tipo": "Apoyo", "poder": 6000},
    {"nombre": "Panda", "tipo": "Cuerpo a Cuerpo", "poder": 8500},
]

def agregar_hechicero(nombre, tipo, poder):
    nuevo_hechicero = {"nombre": nombre, "tipo": tipo, "poder": poder}
    hechiceros.append(nuevo_hechicero)

def mostrar_hechiceros():
    for hechicero in hechiceros:
        print(f"Nombre: {hechicero['nombre']}, Tipo: {hechicero['tipo']}, Poder: {hechicero['poder']}")

def borrar_hechicero(nombre):
    global hechiceros
    hechiceros = [h for h in hechiceros if h['nombre'] != nombre]


def ordenar_hechiceros_por_poder():
    return sorted(hechiceros, key=lambda x: x['poder'], reverse=True)

def hechiceros_grado_especial():
    return [h for h in hechiceros if h['poder'] >= 9000]

def ordenar_hechiceros_burbuja():
    # Trabajamos sobre la lista global o una copia
    n = len(hechiceros)

    # Bucle 1: Las pasadas
    for i in range(n):
        # Bucle 2: Comparación de parejas
        for j in range(0, n - i - 1):

            # --- EL CAMBIO CLAVE ---
            # 1. Accedemos a la clave ['poder'] de cada diccionario.
            # 2. Usamos '<' (menor que) porque queremos orden DESCENDENTE.
            #    Si el actual tiene MENOS poder que el siguiente, los cambiamos
            #    para que el más débil se vaya al fondo.

            poder_actual = hechiceros[j]['poder']
            poder_siguiente = hechiceros[j + 1]['poder']

            if poder_actual < poder_siguiente:
                # Intercambiamos los DICCIONARIOS completos, no solo el poder
                hechiceros[j], hechiceros[j + 1] = hechiceros[j + 1], hechiceros[j]

    return hechiceros

while True:
    print("\n--- Enciclopedia Jujutsu ---")
    print("1. Mostrar Hechiceros")
    print("2. Agregar Hechicero")
    print("3. Borrar Hechicero")
    print("4. Ordenar Hechiceros por Poder")
    print("5. Mostrar Hechiceros de Grado Especial")
    print("6. Ordenar Hechiceros por Poder (Burbuja)")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_hechiceros()
    elif opcion == "2":
        nombre = input("Ingrese el nombre del hechicero: ")
        tipo = input("Ingrese el tipo del hechicero: ")
        poder = int(input("Ingrese el poder del hechicero: "))
        agregar_hechicero(nombre, tipo, poder)
        print("Hechicero agregado exitosamente.")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del hechicero a borrar: ")
        borrar_hechicero(nombre)
        print("Hechicero borrado exitosamente.")
    elif opcion == "4":
        hechiceros_ordenados = ordenar_hechiceros_por_poder()
        print("\n--- Hechiceros Ordenados por Poder ---")
        for hechicero in hechiceros_ordenados:
            print(f"Nombre: {hechicero['nombre']}, Tipo: {hechicero['tipo']}, Poder: {hechicero['poder']}")
    elif opcion == "5":
        especiales = hechiceros_grado_especial()
        print("\n--- Hechiceros de Grado Especial ---")
        for hechicero in especiales:
            print(f"Nombre: {hechicero['nombre']}, Tipo: {hechicero['tipo']}, Poder: {hechicero['poder']}")
    elif opcion =="6":
        hechiceros_ordenados_burbuja = ordenar_hechiceros_burbuja()
        print("\n--- Hechiceros Ordenados por Poder (Burbuja) ---")
        for hechicero in hechiceros_ordenados_burbuja:
            print(f"Nombre: {hechicero['nombre']}, Tipo: {hechicero['tipo']}, Poder: {hechicero['poder']}")
    elif opcion == "7":
        print("Saliendo de la Enciclopedia Jujutsu...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")