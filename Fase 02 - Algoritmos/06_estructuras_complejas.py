# --- SIMULACIÓN DE BASE DE DATOS (JSON STYLE) ---

# Una LISTA que contiene DICCIONARIOS
inventario = [
    {
        "id": 1,
        "nombre": "Laptop",
        "precio": 1500.00,
        "stock": 5
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "precio": 25.50,
        "stock": 50
    },
    {
        "id": 3,
        "nombre": "Teclado",
        "precio": 100.00,
        "stock": 20
    }
]

print("--- ACCEDIENDO A DATOS ANIDADOS ---")

# 1. Acceder al primer producto (Índice 0)
producto_1 = inventario[0]
print(f"Producto completo: {producto_1}")

# 2. Acceder a un dato ESPECÍFICO (Nombre del segundo producto)
# Sintaxis: lista[indice][clave]
nombre_mouse = inventario[1]["nombre"]
print(f"Item 2: {nombre_mouse}")

# 3. Recorrer la base de datos (Reporte)
print("\n--- REPORTE DE INVENTARIO ---")
for item in inventario:
    # 'item' se convierte en el diccionario de turno
    nombre = item["nombre"]
    precio = item["precio"]
    stock = item["stock"]

    print(f"Producto: {nombre} | Valor en almacén: ${precio * stock}")