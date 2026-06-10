# Ejercicio 2: Cajero Automático Bancario

saldo = 1000000
opcion = 0

while opcion != 4:
    print("MENÚ DEL CAJERO")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Saldo actual:", saldo)

    elif opcion == 2:
        deposito = float(input("Ingrese el valor que desea depositar: "))
        saldo += deposito
        print("Saldo depositado correctamente.")

    elif opcion == 3:
        retiro = float(input("Ingrese la cantidad que desea retirar: "))

        if retiro > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= retiro
            print("Retiro realizado correctamente.")

    elif opcion == 4:
        print("Gracias por utilizar el cajero automático.")

    else:
        print("Opción inválida.")