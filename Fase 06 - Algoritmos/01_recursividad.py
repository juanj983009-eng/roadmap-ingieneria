def factorial_recursivo(n):
    print(f"🔄 Entrando a la dimensión del {n}")

    # 1. EL FRENO DE EMERGENCIA (Caso Base)
    # Si no ponemos esto, la función se llamará infinitamente hasta que Python explote.
    if n == 1:
        print("🛑 ¡Llegamos al final! Devolvemos 1.")
        return 1

    # 2. LA LLAMADA RECURSIVA (Inception)
    # La función se llama a sí misma, pero con un problema más pequeño (n-1)
    resultado = n * factorial_recursivo(n - 1)

    print(f"✅ Resolviendo: {n} * factorial({n-1}) = {resultado}")
    return resultado

# --- ZONA DE PRUEBA ---
numero = 5
print(f"Calculando el factorial de {numero}...\n")

total = factorial_recursivo(numero)

print(f"\n🏆 El Factorial de {numero} es: {total}")