#Sistema de Reservas de Cine (Matrices)
sala = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def mostrar_sala():
    print("Estado de la sala (0: disponible, 1: reservado):")
    for fila in sala:
        print(" ".join(str(asiento) for asiento in fila))

def reservar_asiento(fila, columna):
    if sala[fila][columna] == 0:
        sala[fila][columna] = 1
        print(f"Asiento en fila {fila + 1}, columna {columna + 1} reservado exitosamente.")
    else:
        print(f"El asiento en fila {fila + 1}, columna {columna + 1} ya está reservado.")
        return
# Ejemplo de uso
mostrar_sala()
x =  int(input("Ingrese la cantidad de asientos a reservar: "))
for i in range(x):
    fila = int(input("Ingrese la fila del asiento a reservar (1-5): ")) - 1
    columna = int(input("Ingrese la columna del asiento a reservar (1-5): ")) - 1
    reservar_asiento(fila, columna)
mostrar_sala()
