# --- LABORATORIO DE TIPOS DE DATOS ---

# 1. Enteros (int): Números sin decimales
ram_gb = 16
print(f"Memoria RAM: {ram_gb} GB")
print(type(ram_gb)) # type() es tu herramienta de diagnóstico

# 2. Flotantes (float): Números con decimales (Cuidado con la precisión)
precio_dolar = 3.85
print(f"Precio del dólar: {precio_dolar}")
print(type(precio_dolar))

# 3. Cadenas de Texto (str): Secuencia de caracteres
mensaje = "Error 404: Not Found"
numero_falso = "100" # Esto parece número, pero es texto
print(mensaje)
print(type(numero_falso))

# 4. Booleanos (bool): Interruptores (Verdadero/Falso) -> Base de la lógica binaria
es_servidor_activo = True
print(f"¿El servidor está prendido?: {es_servidor_activo}")
print(type(es_servidor_activo))

# --- EXPERIMENTO DE INGENIERÍA ---
# Vamos a ver la diferencia entre sumar números y sumar textos
a = 10
b = 20
suma_numeros = a + b

x = "10"
y = "20"
suma_textos = x + y # Esto se llama "Concatenación"

print("-------------------")
print(f"Suma Matemática (10 + 20): {suma_numeros}")
print(f"Suma de Texto ('10' + '20'): {suma_textos}")