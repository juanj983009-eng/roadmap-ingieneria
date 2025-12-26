import sqlite3

# 1. CONEXIÓN
# Si el archivo no existe, SQLite lo crea automáticamente.
conexion = sqlite3.connect("mi_primera_base.db")

# El "Cursor" es como el puntero del mouse. Es el que ejecuta las órdenes.
cursor = conexion.cursor()

# 2. CREAR TABLA (Solo se hace una vez)
# IF NOT EXISTS: Para que no de error si vuelves a ejecutar el programa.
sql_crear = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    correo TEXT
)
"""
cursor.execute(sql_crear)
print("✅ Tabla creada exitosamente.")

# 3. INSERTAR DATOS (CREATE)
# Fíjate en los signos de interrogación (?). Son por seguridad (evitan hackeos).
sql_insertar = "INSERT INTO usuarios (nombre, edad, correo) VALUES (?, ?, ?)"
datos = ("Juan", 25, "juan@email.com")

cursor.execute(sql_insertar, datos)
conexion.commit() # ¡IMPORTANTE! 'commit' es como el botón "Guardar"
print("✅ Usuario insertado.")

# 4. LEER DATOS (READ)
cursor.execute("SELECT * FROM usuarios")
resultado = cursor.fetchall() # Trae TODAS las filas

print("\n--- BASE DE DATOS ---")
for fila in resultado:
    print(fila) # Devuelve una Tupla: (1, 'Juan', 25, 'juan@email.com')

# 5. CERRAR CONEXIÓN (Siempre cierra la puerta al salir)
conexion.close()