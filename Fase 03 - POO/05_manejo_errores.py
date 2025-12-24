# --- MANEJO DE ERRORES Y EXCEPCIONES ---

def division_segura():
    while True:
        try:
            # ZONA PELIGROSA ⚠️
            # Aquí pueden pasar cosas malas si el usuario escribe tonterías.
            print("\n--- CALCULADORA DE DIVISIÓN ---")
            numerador = float(input("Ingresa el número a dividir: "))
            divisor = float(input("Ingresa el divisor: "))

            # Si el divisor es 0, Python lanzaría un error aquí
            resultado = numerador / divisor

        except ZeroDivisionError:
            # Esto atrapa SOLO si intentan dividir por cero
            print("⛔ Error Matemático: ¡No puedes dividir entre cero!")

        except ValueError:
            # Esto atrapa SOLO si escriben letras en vez de números
            print("⛔ Error de Texto: ¡Debes ingresar números, no letras!")

        except Exception as e:
            # Esto atrapa CUALQUIER otra cosa rara (el comodín)
            print(f"⛔ Error desconocido: {e}")

        else:
            # Esto se ejecuta SOLO si NO hubo errores en el try
            print(f"✅ Resultado: {resultado}")
            break # Rompemos el ciclo porque salió bien

        finally:
            # Esto se ejecuta SIEMPRE (haya error o no)
            print("🔄 Fin del intento.")

# Probamos la función
division_segura()