# --- INTRODUCCIÓN A POO: CLASES Y OBJETOS ---

# 1. DEFINICIÓN DE LA CLASE (El Molde)
# Por convención, las Clases empiezan con Mayúscula (PascalCase)
class Robot:

    # El Constructor (__init__)
    # Esta función se ejecuta AUTOMÁTICAMENTE cuando nace el objeto.
    # Sirve para darle sus valores iniciales.
    def __init__(self, nombre, modelo):
        self.nombre = nombre   # Atributo: Mi nombre es el que me pasaron
        self.modelo = modelo   # Atributo: Mi modelo es el que me pasaron
        self.energia = 100     # Atributo: Todos nacen con 100 de batería
        print(f"🤖 Sistema iniciado: Soy {self.nombre}")

    # Método (Acción)
    # Las funciones dentro de una clase se llaman MÉTODOS.
    def saludar(self):
        print(f"[{self.nombre}]: ¡Hola humanos! Soy modelo {self.modelo}.")

    def trabajar(self):
        if self.energia > 0:
            self.energia -= 10
            print(f"[{self.nombre}]: Trabajando duramente... (Energía: {self.energia})")
        else:
            print(f"[{self.nombre}]: 🪫 Batería baja. No puedo trabajar.")

    def recargar(self):
        self.energia = 100
        print(f"[{self.nombre}]: 🔋 Batería al 100%.")

# --- ZONA DE USO (INSTANCIAS) ---
print("--- FÁBRICA DE ROBOTS ---")

# 2. CREACIÓN DE OBJETOS (Instanciación)
# Fíjate que no pasamos 'self', Python lo pone solo. Solo pasamos nombre y modelo.
r1 = Robot("R2D2", "Astro-Droid")
r2 = Robot("Terminator", "T-800")

# 3. INTERACCIÓN
# Cada uno tiene sus propios datos.
r1.saludar()
r2.saludar()

# Vamos a cansar a R1
r1.trabajar()
r1.trabajar()

# Verificamos que R2 sigue lleno de energía (Son independientes)
print(f"Energía de R1: {r1.energia}")
print(f"Energía de R2: {r2.energia}")