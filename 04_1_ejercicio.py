# Ejercicio 4.1: Elegibilidad para beca universitaria

promedio_del_estudiante = float(input("Ingrese el promedio del estudiante: "))
if promedio_del_estudiante < 0.0 or promedio_del_estudiante > 20.0:
    print("Error: El promedio ingresado no es válido. Debe estar entre 0.0 y 20.0.")
    exit()
km_de_su_casa_a_la_universidad = float(input("Ingrese los kilómetros de su casa a la universidad: "))
ingreso_mensual_de_su_familia = float(input("Ingrese el ingreso mensual de su familia: "))
if promedio_del_estudiante >= 15.0 and (km_de_su_casa_a_la_universidad > 10 or ingreso_mensual_de_su_familia < 1000.0):
    print("El estudiante es elegible para la beca.")
else:
    print("El estudiante no es elegible para la beca.")
