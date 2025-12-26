import sqlite3

# Conectamos a la MISMA base de datos de antes
conexion = sqlite3.connect("mi_primera_base.db")
cursor = conexion.cursor()

# 1. LIMPIEZA (Opcional, para no llenar de basura)
# DELETE FROM borra datos, pero deja la tabla viva.
# ¡CUIDADO! Si no pones WHERE, borra TODO.
cursor.execute("DELETE FROM usuarios") 
print("🧹 Base de datos limpiada.")

# 2. INSERCIÓN MASIVA (executemany)
# En lugar de hacer 3 inserts, hacemos uno solo con una lista de tuplas.
gente_nueva = [
    ("Ana", 18, "ana@test.com"),
    ("Beto", 35, "beto@test.com"),
    ("Carla", 40, "carla@test.com"),
    ("Daniel", 15, "dani@test.com")
]

# El '?' se llenará con cada dato de la lista automáticamente
cursor.executemany("INSERT INTO usuarios (nombre, edad, correo) VALUES (?, ?, ?)", gente_nueva)
conexion.commit()
print(f"✅ Se insertaron {cursor.rowcount} usuarios nuevos.")

# 3. BÚSQUEDA INTELIGENTE (WHERE)
print("\n--- 🔍 BUSCANDO MAYORES DE EDAD (<20) ---")

# La orden SQL: "Selecciona TODO de usuarios DONDE la edad sea menor a 20"
sql_busqueda = "SELECT * FROM usuarios WHERE edad < 20"
cursor.execute(sql_busqueda)
resultados = cursor.fetchall()

for u in resultados:
    # u es una tupla: (id, nombre, edad, correo)
    print(f"ID: {u[0]} | Nombre: {u[1]} | Edad: {u[2]}")

# 4. BÚSQUEDA ESPECÍFICA
print("\n--- 🔍 BUSCANDO A 'Usuarios cuyo nombre comienza con \"C\"' ---")
# Fíjate en las comillas simples 'Daniel' dentro del SQL
cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE 'C%'")
daniel = cursor.fetchone() # fetchone trae SOLO UNO (el primero que encuentre)
print(daniel)

conexion.close()