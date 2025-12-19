# --- LABORATORIO DE INPUTS Y CASTING ---
import datetime

# 1. INPUT SIMPLE (Siempre devuelve texto/str)
nombre = input("¿Cuál es tu nombre de usuario?: ")

# 2. EL PROBLEMA Y LA SOLUCIÓN (Casting)
# input() devuelve texto. La función int() lo transforma a entero.
edad_texto = input("¿Cuántos años tienes?: ")
edad_numero = int(edad_texto)  # <--- AQUÍ OCURRE LA MAGIA (CASTING)

# Forma PRO (hacerlo en una sola línea):
# estatura = float(input("¿Cuánto mides en metros? (ej. 1.75): "))

# 3. PROCESAMIENTO
# Obtenemos el año actual automáticamente del sistema
anio_actual = datetime.datetime.now().year
anio_nacimiento = anio_actual - edad_numero

# 4. SALIDA (OUTPUT)
print("--------------------------------")
print(f"Sistema: Procesando datos de {nombre}...")
print(f"Detectado: Tienes {edad_numero} años.")
print(f"Cálculo: Naciste aproximadamente en {anio_nacimiento}.")
print("--------------------------------")