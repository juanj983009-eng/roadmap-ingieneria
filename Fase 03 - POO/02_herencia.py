# --- HERENCIA EN POO ---

# 1. CLASE PADRE (La Base)
class Personaje:
    def __init__(self, nombre, hp):
        self.nombre = nombre
        self.hp = hp
        self.vivo = True

    def info(self):
        print(f"[{self.nombre}] HP: {self.hp} | Estado: {'Vivo' if self.vivo else 'Muerto'}")

    def morir(self):
        self.vivo = False
        print(f"💀 {self.nombre} ha muerto.")

# 2. CLASE HIJA 1 (Guerrero)
# Hereda todo lo de 'Personaje'
class Guerrero(Personaje):
    def __init__(self, nombre, hp, fuerza):
        # super().__init__ llama al constructor del Padre para que configure el nombre y hp
        super().__init__(nombre, hp)
        self.fuerza = fuerza # Atributo exclusivo de Guerrero

    # Método exclusivo
    def ataque_espada(self):
        print(f"⚔️ {self.nombre} ataca con la espada! (Daño: {self.fuerza})")

# 3. CLASE HIJA 2 (Mago)
class Mago(Personaje):
    def __init__(self, nombre, hp, mana):
        super().__init__(nombre, hp)
        self.mana = mana

    def lanzar_hechizo(self):
        if self.mana >= 10:
            self.mana -= 10
            print(f"🔥 {self.nombre} lanza Bola de Fuego! (Mana restante: {self.mana})")
        else:
            print(f"💧 {self.nombre} no tiene suficiente mana.")

# --- ZONA DE JUEGO ---
print("--- COMIENZA LA AVENTURA ---")

# Instanciamos las clases hijas
guts = Guerrero("Guts", 200, 50)
gandalf = Mago("Gandalf", 100, 50)

# Usamos métodos heredados (info)
guts.info()
gandalf.info()

# Usamos métodos propios
guts.ataque_espada()
gandalf.lanzar_hechizo()
gandalf.lanzar_hechizo()

# Probamos herencia de métodos base
guts.morir()
guts.info()