usuario = 0 
contraseña = 0

usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

if usuario == "admin" and contraseña == "sena2026":
    print("Bienvenido")
else:
    print("Usuario y/o password incorrectos")
