# --- LABORATORIO DE FUNCIONES ---

print("--- GESTIÓN DE FUNCIONES ---")

# 1. DEFINICIÓN DE LA FUNCION
# def nombre_funcion(parametros):
def saludar_ingeniero(nombre):
    # Esta función solo hace una acción, no devuelve valor.
    print(f"👋 Hola, Ingeniero {nombre}. Sistema listo.")

# 2. FUNCION CON RETORNO (RETURN) - ¡ESTO ES INGENIERÍA!
# A diferencia de print, 'return' devuelve el dato al código para seguir usándolo.
def calcular_area_cuadrado(lado):
    area = lado * lado
    return area  # <--- Devuelve el valor, no lo imprime.

def convertir_dolares_a_soles(dolares):
    tasa_cambio = 3.85
    resultado = dolares * tasa_cambio
    return resultado

# --- ZONA DE EJECUCIÓN (MAIN) ---
# Aquí usamos las herramientas que acabamos de construir.

# Uso 1: Función simple
saludar_ingeniero("Juan")
saludar_ingeniero("Sofi") # Reutilizamos el código sin reescribirlo

# Uso 2: Función con retorno
lado_usuario = 5
# Guardamos el resultado de la función en una variable
area_calculada = calcular_area_cuadrado(lado_usuario)

print(f"El área de un cuadrado de lado {lado_usuario} es: {area_calculada}")

# Uso 3: Conversión
dinero = 100
soles = convertir_dolares_a_soles(dinero)
print(f"{dinero} USD son {soles} PEN.")