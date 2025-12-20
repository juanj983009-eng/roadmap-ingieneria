# --- DICCIONARIOS (HASH MAPS) ---
# Complejidad de búsqueda: O(1) - ¡La más rápida posible!

print("--- SISTEMA DE PRODUCTOS ---")

# 1. Creación (Llave : Valor)
# En tu POS, la llave sería el Código de Barras o ID.
base_de_datos = {
    "A001": "Laptop Gamer",
    "B002": "Mouse Óptico",
    "C003": "Teclado Mecánico",
    "D004": "Monitor 24 pulg"
}

# 2. Acceso Instantáneo
# No recorre nada. Va directo a la memoria donde está "B002".
codigo = "B002"
print(f"Buscando {codigo}...")
print(f"Producto encontrado: {base_de_datos[codigo]}")

# 3. Modificar y Agregar
base_de_datos["B002"] = "Mouse Inalámbrico" # Actualizar precio o nombre
base_de_datos["E005"] = "Webcam HD"         # Agregar nuevo

# 4. Eliminar
del base_de_datos["A001"]

# Imprimir todo el diccionario (se ve como un JSON)
print("\nInventario actualizado:")
print(base_de_datos)

# --- TRUCO PRO: GET ---
# Si buscas algo que no existe con corchetes [], el programa explota.
# Usa .get() para evitar errores.
consulta = base_de_datos.get("Z999", "Producto no encontrado")
print(f"\nBúsqueda de Z999: {consulta}")