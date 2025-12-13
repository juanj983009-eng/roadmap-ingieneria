# --- LABORATORIO DE CICLOS (LOOPS) ---
import time

print("--- INICIANDO PROTOCOLO DE REPETICIÓN ---")

# 1. CICLO CON RANGO (Matemático)
# Queremos repetir algo 5 veces.
# La variable 'i' (iterador) va cambiando de valor en cada vuelta.
print("\n>>> Ejemplo 1: Conteo simple")

for i in range(1, 6): # Esto irá del 1 al 5
    print(f"Vuelta número: {i}")

# 2. CICLO INVERSO (Cuenta regresiva)
# range(inicio, fin, paso) -> El paso -1 hace que reste
print("\n>>> Ejemplo 2: Lanzamiento de Cohete")

for contador in range(10, 0, -1):
    print(f"T-minus: {contador}")
    time.sleep(1) # Descomenta esto para ver el efecto de espera real
    
print("🚀 ¡DESPEGUE!")

# 3. ACUMULADOR (Patrón de Diseño básico)
# Sumar los números del 1 al 100 automáticamente.
print("\n>>> Ejemplo 3: La Suma de Gauss (1 al 100)")

suma_total = 0 # Variable vacía para ir guardando

for numero in range(1, 101):
    suma_total = suma_total + numero
    # En cada vuelta, sumamos el número actual al total acumulado

print(f"La suma de 1 a 100 es: {suma_total}")