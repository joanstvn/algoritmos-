compra = float(input("Ingrese el valor de la compra: "))
tipo = input("Ingrese el tipo de cliente (VIP o normal): ")

descuento = 0

if compra >= 500000 and tipo == "VIP":
    descuento = 20

elif compra >= 500000 and tipo == "normal":
    descuento = 10

elif compra < 500000 and tipo == "VIP":
    descuento = 5

elif compra < 500000 and tipo == "normal":
    descuento = 0

valor_descuento = compra * descuento / 100
total = compra - valor_descuento

print("Valor de la compra:", compra)
print("Porcentaje de descuento:", descuento, "%")
print("Valor del descuento:", valor_descuento)
print("Valor total a pagar:", total)