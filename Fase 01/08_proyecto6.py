#Simulador de Batalla RPG (Por Turnos)

import random

hp_jugador = 100
hp_enemigo = 100

print("¡Bienvenido al Simulador de Batalla RPG!")
print("Tú y tu enemigo comienzan con 100 puntos de vida cada uno.")
while hp_jugador > 0 and hp_enemigo > 0:
    print(f"\nTu HP: {hp_jugador} | HP del Enemigo: {hp_enemigo}")

    accion = input("¿Qué acción deseas realizar? (atacar/curar): ").lower()

    if accion == "atacar":
        daño_jugador = random.randint(10, 30)
        hp_enemigo -= daño_jugador
        print(f"¡Atacaste al enemigo y le causaste {daño_jugador} puntos de daño!")
    elif accion == "curar":
        cura_jugador = random.randint(15, 25)
        hp_jugador += cura_jugador
        if hp_jugador > 100:
            hp_jugador = 100
        print(f"¡Te curaste y recuperaste {cura_jugador} puntos de vida!")
    else:
        print("Acción inválida. Por favor, elige 'atacar' o 'curar'.")
        continue

    if hp_enemigo <= 0:
        print("\n¡Has derrotado al enemigo! ¡Felicidades!")
        break

    daño_enemigo = random.randint(10, 25)
    hp_jugador -= daño_enemigo
    print(f"El enemigo te atacó y te causó {daño_enemigo} puntos de daño!")

    if hp_jugador <= 0:
        print("\n¡Has sido derrotado por el enemigo! ¡Mejor suerte la próxima vez!")

print("¡Gracias por jugar al Simulador de Batalla RPG!")