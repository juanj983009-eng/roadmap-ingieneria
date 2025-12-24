# --- ENCAPSULAMIENTO Y DATOS PRIVADOS ---

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # ATENCIÓN: El guion bajo doble (__) hace que la variable sea PRIVADA.
        # Python la "esconde" para que no se pueda tocar desde fuera.
        self.__saldo = saldo_inicial

    # Método Público para ver el saldo (Getter)
    def consultar_saldo(self):
        print(f"💰 Saldo de {self.titular}: ${self.__saldo}")

    # Método Público para agregar dinero (Setter)
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"✅ Depósito exitoso: +${monto}")
        else:
            print("⛔ Error: No puedes depositar montos negativos.")

    # Método Público para retirar
    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"✅ Retiro exitoso: -${monto}")
        else:
            print("⛔ Error: Fondos insuficientes o monto inválido.")

# --- ZONA DE PRUEBA ---
mi_cuenta = CuentaBancaria("Juan", 1000)

mi_cuenta.consultar_saldo()
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
mi_cuenta.consultar_saldo()

print("\n--- INTENTO DE HACKEO ---")
# Intentamos cambiar el saldo "a la fuerza"
mi_cuenta.__saldo = 9999999  # Esto NO funcionará como esperas (o dará error)
print("Intenté poner el saldo en 9 millones...")

# Verificamos si funcionó el hackeo
mi_cuenta.consultar_saldo()