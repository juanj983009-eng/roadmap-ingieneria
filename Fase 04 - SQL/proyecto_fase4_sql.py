import sqlite3

NOMBRE_DB = "almacen.db"

def conectar():
    return sqlite3.connect(NOMBRE_DB)

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

class GestorInventario:
    def __init__(self):
        # Al crear el gestor, nos aseguramos de que la tabla exista
        crear_tabla()

    def agregar_producto(self, nombre, precio, stock):
        conn = conectar()
        cursor = conn.cursor()
        # SQL con parámetros (?) para seguridad
        sql = "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)"
        cursor.execute(sql, (nombre, precio, stock))
        conn.commit()
        conn.close()
        print(f"✅ Producto '{nombre}' guardado en la base de datos.")

    def ver_productos(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        conn.close()

        print("\n--- INVENTARIO ACTUAL ---")
        print(f"{'ID':<5} {'NOMBRE':<20} {'PRECIO':<10} {'STOCK':<5}")
        print("-" * 45)
        for p in resultados:
            # p es (id, nombre, precio, stock)
            print(f"{p[0]:<5} {p[1]:<20} ${p[2]:<9} {p[3]:<5}")

    def eliminar_producto(self, id_producto):
        conn = conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM productos WHERE id = ?"
        cursor.execute(sql, (id_producto,))
        conn.commit()
        conn.close()
        print(f"🗑️ Producto ID {id_producto} eliminado.")

    def actualizar_stock(self, id_producto, nuevo_stock):
        conn = conectar()
        cursor = conn.cursor()
        sql = "UPDATE productos SET stock = ? WHERE id = ?"
        cursor.execute(sql, (nuevo_stock, id_producto))
        conn.commit()
        conn.close()
        print(f"🔄 Stock del producto ID {id_producto} actualizado a {nuevo_stock}.")

# --- INTERFAZ DE USUARIO ---
def main():
    tienda = GestorInventario()

    while True:
        print("\n[ SISTEMA DE ALMACÉN SQL ]")
        print("1. Nuevo Producto")
        print("2. Ver Inventario")
        print("3. Eliminar Producto")
        print("4. Actualizar Stock")
        print("5. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            nom = input("Nombre: ")
            prec = float(input("Precio: "))
            stk = int(input("Stock: "))
            tienda.agregar_producto(nom, prec, stk)

        elif opcion == "2":
            tienda.ver_productos()

        elif opcion == "3":
            tienda.ver_productos() # Mostramos la lista para que vea el ID
            id_borrar = int(input("Ingrese el ID del producto a eliminar: "))
            tienda.eliminar_producto(id_borrar)

        elif opcion == "4":
            tienda.ver_productos() # Mostramos la lista para que vea el ID
            id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
            nuevo_stk = int(input("Nuevo stock: "))
            tienda.actualizar_stock(id_actualizar, nuevo_stk)

        elif opcion == "5":
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()