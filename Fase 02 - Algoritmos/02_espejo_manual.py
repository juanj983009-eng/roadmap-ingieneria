# --- LOGICA DE DOS PUNTEROS (TWO POINTERS) ---

def invertir_lista_manual(lista):
    # 1. Definimos los punteros iniciales
    izquierda = 0
    derecha = len(lista) - 1  # El último índice siempre es largo - 1

    # 2. El Ciclo: Ejecutar mientras los punteros no se choquen
    while izquierda < derecha:

        # --- ZONA DE VISUALIZACIÓN (DEBUGGING) ---
        # Imprimimos para ver qué está pasando antes del cambio
        print(f"Cambiando {lista[izquierda]} por {lista[derecha]}")

        # --- TU TAREA: EL SWAP ---
        # Intercambia los valores de lista[izquierda] y lista[derecha]
        # (Usa la misma técnica que en Bubble Sort: a, b = b, a)
        lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

        # ... escribe tu código de swap aquí ...

        # 3. Mover los punteros
        izquierda += 1  # Camina hacia el centro ->
        derecha -= 1    # Camina hacia el centro <-

    return lista

# --- PRUEBA ---
mis_datos = [10, 20, 30, 40, 50]
print(f"Original: {mis_datos}")

resultado = invertir_lista_manual(mis_datos)
print(f"Invertida: {resultado}")