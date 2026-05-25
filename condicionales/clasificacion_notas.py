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