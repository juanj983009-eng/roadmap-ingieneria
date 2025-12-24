#Sistema de Login

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def login(self, username, password):
        if self.username == username and self.__password == password:
            return f"✅ {self.username} ha iniciado sesión correctamente."
        else:
            return "❌ Credenciales incorrectas."

    def cambiar_password(self, antigua_password, nueva_password):
        if self.__password == antigua_password:
            self.__password = nueva_password
            return "✅ Contraseña cambiada exitosamente."
        else:
            return "❌ La contraseña antigua es incorrecta."

# --- ZONA DE PRUEBA ---
usuario1 = Usuario("juan123", "miSecreta!")
print(usuario1.login("juan123", "miSecreta!"))  # Correcto
print(usuario1.login("juan123", "otraCosa"))    # Incorrecto
print(usuario1.cambiar_password("miSecreta!", "nuevaPassword"))  # Cambio exitoso
print(usuario1.login("juan123", "nuevaPassword"))  # Login con nueva contraseña