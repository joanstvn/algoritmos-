# Ejercicio 1: Evaluación de Solicitud de Crédito

nombre = input("Ingrese el nombre completo del cliente: ")
documento = input("Ingrese el documento de identidad: ")
ingreso_mensual = float(input("Ingrese ingreso mensual del cliente: "))

print("\nNombre del cliente:", nombre)
print("Número de documento:", documento)
print("Ingreso mensual:", ingreso_mensual)

if ingreso_mensual >= 2000000:
    print("Estado de la solicitud: APROBADA")
else:
    print("Estado de la solicitud: RECHAZADA")