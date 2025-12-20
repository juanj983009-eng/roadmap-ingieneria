#El Traductor

print("Colores de español a inglés:")
colores = {
    "rojo": "red",
    "verde": "green",
    "azul": "blue",
    "amarillo": "yellow",
    "negro": "black",
    "blanco": "white"
}

color = input("Ingresa un color en español: ").strip().lower()
traduccion = colores.get(color, "Color no encontrado")
print(f"La traducción de '{color}' es: {traduccion}")