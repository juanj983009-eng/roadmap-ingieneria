#El Ahorcado (Hangman)
import random
def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()

def jugar_ahorcado():
    lista_palabras = ["python", "programacion", "desarrollo", "computadora", "teclado", "monitor", "raton", "software", "hardware", "algoritmo"]
    palabra_secreta = random.choice(lista_palabras)
    letras_adivinadas = []
    intentos_restantes = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra secreta letra por letra.")

    while intentos_restantes > 0:
        print("\n" + mostrar_tablero(palabra_secreta, letras_adivinadas))
        print(f"Intentos restantes: {intentos_restantes}")
        letra_usuario = input("Ingresa una letra: ").lower()

        if len(letra_usuario) != 1 or not letra_usuario.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue

        if letra_usuario in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra_usuario)

        if letra_usuario in palabra_secreta:
            print(f"¡Bien hecho! La letra '{letra_usuario}' está en la palabra.")
        else:
            intentos_restantes -= 1
            print(f"La letra '{letra_usuario}' no está en la palabra.")

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break
    else:
        print("\n¡Has perdido! La palabra secreta era:", palabra_secreta)

jugar_ahorcado()