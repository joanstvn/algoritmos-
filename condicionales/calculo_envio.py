peso = float(input("Ingrese el peso del paquete: "))
internacional = input("¿El envío es internacional? (si o no): ")
premium = input("¿El cliente es premium? (si o no): ")

costo = 0

if peso < 1:
    costo = 8000

elif peso >= 1 and peso <= 5:
    costo = 15000

elif peso > 5:
    costo = 30000

valor_extra = 0
valor_descuento = 0

if internacional == "si":
    valor_extra = costo * 0.40
    costo = costo + valor_extra

if premium == "si":
    valor_descuento = costo * 0.20
    costo = costo - valor_descuento

print("Costo base del envío:", costo)

if internacional == "si":
    print("Valor adicional:", valor_extra)

if premium == "si":
    print("Descuento aplicado:", valor_descuento)

print("Valor final a pagar:", costo)