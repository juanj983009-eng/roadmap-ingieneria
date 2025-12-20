def ordenamiento_burbuja(lista):
    n = len(lista)
    # Bucle 1: Las "pasadas" necesarias
    for i in range(n):
        # Bucle 2: La comparación de parejas
        for j in range(0, n - i - 1):
            # Si el actual es MAYOR que el siguiente...
            if lista[j] < lista[j + 1]:
                # ... los intercambiamos (Swap)
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [64, 34, 25, 12, 22, 11, 90]
print("Ordenado:", ordenamiento_burbuja(numeros))# Algoritmo de Ordenamiento Burbuja