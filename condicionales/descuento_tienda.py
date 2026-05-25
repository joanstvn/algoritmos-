# ============================================
# Ejercicio 3 — Descuento en una tienda
# ============================================

# Una tienda desea calcular el descuento que recibirá
# un cliente según el valor de la compra y el tipo de cliente.

# Reglas:

# Compras de 500.000 pesos o más:
# - Cliente VIP → descuento del 20%.
# - Cliente normal → descuento del 10%.

# Compras menores a 500.000 pesos:
# - Cliente VIP → descuento del 5%.
# - Cliente normal → no recibe descuento.

# El programa debe mostrar:
# - Valor de la compra.
# - Porcentaje de descuento aplicado.
# - Valor del descuento.
# - Valor total a pagar.

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
