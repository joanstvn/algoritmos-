# ============================================
# Ejercicio 2 — Clasificación de notas
# ============================================

# Desarrolle un programa que solicite la nota definitiva
# de un estudiante en una materia.

# Reglas:
# - Si la nota está entre 4.5 y 5.0:
#   “Excelente desempeño.”
#
# - Si la nota está entre 3.5 y 4.4:
#   “El estudiante aprobó la materia.”
#
# - Si la nota está entre 2.0 y 3.4:
#   “El estudiante debe realizar recuperación.”
#
# - Si la nota es menor a 2.0:
#   “El estudiante reprobó la materia.”

# Validaciones:
# - Si la nota es menor que 0 o mayor que 5:
#   “Error: nota inválida.”

nota_definitiva = 0
entrada = 0 

entrada = input("Ingrese la nota definitiva del estudiante: ")
if "," in entrada:
    entrada = entrada.replace(",", ".")

nota = float(entrada)

if nota >= 4.5 and nota <= 5.0:
    print("Excelente desempeño.")

elif nota >= 3.5 and nota <= 4.4:
    print("El estudiante aprobó la materia.")

elif nota >= 2.0 and nota <= 3.4:
    print("El estudiante debe realizar recuperación.")

elif nota < 2.0:
    print("El estudiante reprobó la materia.")

else:
    print("Ingrese una nota valida")
