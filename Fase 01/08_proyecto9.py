#Agenda de Contactos (CRUD Completo)
nombres = ["juan", "ana"]
telefonos = ["123456789", "987654321"]
while True:
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Ver contactos")
    print("2. Agregar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        print("\n--- LISTA DE CONTACTOS ---")
        for i in range(len(nombres)):
            print(f"{i + 1}. {nombres[i]} - {telefonos[i]}")
    elif opcion == '2':
        nuevo_nombre = input("Ingrese el nombre del nuevo contacto: ")
        nuevo_telefono = input("Ingrese el teléfono del nuevo contacto: ")
        nombres.append(nuevo_nombre)
        telefonos.append(nuevo_telefono)
        print(f"Contacto '{nuevo_nombre}' agregado exitosamente.")
    elif opcion == '3':
        indice = int(input("Ingrese el número del contacto a actualizar: ")) - 1
        if 0 <= indice < len(nombres):
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            nombres[indice] = nuevo_nombre
            telefonos[indice] = nuevo_telefono
            print(f"Contacto actualizado a '{nuevo_nombre}'.")
        else:
            print("Número de contacto inválido.")
    elif opcion == '4':
        indice = int(input("Ingrese el número del contacto a eliminar: ")) - 1
        if 0 <= indice < len(nombres):
            eliminado_nombre = nombres.pop(indice)
            telefonos.pop(indice)
            print(f"Contacto '{eliminado_nombre}' eliminado exitosamente.")
        else:
            print("Número de contacto inválido.")
    elif opcion == '5':
        print("Saliendo de la agenda de contactos.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")