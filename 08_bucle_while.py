# --- MENÚ INTERACTIVO (WHILE LOOP) ---

print("--- SISTEMA INICIADO ---")

# Variable de control
ejecutando = True

while ejecutando:
    # 1. Mostrar opciones
    print("\n[ MENÚ PRINCIPAL ]")
    print("1. Saludar")
    print("2. Calcular suma")
    print("3. SALIR")

    # 2. Pedir orden
    opcion = input("Elige una opción (1-3): ")

    # 3. Evaluar orden
    if opcion == "1":
        print("👋 ¡Hola Ingeniero!")

    elif opcion == "2":
        # Fíjate que podemos hacer lógica aquí dentro
        n1 = int(input("Num 1: "))
        n2 = int(input("Num 2: "))
        print(f"Suma: {n1 + n2}")

    elif opcion == "3":
        print("Cerrando sistema...")
        # AQUÍ ROMPEMOS EL CICLO
        ejecutando = False
        # También podrías usar la palabra clave 'break'

    else:
        print("⛔ Opción no válida, intenta de nuevo.")

print("--- SISTEMA APAGADO ---")