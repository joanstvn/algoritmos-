# ============================================
# Ejercicio 4 — Cálculo de costo de envío
# ============================================

# Una empresa de mensajería cobra el envío de paquetes
# según su peso.

# Tarifas base:
# - Si el paquete pesa menos de 1 kg:
#   costo de 8.000 pesos.
#
# - Si pesa entre 1 kg y 5 kg:
#   costo de 15.000 pesos.
#
# - Si pesa más de 5 kg:
#   costo de 30.000 pesos.

# Reglas adicionales:
# - Si el envío es internacional,
#   aumentar el valor total en un 40%.
#
# - Si el cliente es premium,
#   aplicar un descuento del 20%.

# El programa debe mostrar:
# - Costo base del envío.
# - Valor adicional o descuento aplicado.
# - Valor final a pagar.

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
