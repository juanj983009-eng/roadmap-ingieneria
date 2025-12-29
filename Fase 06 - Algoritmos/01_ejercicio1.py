# Creamos la libreta (diccionario) vacía
memoria = {}

def fibonacci_turbo(n):
    # 1. ¿Ya lo tengo anotado? (El Truco)
    if n in memoria:
        return memoria[n]

    # 2. Casos Base
    if n == 0:
        return 0
    if n == 1:
        return 1

    # 3. Calcular y GUARDAR en la libreta
    resultado = fibonacci_turbo(n - 1) + fibonacci_turbo(n - 2)
    memoria[n] = resultado  # <--- Aquí está la magia

    return resultado

# --- PRUEBA DE VELOCIDAD ---
import time

inicio = time.time()
n = int(input("Introduce un número para calcular su Fibonacci: "))  # ¡Prueba con 100! Antes era imposible.
resultado = fibonacci_turbo(n)
fin = time.time()

print(f"Fibonacci({n}) = {resultado}")
print(f"⏱️ Tiempo: {fin - inicio} segundos")