#Calculadora de primaria

print("=== Calculadora de Multiplicación ===")
numero = int(input("Ingrese un número entero: "))

for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
