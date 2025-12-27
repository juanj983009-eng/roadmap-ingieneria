import sqlite3

conexion = sqlite3.connect("mi_primera_base.db")
cursor = conexion.cursor()

print("--- ANTES DE LOS CAMBIOS ---")
cursor.execute("SELECT * FROM usuarios")
for u in cursor.fetchall():
    print(u)

# 1. ACTUALIZAR (UPDATE)
# Sintaxis: UPDATE tabla SET columna = nuevo_valor WHERE condicion
print("\n🔄 Actualizando a Carla...")

# Vamos a buscar a Carla por su nombre y añadirle Dra. a su nombre
# OJO: En la vida real, es más seguro buscar por ID, pero aquí usaremos nombre.
cursor.execute("UPDATE usuarios SET nombre = 'Dra. Carla' WHERE nombre = 'Carla'")

# 2. ELIMINAR (DELETE)
# Sintaxis: DELETE FROM tabla WHERE condicion
print("❌ Eliminando usuarios maypores de 30 años...")

cursor.execute("DELETE FROM usuarios WHERE edad > 30")

# 3. GUARDAR CAMBIOS
# Si no haces commit, nada de esto se guarda de verdad.
conexion.commit()

print("\n--- DESPUÉS DE LOS CAMBIOS ---")
cursor.execute("SELECT * FROM usuarios")
for u in cursor.fetchall():
    print(u)

conexion.close()