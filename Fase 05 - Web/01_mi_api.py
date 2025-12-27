from fastapi import FastAPI
import uvicorn

# Creamos la aplicación (El Mesero)
app = FastAPI()

# Definimos una RUTA (Endpoint)
# Cuando alguien entre a la dirección raíz "/" (la puerta de entrada)
@app.get("/")
def entrada_principal():
    # Retornamos un Diccionario. FastAPI lo convierte a JSON automáticamente.
    return {"mensaje": "¡Hola mundo! Mi servidor está vivo 🤖"}

# Otra ruta: /perfil
@app.get("/perfil")
def mi_perfil():
    return {
        "nombre": "Juan",
        "rol": "Ingeniero de Backend",
        "tecnologias": ["Python", "SQL", "FastAPI"]
    }