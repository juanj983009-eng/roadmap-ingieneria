# --- SISTEMA DE CONTROL DE ACCESO ---

print("--- SECURE GATE v1.0 ---")

# 1. Pedimos datos y convertimos a número (Casting)
edad = int(input("Por favor, ingrese su edad: "))

# 2. La Decisión (Logic Gate)
# Usamos operadores de comparación:
# >  Mayor que
# <  Menor que
# >= Mayor o igual que
# <= Menor o igual que
# == Igual a (OJO: es doble igual para comparar)
# != Diferente de

if edad >= 18:
    # ----------------------------------------------------
    # ZONA INDENTADA: Todo lo que esté aquí dentro SOLO
    # ocurre si la condición es VERDADERA.
    # ----------------------------------------------------
    print("✅ Acceso CONCEDIDO.")
    print("Bienvenido al sistema, Ingeniero.")

else:
    # ----------------------------------------------------
    # ZONA INDENTADA DEL ELSE: Ocurre si la condición
    # es FALSA.
    # ----------------------------------------------------
    print("⛔ Acceso DENEGADO.")
    print("Lo siento, eres menor de edad.")

# 3. Flujo Principal (Sin indentación)
# Esta línea se ejecuta SIEMPRE, pase lo que pase.
print("--- Fin del proceso ---")