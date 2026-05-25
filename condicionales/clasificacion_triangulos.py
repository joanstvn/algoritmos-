a = float(input("Ingrese el lado A: "))
b = float(input("Ingrese el lado B: "))
c = float(input("Ingrese el lado C: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Los valores ingresados no forman un triángulo válido.")

elif a + b <= c or a + c <= b or b + c <= a:
    print("Los valores ingresados no forman un triángulo válido.")

else:

    if a == b and b == c:
        print("El triángulo es equilátero.")

    elif a == b or a == c or b == c:
        print("El triángulo es isósceles.")

    else:
        print("El triángulo es escaleno.")