# --- PROYECTO FASE 1: GESTOR DE TAREAS ---

def mostrar_tareas(lista_tareas):
    if not lista_tareas: # Si la lista está vacía
        print("La lista está vacía.")
    else:
        # TAREA PARA TI: Usa un for para imprimir cada tarea
        # Pista: for tarea in lista_tareas...
        for tareas in lista_tareas:
            print(f"Lista de tareas: {tareas}") # Borra esto y pon tu código

def agregar_tarea(lista_tareas, nueva_tarea):
    # TAREA PARA TI: Agrega la nueva_tarea a la lista
    lista_tareas.append(nueva_tarea)
    print("Tarea agregada") # Borra esto y pon tu código


def eliminar_tarea(lista_tareas, tarea_a_eliminar):    # TAREA PARA TI: Elimina tarea_a_eliminar de la lista
    if tarea_a_eliminar in lista_tareas:
        lista_tareas.remove(tarea_a_eliminar)
        print("Tarea eliminada") # Borra esto y pon tu código
    else:
        print("La tarea no se encontró en la lista.")
def main():
    tareas = [] # Base de datos en memoria

    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Ver Tareas")
        print("2. Agregar Tarea")
        print("3. Eliminar Tarea (Opcional: Reto extra)")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            t = input("Escribe la tarea: ")
            agregar_tarea(tareas, t)
        elif opcion == "3":
            t = input("Escribe la tarea a eliminar: ")
            eliminar_tarea(tareas, t)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

# Punto de arranque
main()