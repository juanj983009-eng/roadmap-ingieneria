import json

# Nombre del archivo donde guardaremos los datos
ARCHIVO_DB = "inventario.json"

def guardar_datos(lista_productos):
    # 'w' = Write (Sobrescribir). Cada vez que guardamos, actualizamos todo el archivo.
    with open(ARCHIVO_DB, 'w', encoding='utf-8') as f:
        # json.dump(DATOS, ARCHIVO, OPCIONES)
        # indent=4 es para que el archivo se vea bonito y ordenado (no todo en una línea)
        json.dump(lista_productos, f, indent=4)
    print("💾 Datos guardados correctamente en inventario.json")

def cargar_datos():
    try:
        # 'r' = Read (Leer)
        with open(ARCHIVO_DB, 'r', encoding='utf-8') as f:
            datos = json.load(f) # ¡Magia! Convierte el texto del archivo a Lista de Python
            return datos
    except FileNotFoundError:
        # Si el archivo no existe (la primera vez), devolvemos una lista vacía
        print("⚠️ No se encontró archivo previo. Creando base de datos nueva.")
        return []

# --- ZONA DE PRUEBAS ---

# 1. Intentamos cargar lo que había antes
mis_productos = cargar_datos()

print(f"📦 Productos actuales en memoria: {mis_productos}")

# 2. Agregamos un producto nuevo
# Pedimos datos al usuario (o los inventamos para probar)
nuevo = {
    "nombre": "Laptop Gamer",
    "precio": 1500,
    "stock": 10
}
mis_productos.append(nuevo)

# 3. Guardamos la lista actualizada
guardar_datos(mis_productos)

print("✅ Proceso terminado. Cierra y vuelve a abrir para ver la magia.")