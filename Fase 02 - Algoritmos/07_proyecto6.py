#La Mazmorra de Texto (Text Adventure RPG)

mundo = {
    "entrada": {
        "descripcion": "Estás frente a una cueva oscura.",
        "norte": "salon_principal",
        "item": None
    },
    "salon_principal": {
        "descripcion": "Un gran salón con antorchas.",
        "sur": "entrada",
        "este": "tesoreria",
        "item": "espada_oxidada"
    },
    "tesoreria": {
        "descripcion": "¡Brilla mucho! Pero hay un dragón dormido.",
        "oeste": "salon_principal",
        "item": "cofre_oro"
    }
}

def navegacion_actual(ubicacion):
    print("\n" + mundo[ubicacion]["descripcion"])
    if mundo[ubicacion]["item"]:
        print(f"Ves un(a) {mundo[ubicacion]['item']} aquí.")
    return ubicacion

def mover(ubicacion, direccion):
    if direccion in mundo[ubicacion]:
        return mundo[ubicacion][direccion]
    else:
        print("No puedes ir por ahí.")
        return ubicacion

def recoger_item(ubicacion, inventario):
    item = mundo[ubicacion]["item"]
    if item:
        inventario.append(item)
        print(f"Has recogido: {item}")
        mundo[ubicacion]["item"] = None
    else:
        print("No hay nada que recoger aquí.")
    return inventario

def winner(inventario):
    return "cofre_oro" in inventario and "espada_oxidada" in inventario

ubicacion_actual = "entrada"
inventario = []
while True:
    ubicacion_actual = navegacion_actual(ubicacion_actual)
    comando = input("¿Qué quieres hacer? (mover [norte/sur/este/oeste], recoger, inventario, salir): ").strip().lower()

    if comando.startswith("mover"):
        direccion = comando.split()[1]
        ubicacion_actual = mover(ubicacion_actual, direccion)
    elif comando == "recoger":
        inventario = recoger_item(ubicacion_actual, inventario)
    elif comando == "inventario":
        print("Inventario:", inventario)
    elif comando == "salir":
        print("¡Gracias por jugar!")
        break
    else:
        print("Comando no reconocido.")

    if winner(inventario):
        print("¡Felicidades! Has encontrado el cofre de oro y la espada oxidada. ¡Has ganado el juego!")
        break