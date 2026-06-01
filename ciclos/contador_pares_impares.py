# Realice un algoritmo que imprima los numeros pares entre 2 y 100

numero = 1

while numero <= 100:
    numero = numero + 1
    if numero % 2 == 0:
        print(numero, "Es un numero par")
    else:
        print(numero,"Es un numero impar")