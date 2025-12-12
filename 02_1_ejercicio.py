nombre = input("¿Cuál es tu nombre de usuario?: ")
año_nacimiento_texto = input("¿En qué año naciste?: ")

codigo_nombre = nombre[0:2]
codigo_año = año_nacimiento_texto[-2:]

print(f"Tu código de usuario es: {codigo_nombre}{codigo_año}")


apellido = input("¿Cuál es tu apellido?: ")
año_actual_texto = input("¿En qué año estamos?: ")
codigo_apellido = apellido[0:3]
año_actual_numero = int(año_actual_texto)
codigo_año_actual = str(año_actual_numero)[-2:]
print(f"Tu nuevo código de usuario es: {codigo_apellido}{codigo_año_actual}")

