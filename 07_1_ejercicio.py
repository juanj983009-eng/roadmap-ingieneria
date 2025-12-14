#Calculadora básica

def sumar(a, b):
    c = a + b
    return c

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")
if operacion == "+":
    print(f"Resultado: {sumar(n1, n2)}")
elif operacion == "-":
    print(f"Resultado: {restar(n1, n2)}")
elif operacion == "*":
    print(f"Resultado: {multiplicar(n1, n2)}")
elif operacion == "/":
    print(f"Resultado: {dividir(n1, n2)}")
else:
    print("Operación no válida.")