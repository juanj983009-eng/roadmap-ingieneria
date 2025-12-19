#Piedra, Papel o Tijera (vs. La Máquina)

import random
opciones = ["Piedra", "Papel", "Tijera"]
print("¡Bienvenido al juego de Piedra, Papel o Tijera!")

# Entrada del usuario
eleccion_usuario = input("Elige Piedra, Papel o Tijera: ").capitalize()
while eleccion_usuario not in opciones:
    print("Elección inválida. Por favor, elige Piedra, Papel o Tijera.")
    eleccion_usuario = input("Elige Piedra, Papel o Tijera: ").capitalize()

# Elección de la máquina
eleccion_maquina = random.choice(opciones)
print(f"La máquina eligió: {eleccion_maquina}")

# Determinar el ganador
if eleccion_usuario == eleccion_maquina:
    print("¡Es un empate!")
elif (eleccion_usuario == "Piedra" and eleccion_maquina == "Tijera") or \
(eleccion_usuario == "Papel" and eleccion_maquina == "Piedra") or \
(eleccion_usuario == "Tijera" and eleccion_maquina == "Papel"):
    print("¡Felicidades! ¡Ganaste!")
else:
    print("¡La máquina gana! ¡Mejor suerte la próxima vez!")

print("¡Gracias por jugar!")