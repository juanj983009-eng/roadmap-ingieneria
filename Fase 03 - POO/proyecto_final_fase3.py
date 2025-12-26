import json
import os # Para verificar si existe el archivo

ARCHIVO = "gremio.json"

# --- 1. CLASES (MODELOS) ---
class Heroe:
    def __init__(self, nombre, nivel, clase):
        self.nombre = nombre
        self.nivel = nivel
        self.clase = clase # "Guerrero" o "Mago"

    def detalle(self):
        return f"{self.nombre} (Nvl {self.nivel}) - Clase: {self.clase}"

    # TAREA: Necesitamos convertir el Objeto a Diccionario para poder guardarlo en JSON
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "nivel": self.nivel,
            "clase": self.clase
            # Si agregas mana o fuerza en las hijas, añádelos aquí o sobrescribe este método
        }

class Guerrero(Heroe):
    def __init__(self, nombre, nivel, fuerza):
        super().__init__(nombre, nivel, "Guerrero")
        self.fuerza = fuerza

    # Sobrescribimos para añadir la fuerza al diccionario
    def to_dict(self):
        data = super().to_dict() # Trae lo básico
        data["fuerza"] = self.fuerza
        return data

class Mago(Heroe):
    def __init__(self, nombre, nivel, mana):
        super().__init__(nombre, nivel, "Mago")
        self.mana = mana

    def to_dict(self):
        data = super().to_dict()
        data["mana"] = self.mana
        return data

# --- 2. GESTOR DE DATOS (CONTROLADOR) ---
class GestorGremio:
    def __init__(self):
        self.lista_heroes = []
        self.cargar_datos() # Al nacer, el gestor intenta leer el disco

    def guardar_datos(self):
        # Convertimos la lista de OBJETOS a lista de DICCIONARIOS
        datos_para_json = []
        for h in self.lista_heroes:
            datos_para_json.append(h.to_dict())

        try:
            with open(ARCHIVO, 'w') as f:
                json.dump(datos_para_json, f, indent=4)
            print("💾 Gremio guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar: {e}")

    def cargar_datos(self):
        if not os.path.exists(ARCHIVO):
            return # Si no existe, no hacemos nada (lista vacía)

        try:
            with open(ARCHIVO, 'r') as f:
                datos_json = json.load(f)

            # RECONSTRUCCIÓN: De Diccionario a Objeto
            self.lista_heroes = []
            for d in datos_json:
                if d["clase"] == "Guerrero":
                    nuevo = Guerrero(d["nombre"], d["nivel"], d["fuerza"])
                elif d["clase"] == "Mago":
                    nuevo = Mago(d["nombre"], d["nivel"], d["mana"])
                self.lista_heroes.append(nuevo)

        except Exception as e:
            print(f"Error al cargar: {e}")

    def agregar_heroe(self, heroe):
        self.lista_heroes.append(heroe)
        self.guardar_datos() # Guardado automático

    def listar_heroes(self):
        print("\n--- MIEMBROS DEL GREMIO ---")
        for h in self.lista_heroes:
            print(h.detalle())

# --- 3. INTERFAZ (VISTA) ---
def main():
    gestor = GestorGremio()

    while True:
        print("\n1. Reclutar Guerrero")
        print("2. Reclutar Mago")
        print("3. Ver Gremio")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            nom = input("Nombre: ")
            fuerza = int(input("Fuerza (1-100): "))
            # TAREA: Crear objeto Guerrero y pasarlo al gestor
            g = Guerrero(nom, 1, fuerza)
            gestor.agregar_heroe(g)

        elif opcion == "2":
            nom = input("Nombre: ")
            mana = int(input("Mana (10-100): "))
            # TAREA: Crear objeto Mago y pasarlo al gestor
            m = Mago(nom, 1, mana)
            gestor.agregar_heroe(m)
        elif opcion == "3":
            gestor.listar_heroes()

        elif opcion == "4":
            print("Cerrando sistema...")
            break

# Ejecutar
if __name__ == "__main__":
    main()