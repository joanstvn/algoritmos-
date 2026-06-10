# Realizar un algoritmo que solicite 10 numeros enteros. emplear el ciclo for 
# Contar los ceros ingresados 
# Contar los numeros negativos
# Contar los numeros positivos
# Sumar los numeros ingresados
# Promediar los numeros ingresados 
# Imprimir la cantidad de numeros positivos ingresados 
# Imprmimr la suma de los numeros ingresados 
# Imprimir la el promedio de los numero ingresados 


numeros = 0 
contadorCeros = 0
contadorPositivos = 0
contadorNegativos = 0
sumaNumeros = 0 
promedioNumeros = 0

for i in range(1, 11):
    numero = int(input("Ingrese un numero: "))
    if numero < 0: 
        contadorNegativos = contadorNegativos + 1
    elif numero > 0: 
        contadorPositivos = contadorPositivos + 1
    else:
        contadorCeros = contadorCeros + 1
    sumaNumeros = sumaNumeros + numero
promedioNumeros = sumaNumeros / 10
print(f"cantiad de ceros: {contadorCeros} \n cantidad de numeros negativos: {contadorNegativos} \n cantidad postivos: {contadorPositivos} \n suna de los numeros: {sumaNumeros} \n promedio de los numeros: {promedioNumeros}" )

