# ============================================
# Ejercicio 10 — Clasificación de triángulos
# ============================================

# Desarrolle un programa que solicite
# los tres lados de un triángulo.

# Validaciones:
# Antes de clasificar el triángulo,
# el programa debe verificar lo siguiente:

# - Ningún lado puede ser menor o igual a cero.
#
# - Para que un triángulo exista,
#   la suma de dos lados siempre debe ser
#   mayor que el tercer lado.

# Esto significa que deben cumplirse
# estas tres condiciones:

# - a + b > c
# - a + c > b
# - b + c > a

# Clasificación:

# - Si los tres lados son iguales:
#   “El triángulo es equilátero.”
#
# - Si únicamente dos lados son iguales:
#   “El triángulo es isósceles.”
#
# - Si los tres lados son diferentes:
#   “El triángulo es escaleno.”

# Si no cumple las condiciones:
# “Los valores ingresados no forman
# un triángulo válido.”

a = float(input("Ingrese el lado A: "))
b = float(input("Ingrese el lado B: "))
c = float(input("Ingrese el lado C: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Los valores ingresados no forman un triángulo válido.")

elif a + b <= c or a + c <= b or b + c <= a:
    print("Los valores ingresados no forman un triángulo válido.")

else:

    if a == b and b == c:
        print("El triángulo es equilátero.")

    elif a == b or a == c or b == c:
        print("El triángulo es isósceles.")

    else:
        print("El triángulo es escaleno.")
