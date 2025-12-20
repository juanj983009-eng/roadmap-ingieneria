# --- BÚSQUEDA BINARIA (BINARY SEARCH) ---
# Complejidad: O(log N) - ¡Extremadamente rápido!

def busqueda_binaria(lista, objetivo):
    inicio = 0
    final = len(lista) - 1
    pasos = 0 # Solo para ver qué tan rápido es

    while inicio <= final:
        pasos += 1

        # 1. Encontrar el punto medio
        # El // significa "división entera" (sin decimales)
        medio = (inicio + final) // 2
        valor_medio = lista[medio]

        print(f"Paso {pasos}: Buscando en índice {medio} (Valor: {valor_medio})")

        # 2. Verificar si lo encontramos
        if valor_medio == objetivo:
            return f"¡Encontrado en la posición {medio} en {pasos} pasos!"

        # 3. Decidir hacia dónde ir
        if valor_medio < objetivo:
            # Si el valor del medio es MENOR, ignoramos la izquierda
            inicio = medio + 1
        else:
            # Si el valor del medio es MAYOR, ignoramos la derecha
            final = medio - 1

    return "Elemento no encontrado."

# --- ZONA DE PRUEBAS ---
# OJO: La lista TIENE que estar ordenada.
datos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("--- INICIANDO BÚSQUEDA ---")
print(busqueda_binaria(datos, 60))