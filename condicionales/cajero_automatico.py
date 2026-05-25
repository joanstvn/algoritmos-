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