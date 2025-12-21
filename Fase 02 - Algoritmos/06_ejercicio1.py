#El Buscador de Precios
inventario = [
    {"nombre": "manzana", "precio": 0.5},
    {"nombre": "banana", "precio": 0.3},
    {"nombre": "naranja", "precio": 0.7},
    {"nombre": "pera", "precio": 0.6},
    {"nombre": "uva", "precio": 1.0}
]
producto = input("Ingresa el nombre del producto: ").strip().lower()
encontrado = False
for item in inventario:
    if item["nombre"] == producto:
        print(f"El precio de la {producto} es: ${item['precio']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado en el inventario.")

