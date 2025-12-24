# --- POLIMORFISMO EN ACCIÓN ---

# 1. CLASE PADRE
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    # Método genérico (por si alguien olvida definir el suyo)
    def atacar(self):
        print(f"😐 {self.nombre} no sabe cómo atacar.")

# 2. CLASES HIJAS (SOBRESCRIBEN EL MÉTODO)
class Guerrero(Personaje):
    def atacar(self):
        print(f"⚔️ {self.nombre} aplasta con su martillo!")

class Mago(Personaje):
    def atacar(self):
        print(f"🔥 {self.nombre} lanza una bola de fuego!")

class Arquero(Personaje):
    def atacar(self):
        print(f"🏹 {self.nombre} dispara una flecha precisa!")

class Monstruo(Personaje):
    def atacar(self):
        print(f"👹 {self.nombre} ataca con un rugido aterrador!")

class Hechizero(Personaje):
    def atacar(self):
        print(f"🔮 {self.nombre} activa su dominio!")

# --- ZONA DE PRUEBA ---

# Creamos un ejército mixto (Lista de Objetos)
ejercito = [
    Guerrero("Thor"),
    Mago("Merlín"),
    Arquero("Legolas"),
    Guerrero("Hulk"),  # Otro guerrero
    Personaje("Aldeano"), # Uno genérico
    Monstruo("Goblin"),
    Hechizero("Gojo Satoru")
]

print("--- ¡INICIA LA BATALLA! ---")

# EL PODER DEL POLIMORFISMO
# Tratamos a todos igual, pero cada uno actúa diferente.
for soldado in ejercito:
    soldado.atacar()
    # Fíjate: No usamos 'if', solo llamamos a atacar()