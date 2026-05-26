# ============================================
# Ejercicio 6 — Impuesto vehicular
# ============================================

# La alcaldía necesita un sistema que calcule
# el valor del impuesto vehicular.

# Tarifas:
# Tipo de vehículo → Valor del impuesto
#
# - Moto → 100.000
# - Carro → 300.000
# - Camión → 800.000

# Reglas adicionales:
# - Si el vehículo es eléctrico,
#   recibe un descuento del 50%.
#
# - Si el propietario tiene multas pendientes,
#   no podrá pagar el impuesto.

# El programa debe mostrar:
# - Tipo de vehículo.
# - Valor base del impuesto.
# - Descuento aplicado.
# - Valor final a pagar.

# Si tiene multas pendientes:
# “No es posible realizar el pago del impuesto
# porque el propietario tiene multas pendientes.”

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
