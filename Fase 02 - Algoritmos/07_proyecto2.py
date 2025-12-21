#El Rastreador de Gastos (Finance Tracker)
gastos = [
    {"descripcion": "salchipapa", "monto": 150.0, "categoria": "comida"},
    {"descripcion": "bus", "monto": 75.0, "categoria": "transporte"},
    {"descripcion": "television", "monto": 200.0, "categoria": "entretenimiento"},
]

def agregar_gasto():
    descripcion = input("Ingrese la descripción del gasto: ")
    monto = float(input("Ingrese el monto del gasto: "))
    categoria = input("Ingrese la categoría del gasto: ")
    gastos.append({"descripcion": descripcion, "monto": monto, "categoria": categoria})
    print("Gasto agregado exitosamente.")

def mostrar_gastos():
    print("Lista de gastos:")
    for gasto in gastos:
        print(f"{gasto['descripcion']} - Monto: {gasto['monto']} - Categoría: {gasto['categoria']}")

def total_gastos():
    total = sum(gasto["monto"] for gasto in gastos)
    print(f"Total de gastos: {total}")

def filtrar_por_categoria():
    categoria = input("Ingrese la categoría a filtrar: ")
    print(f"Gastos en la categoría '{categoria}':")
    for gasto in gastos:
        if gasto["categoria"].lower() == categoria.lower():
            print(f"{gasto['descripcion']} - Monto: {gasto['monto']}")

def main():
    while True:
        print("\n--- Rastreador de Gastos ---")
        print("1. Agregar Gasto")
        print("2. Mostrar Gastos")
        print("3. Total de Gastos")
        print("4. Filtrar por Categoría")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_gasto()
        elif opcion == "2":
            mostrar_gastos()
        elif opcion == "3":
            total_gastos()
        elif opcion == "4":
            filtrar_por_categoria()
        elif opcion == "5":
            print("Saliendo del rastreador de gastos...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
