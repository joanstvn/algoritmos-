edad = int(input("Ingrese la edad: "))
habitaciones = input("¿Hay habitaciones disponibles? (si o no): ")
noches = int(input("Ingrese la cantidad de noches: "))
temporada = input("¿Es temporada alta? (si o no): ")

valor_noche = 100000
total = noches * valor_noche

if edad >= 18 and habitaciones == "si":

    if noches > 5:
        descuento = total * 0.15
        total = total - descuento

    if temporada == "si":
        aumento = total * 0.25
        total = total + aumento

    print("Reserva realizada exitosamente.")
    print("Cantidad de noches:", noches)
    print("Valor total a pagar:", total)

else:
    print("No es posible realizar la reserva.")