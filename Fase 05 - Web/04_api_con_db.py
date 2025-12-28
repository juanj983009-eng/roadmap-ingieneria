import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()
NOMBRE_DB = "tienda_online.db"

# --- 1. CONFIGURACIÓN DE BASE DE DATOS ---
def inicializar_db():
    conn = sqlite3.connect(NOMBRE_DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            precio REAL,
            stock INTEGER
        )
    """)
    conn.commit()
    conn.close()

# Ejecutamos esto al arrancar para asegurar que la tabla exista
inicializar_db()

# --- 2. MODELO DE DATOS (PYDANTIC) ---
class ProductoNuevo(BaseModel):
    nombre: str
    precio: float
    stock: int

# --- 3. ENDPOINTS (RUTAS) ---

@app.post("/productos")
def crear_producto(item: ProductoNuevo):
    # Conectamos a la BD
    conn = sqlite3.connect(NOMBRE_DB)
    cursor = conn.cursor()

    # Insertamos los datos que llegaron de la web
    sql = "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)"
    cursor.execute(sql, (item.nombre, item.precio, item.stock))

    conn.commit()
    conn.close()

    return {"mensaje": "✅ Producto guardado en la base de datos"}

@app.get("/productos")
def leer_productos():
    conn = sqlite3.connect(NOMBRE_DB)
    # Row_factory hace que los resultados parezcan diccionarios y no tuplas
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()
    conn.close()

    return resultados

if __name__ == "__main__":
    uvicorn.run("04_api_con_db:app", host="127.0.0.1", port=8000, reload=True)