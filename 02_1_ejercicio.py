# Ejercicio 2.1: Códigos de usuario

nombre = input("¿Cuál es tu nombre de usuario?: ")
año_nacimiento_texto = input("¿En qué año naciste?: ")

codigo_nombre = nombre[0:2]
codigo_año = año_nacimiento_texto[-2:]

print(f"Tu código de usuario es: {codigo_nombre}{codigo_año}")


apellido = input("¿Cuál es tu apellido?: ")
año_actual_texto = input("¿En qué año estamos?: ")
codigo_apellido = apellido[0:3]
codigo_año_actual = año_actual_texto[-2:]
print(f"Tu nuevo código de usuario es: {codigo_apellido}{codigo_año_actual}")


nombre_pareja = input ("¿Cuál es el nombre de tu pareja?: ")
edad_pareja_texto = input("¿Cuántos años tiene tu pareja?: ")
codigo_pareja = nombre_pareja[0:2]
codigo_edad_pareja = edad_pareja_texto[-1]
print(f"El código de usuario de tu pareja es: {codigo_pareja}{codigo_edad_pareja}")

