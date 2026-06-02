contador_positivo = 0 
contador_negativo = 0

numeros = int(input("Ingrese un numero: "))

while numeros != 0:
    if numeros < 0:
        contador_negativo = contador_negativo + 1
    else:
        contador_positivo = contador_positivo + 1
    numeros = int(input("Ingrese un numero: "))

print("Cantidad de numeros positivos: ", (contador_positivo))
print("Cantiad de numeros negativos: ", (contador_negativo))