# ============================================
# Ejercicio 7 — Validación de acceso a un sistema
# ============================================

# Una empresa desea validar el acceso
# de sus empleados a un sistema interno.

# El usuario podrá ingresar únicamente si:
# - La cuenta está activa.
# - La contraseña es correcta.
#
# Además, debe cumplir al menos una
# de estas condiciones:
# - Ser administrador.
# - Tener permiso especial.

# El programa debe mostrar:
# - “Acceso permitido.”
# o
# - “Acceso denegado.”

cuenta = input("¿La cuenta está activa? (si o no): ")
contrasena = input("¿La contraseña es correcta? (si o no): ")
admin = input("¿Es administrador? (si o no): ")
permiso = input("¿Tiene permiso especial? (si o no): ")

if cuenta == "si" and contrasena == "si":

    if admin == "si" or permiso == "si":
        print("Acceso permitido.")

    else:
        print("Acceso denegado.")

else:
    print("Acceso denegado.")
