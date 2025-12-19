#Simulador de Carreras (Consola)
coche_rojo  = 0
coche_azul  = 0
coche_verde = 0

import random
print("¡Bienvenido al Simulador de Carreras!")
input("Presiona Enter para iniciar la carrera...")
while True:
    input("\nAvance de los coches:")
    coche_rojo  += random.randint(1, 10)
    coche_azul  += random.randint(1, 10)
    coche_verde += random.randint(1, 10)
    distancia_rojo = coche_rojo // 10
    distancia_azul = coche_azul // 10
    distancia_verde = coche_verde // 10
    print(f"Coche Rojo: {'-' * (distancia_rojo)}{coche_rojo} km | Coche Azul: {'-' * (distancia_azul)} {coche_azul} km | Coche Verde: {'-' * (distancia_verde)} {coche_verde} km ")
    if coche_rojo >= 100 or coche_azul >= 100 or coche_verde >= 100:
        break
if coche_rojo >= 100:
    print("¡El Coche Rojo ha ganado la carrera!")
elif coche_azul >= 100:
    print("¡El Coche Azul ha ganado la carrera!")
else:
    print("¡El Coche Verde ha ganado la carrera!")
print("¡Gracias por participar en el Simulador de Carreras!")

