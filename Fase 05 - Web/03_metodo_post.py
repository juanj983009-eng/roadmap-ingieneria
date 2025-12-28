from fastapi import FastAPI
from pydantic import BaseModel # <--- Importamos el validador
import uvicorn

app = FastAPI()

# --- 1. MODELO DE DATOS (El Molde) ---
# Esto define qué datos ACEPTAMOS. Si mandan otra cosa, lo rechazamos.
class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int = 0  # Valor por defecto (si no lo mandan, es 0)
    en_oferta: bool = False

# Base de datos simulada en memoria
inventario = []

# --- 2. RUTA POST (Crear) ---
# Fíjate que usamos @app.post, no @app.get
@app.post("/productos")
def crear_producto(item: Producto):
    # 'item' ya viene validado y convertido a objeto Python
    inventario.append(item)
    return {"mensaje": "Producto creado", "datos_guardados": item}

# --- 3. RUTA GET (Ver todos) ---
@app.get("/productos")
def ver_inventario():
    return inventario

if __name__ == "__main__":
    uvicorn.run("03_metodo_post:app", host="127.0.0.1", port=8000, reload=True)