#Simulador de Cajero Automático (ATM)
saldo_cuenta = 1000.0  # Saldo inicial de la cuenta

def mostrar_saldo():
    print(f"Su saldo actual es: S/ {saldo_cuenta:.2f}")

def depositar():
    global saldo_cuenta
    monto = float(input("Ingrese el monto a depositar: S/ "))
    if monto > 0:
        saldo_cuenta += monto
        print(f"Has depositado S/ {monto:.2f}. Nuevo saldo: S/ {saldo_cuenta:.2f}")
    else:
        print("Monto inválido. El depósito debe ser mayor a cero.")

def retirar():
    global saldo_cuenta
    monto = float(input("Ingrese el monto a retirar: S/ "))
    if 0 < monto <= saldo_cuenta:
        saldo_cuenta -= monto
        print(f"Has retirado S/ {monto:.2f}. Nuevo saldo: S/ {saldo_cuenta:.2f}")
    else:
        print("Monto inválido o saldo insuficiente.")

def main():
    while True:
        print("\n--- Cajero Automático ---")
        print("1. Mostrar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            mostrar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
# Punto de arranque
main()