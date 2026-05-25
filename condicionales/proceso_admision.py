# ============================================
# Ejercicio 9 — Proceso de admisión universitaria
# ============================================

# Una universidad desea automatizar
# el proceso de admisión de estudiantes.

# Requisitos de admisión:

# El aspirante será admitido únicamente si:
# - Tiene un puntaje igual o superior a 350.
# - Aprobó la entrevista.

# Reglas adicionales:
# - Si el puntaje es mayor a 450,
#   recibe beca parcial.
#
# - Si el puntaje es mayor a 500,
#   recibe beca completa.
#
# - Si tiene sanciones disciplinarias,
#   será rechazado automáticamente.

# El programa debe mostrar:
# - “Aspirante admitido.”
# - “Aspirante rechazado.”
# - Tipo de beca obtenida, si aplica.

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
