#El Buscador de Precios
inventario = [
    {"nombre": "manzana", "precio": 0.5},
    {"nombre": "banana", "precio": 0.3},
    {"nombre": "naranja", "precio": 0.7},
    {"nombre": "pera", "precio": 0.6},
    {"nombre": "uva", "precio": 1.0}
]

for item in inventario:
    if item["precio"] > 0.5:
        print(f"El precio de {item['nombre']} es {item['precio']}")
