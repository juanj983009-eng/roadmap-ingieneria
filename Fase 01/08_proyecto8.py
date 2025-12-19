#El Cifrador César (Ciberseguridad Básica)
print("--- CIFRADOR CÉSAR ---")

def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            desplazamiento_base = ord('A') if char.isupper() else ord('a')
            char_cifrado = chr((ord(char) - desplazamiento_base + desplazamiento) % 26 + desplazamiento_base)
            resultado += char_cifrado
        else:
            resultado += char
    return resultado
def descifrar_cesar(texto_cifrado, desplazamiento):
    return cifrar_cesar(texto_cifrado, -desplazamiento)
texto = input("Ingrese el texto a cifrar: ")
desplazamiento = int(input("Ingrese el desplazamiento (número de posiciones): "))
texto_cifrado = cifrar_cesar(texto, desplazamiento)
print(f"Texto cifrado: {texto_cifrado}")
texto_descifrado = descifrar_cesar(texto_cifrado, desplazamiento)
print(f"Texto descifrado: {texto_descifrado}")
print("--- FIN DEL CIFRADOR CÉSAR ---")