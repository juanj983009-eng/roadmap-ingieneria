#El Buscador Seguro (uso de excepciones)
frutas = ["manzana", "banana", "cereza", "durazno", "mango", "pera"]

buscar = input("Ingrese el la posición de la fruta que desea buscar (0-5): ")
try:
    indice = int(buscar)
    fruta = frutas[indice]
    print(f"La fruta en la posición {indice} es: {fruta}")
except ValueError:
    print("⛔ Error: Debes ingresar un número entero válido.")
except IndexError:
    print("⛔ Error: Índice fuera de rango. Debe estar entre 0 y 5.")
except Exception as e:
    print(f"⛔ Error desconocido: {e}")
finally:
    print("🔄 Fin de la búsqueda.")


