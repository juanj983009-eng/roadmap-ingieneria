# Ejercicio 2.2: Cálculo de total con IGV

nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad a comprar: "))

subtotal = precio_unitario * cantidad
total = subtotal * 1.18  # Aplicando IGV del 18%
print(f"Subtotal: S/ {subtotal:.2f}")
print(f"Total a pagar (con IGV): S/ {total:.2f}")
