# --- SIMULADOR DE LOGIN ---

# Credenciales correctas (Base de datos simulada)
USUARIO_REAL = "admin"
PASS_REAL = "1234"

print("--- INICIO DE SESIÓN ---")
user_input = input("Usuario: ")
pass_input = input("Contraseña: ")

# LÓGICA COMBINADA (AND)
# Python revisa: ¿El usuario coincide? Y ADEMÁS ¿La contraseña coincide?
# Solo si AMBAS son True, entra al bloque.

if user_input == USUARIO_REAL and pass_input == PASS_REAL:
    print("🔓 Acceso Concedido. Bienvenido al panel de control.")

    # BONUS: Un if anidado (Un if dentro de otro if)
    nivel = int(input("Nivel de seguridad (1-5): "))

    if nivel == 5 or user_input == "admin":
        # Aquí usamos OR: Basta con ser nivel 5 O ser admin
        print("⚡ Tienes permisos de SUPERUSUARIO.")
    else:
        print("Usuario estándar.")

else:
    print("⛔ Error: Usuario o contraseña incorrectos.")

print("--- Fin del sistema ---")