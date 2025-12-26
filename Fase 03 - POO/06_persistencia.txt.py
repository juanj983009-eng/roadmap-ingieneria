# --- PERSISTENCIA DE DATOS (I/O) ---
import datetime

class Diario:
    def __init__(self, nombre_archivo):
        self.archivo = nombre_archivo

    def escribir(self, texto):
        # Obtener fecha actual
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 'a' = Append (Agregar al final)
        # encoding='utf-8' = Para que acepte tildes y ñ
        with open(self.archivo, 'a', encoding='utf-8') as f:
            f.write(f"[{fecha}] {texto}\n") # \n es salto de línea
        print("✅ Guardado en disco.")

    def leer(self):
        print(f"\n--- LEYENDO {self.archivo} ---")
        try:
            # 'r' = Read (Leer)
            with open(self.archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                print(contenido)
        except FileNotFoundError:
            print("📭 El archivo aún no existe. ¡Escribe algo primero!")

# --- USO ---
mi_diario = Diario("bitacora_capitan.txt")

# Escribimos algo
mi_diario.escribir("Día 1: He aprendido a guardar datos.")
mi_diario.escribir("Día 2: Python es más poderoso de lo que creía.")

# Leemos lo que está en el disco
mi_diario.leer()