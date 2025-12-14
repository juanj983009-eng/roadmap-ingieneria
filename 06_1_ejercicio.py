# Carrito de compras simple

carrito = []
articulos = input("Ingrese la cantidad de articulos que deseas comprar: ")

for i in range(int(articulos)):
    producto = input(f"Ingrese el nombre del articulo {i+1}: ")
    carrito.append(producto)

print("\n--- Artículos en tu carrito ---")
for item in carrito:
    print(f"- {item}")




clases = []
cantidad_cursos = int(input("¿Cuántos cursos deseas inscribir?: "))
for i in range(cantidad_cursos):
    curso = input(f"Ingrese el nombre del curso {i+1}: ")
    clases.append(curso)

print("\n--- Cursos Inscritos ---")
for curso in clases:
    print(f"- {curso}")