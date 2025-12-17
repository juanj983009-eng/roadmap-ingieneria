#La Caja Registradora (Punto de Venta)

print("¡Bienvenido a la Caja Registradora!")
carrito = []
total_compra = 0.0
while True:
    nombre_producto = input("Ingrese el nombre del producto (o 'salir' para finalizar): ")
    if nombre_producto.lower() == 'salir':
        break
    try:
        precio_unitario = float(input(f"Ingrese el precio unitario de '{nombre_producto}': S/ "))
        cantidad = int(input(f"Ingrese la cantidad de '{nombre_producto}': "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido para el precio y la cantidad.")
        continue

    subtotal = precio_unitario * cantidad
    carrito.append((nombre_producto, precio_unitario, cantidad, subtotal))
    total_compra += subtotal
    print(f"'{nombre_producto}' agregado al carrito. Subtotal: S/ {subtotal:.2f}\n")
print("\nResumen de la compra:")
print("{:<20} {:<10} {:<10} {:<10}".format("Producto", "Precio", "Cantidad", "Subtotal"))
for item in carrito:
    print("{:<20} S/ {:<10.2f} {:<10} S/ {:<10.2f}".format(item[0], item[1], item[2], item[3]))
print(f"\nTotal a pagar: S/ {total_compra:.2f}")
print(f"\nTotal de productos comprados: {len(carrito)}")
print("¡Gracias por su compra!")