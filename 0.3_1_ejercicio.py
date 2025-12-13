agrega_tu_nota = input("¿Cuanto fue tu nota del curso?:")
agrega_tu_nota_float = float(agrega_tu_nota)

if agrega_tu_nota_float <= 20.0 and agrega_tu_nota_float >= 17.0:
    print("¡Felicitaciones! Eres excelente.")
elif agrega_tu_nota_float < 17.0 and agrega_tu_nota_float >= 11.0:
    print("¡Bien hecho! Has aprobado.")
elif agrega_tu_nota_float < 0 or agrega_tu_nota_float > 20:
    print("Error: La nota ingresada no es válida. Debe estar entre 0 y 20.")
else:
    print("Lo siento, no has aprobado el curso. ¡Sigue intentando!")