import sqlite3

conexion = sqlite3.connect("mi_primera_base.db")
cursor = conexion.cursor()

print("--- ANTES DE LOS CAMBIOS ---")
cursor.execute("SELECT * FROM usuarios")
for u in cursor.fetchall():
    print(u)

# 1. ACTUALIZAR (UPDATE)
# Sintaxis: UPDATE tabla SET columna = nuevo_valor WHERE condicion
print("\n🔄 Actualizando a Daniel...")

# Vamos a buscar a Daniel por su nombre y sumarle 1 año a su edad
# OJO: En la vida real, es más seguro buscar por ID, pero aquí usaremos nombre.
cursor.execute("UPDATE usuarios SET edad = 16 WHERE nombre = 'Daniel'")

# 2. ELIMINAR (DELETE)
# Sintaxis: DELETE FROM tabla WHERE condicion
print("❌ Eliminando a Beto...")

cursor.execute("DELETE FROM usuarios WHERE nombre = 'Beto'")

# 3. GUARDAR CAMBIOS
# Si no haces commit, nada de esto se guarda de verdad.
conexion.commit()

print("\n--- DESPUÉS DE LOS CAMBIOS ---")
cursor.execute("SELECT * FROM usuarios")
for u in cursor.fetchall():
    print(u)

conexion.close()