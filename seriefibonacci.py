# Ejercicio 3: Proyección de crecimiento de clientes

n = 0
valor1 = 0
valor2 = 1
valor3 = 0 

while n <= 0:
    n = int(input("Ingrese la cantidad de términos: "))

    if n <= 0:
        print("Valor no válido. Debe ser mayor a cero.")

for i in range(1, n + 1):
    print(valor1, end=" ")

    valor3 = valor1 + valor2
    valor1 = valor2
    valor2 = valor3