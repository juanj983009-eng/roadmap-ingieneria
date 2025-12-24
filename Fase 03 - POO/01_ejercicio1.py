import random

class Heroe:
    def __init__(self, nombre, poder, salud, experiencia=0):
        self.nombre = nombre
        self.poder = poder
        self.salud = salud
        self.experiencia = experiencia

    def atacar(self):
        if self.esta_vivo():
            self.experiencia += 10
            return f"{self.nombre} ataca con {self.poder}. Experiencia ahora: {self.experiencia}"

    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud < 0:
            self.salud = 0
        return f"{self.nombre} recibe {dano} de daño. Salud ahora: {self.salud}"

    def esta_vivo(self):
        return self.salud > 0

# Zona de uso
heroe1 = Heroe("Aragorn", "Espada", 100)
heroe2 = Heroe("Legolas", "Arco", 80)

while heroe1.esta_vivo() and heroe2.esta_vivo():
    print(heroe1.atacar())
    dano = random.randint(5, 20)
    print(heroe2.recibir_dano(dano))
    if not heroe2.esta_vivo():
        print(f"{heroe2.nombre} ha sido derrotado!")
        break

    print(heroe2.atacar())
    dano = random.randint(5, 20)
    print(heroe1.recibir_dano(dano))
    if not heroe1.esta_vivo():
        print(f"{heroe1.nombre} ha sido derrotado!")
        break

print("¡La batalla ha terminado!")