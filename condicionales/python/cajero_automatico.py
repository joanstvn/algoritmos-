# ============================================
# Ejercicio 5 — Cajero automático
# ============================================

# Desarrolle un programa que simule el funcionamiento
# básico de un cajero automático.

# Reglas:
# - El PIN correcto del usuario es: 1234.
#
# - El retiro máximo permitido es
#   de 1.000.000 de pesos.
#
# - El sistema debe verificar que el usuario
#   tenga saldo suficiente para realizar el retiro.

# El programa debe solicitar:
# - PIN.
# - Saldo disponible.
# - Valor que desea retirar.

# El programa debe mostrar:

# Si todo es correcto:
# - “Retiro realizado exitosamente.”
# - Saldo restante.

# En caso de error:
# - “PIN incorrecto.”
# - “Saldo insuficiente.”
# - “El valor supera el límite permitido.”

pin = int(input("Ingrese el PIN: "))
saldo = float(input("Ingrese el saldo disponible: "))
retiro = float(input("Ingrese el valor a retirar: "))

if pin != 1234:
    print("PIN incorrecto.")

elif retiro > 1000000:
    print("El valor supera el límite permitido.")

elif retiro > saldo:
    print("Saldo insuficiente.")

else:
    saldo = saldo - retiro

    print("Retiro realizado exitosamente.")
    print("Saldo restante:", saldo)
