# Ejercicio 3.1: Evaluación de notas

agrega_tu_nota = float(input("¿Cuanto fue tu nota del curso?:"))

if agrega_tu_nota <= 20.0 and agrega_tu_nota >= 17.0:
    print("¡Felicitaciones! Eres excelente.")
elif agrega_tu_nota  < 17.0 and agrega_tu_nota >= 11.0:
    print("¡Bien hecho! Has aprobado.")
elif agrega_tu_nota < 0 or agrega_tu_nota > 20:
    print("Error: La nota ingresada no es válida. Debe estar entre 0 y 20.")
else:
    print("Lo siento, no has aprobado el curso. ¡Sigue intentando!")