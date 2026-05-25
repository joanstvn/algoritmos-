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