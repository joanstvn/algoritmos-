tipo = input("Ingrese el tipo de vehículo (moto, carro o camion): ")
electrico = input("¿El vehículo es eléctrico? (si o no): ")
multas = input("¿Tiene multas pendientes? (si o no): ")

impuesto = 0

if tipo == "moto":
    impuesto = 100000

elif tipo == "carro":
    impuesto = 300000

elif tipo == "camion":
    impuesto = 800000

if multas == "si":
    print("No es posible realizar el pago del impuesto porque el propietario tiene multas pendientes.")

else:
    descuento = 0

    if electrico == "si":
        descuento = impuesto * 0.50

    total = impuesto - descuento

    print("Tipo de vehículo:", tipo)
    print("Valor base del impuesto:", impuesto)
    print("Descuento aplicado:", descuento)
    print("Valor final a pagar:", total)