puntaje = int(input("Ingrese el puntaje: "))
entrevista = input("¿Aprobó la entrevista? (si o no): ")
sanciones = input("¿Tiene sanciones disciplinarias? (si o no): ")

if sanciones == "si":
    print("Aspirante rechazado.")

elif puntaje >= 350 and entrevista == "si":

    print("Aspirante admitido.")

    if puntaje > 500:
        print("Beca completa.")

    elif puntaje > 450:
        print("Beca parcial.")

else:
    print("Aspirante rechazado.")