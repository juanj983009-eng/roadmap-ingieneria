from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 1. RUTA DINÁMICA BÁSICA
# Lo que pongas en la URL después de /saludo/ se guardará en la variable 'nombre'
@app.get("/saludo/{nombre}")
def saludar_amigo(nombre: str):
    return {"mensaje": f"¡Hola {nombre}! Bienvenido a tu API."}

# 2. RUTA CON LÓGICA Y TIPOS DE DATOS
# Aquí esperamos un número entero (int) para el ID
@app.get("/usuario/{id_usuario}")
def buscar_usuario(id_usuario: int):
    # Simulamos una búsqueda en base de datos
    if id_usuario == 1:
        return {"id": 1, "usuario": "Juan", "nivel": "Admin"}
    elif id_usuario == 7:
        return {"id": 7, "usuario": "Cristiano", "nivel": "Leyenda"}
    else:
        return {"error": "Usuario no encontrado", "id": id_usuario}

# 3. RUTA MATEMÁTICA (Calculadora Web)
@app.get("/sumar/{num1}/{num2}")
def sumar(num1: int, num2: int):
    total = num1 + num2
    return {
        "operacion": "suma",
        "numero_1": num1,
        "numero_2": num2,
        "resultado": total
    }

if __name__ == "__main__":
    uvicorn.run("02_rutas_dinamicas:app", host="127.0.0.1", port=8000, reload=True)