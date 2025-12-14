# --- SISTEMA DE INVENTARIO (LISTAS) ---

print("--- INVENTARIO DE HARDWARE ---")

# 1. CREACIÓN (Una lista vacía o con datos)
# Sintaxis: corchetes []
componentes = ["Monitor", "Teclado", "Mouse"]

# Imprimir la lista completa
print(f"Lista inicial: {componentes}")

# 2. ACCESO (Indexing) - Igual que los Strings
print(f"El primer objeto es: {componentes[0]}") # Monitor
print(f"El último objeto es: {componentes[-1]}") # Mouse

# 3. AGREGAR DATOS (Método .append)
# Esto mete datos AL FINAL de la lista dinámicamente.
print("\n...Agregando nuevos productos...")
componentes.append("Audífonos")
componentes.append("Webcam")

print(f"Lista actualizada: {componentes}")

# 4. ELIMINAR DATOS (Método .remove o .pop)
print("\n...Vendiendo el Monitor...")
componentes.remove("Monitor") # Busca el texto exacto y lo borra

print(f"Inventario post-venta: {componentes}")

# 5. INTEGRACIÓN: LISTAS + CICLO FOR (La pareja poderosa)
# "Para cada producto en la lista de componentes..."
print("\n--- REPORTE FINAL ---")
for producto in componentes:
    print(f"- Producto disponible: {producto}")