#Generador de Contraseñas Seguras
import random
import string
def generar_contrasena(longitud):
    if longitud < 8:
        print("La longitud mínima recomendada es 8 caracteres.")
        return None

    # Definir los caracteres a usar
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    digitos = string.digits
    simbolos = string.punctuation

    # Asegurar que la contraseña tenga al menos un carácter de cada tipo
    contrasena = [
        random.choice(minusculas),
        random.choice(mayusculas),
        random.choice(digitos),
        random.choice(simbolos)
    ]

    # Rellenar el resto de la contraseña con una mezcla aleatoria de todos los caracteres
    todos_los_caracteres = minusculas + mayusculas + digitos + simbolos
    contrasena += random.choices(todos_los_caracteres, k=longitud - 4)

    # Mezclar la lista para evitar un patrón predecible
    random.shuffle(contrasena)

    return ''.join(contrasena)

# Solicitar al usuario la longitud de la contraseña
longitud_deseada = int(input("Ingrese la longitud deseada para la contraseña (mínimo 8 caracteres): "))
contrasena_generada = generar_contrasena(longitud_deseada)
if contrasena_generada:
    print(f"Contraseña generada: {contrasena_generada}")
    print(f"Longitud de la contraseña: {len(contrasena_generada)} caracteres")
    print("¡Recuerda guardarla en un lugar seguro!")
