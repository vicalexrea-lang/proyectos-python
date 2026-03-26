# Tipos de datos en Python
nombre = "Victor"        # str (texto)
edad = 17                # int (número entero)
altura = 1.75            # float (número decimal)
estudiante = True        # bool (verdadero o falso)

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(estudiante))
# Conversión de tipos
edad_texto = str(edad)
altura_entera = int(altura)
numero_texto = float("3.14")

print(edad_texto, type(edad_texto))
print(altura_entera, type(altura_entera))
print(numero_texto, type(numero_texto))

# f-strings: la forma más limpia de combinar texto y variables
print(f"Me llamo {nombre}, tengo {edad} años y mido {altura}m")