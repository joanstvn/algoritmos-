# Realizar un algoritmo que solicite 10 temperaturas y luego calcule y muestre:
# promedio de temperaturas positivas, promedio de temperaturas negativas 
# promedio de todas las temperaturas
# cantidad de temperaturas en cero 
# cantidad de temperaturas entre 30 y 50 
# cantidad de temperaturas entre -3 y -11
# temperatura maxima

# 10:00 a.m dilopezz@sena.edu.co

temperatura = 0
sumaTamparaturasPositivas = 0
sumaTamparaturasNagativas = 0
sumaTodasTamparaturas = 0
contadorTamparaturasPositivas = 0
contadorTamparaturasNagativas = 0
contadorTamparaturasCeros = 0
contadorTamparaturas30a50 = 0
contadorTamparaturasMenos3Menos11 = 0
tamparaturaMaxima = 0

for i in range(1, 11):
    temperatura = float(input("Ingrese una temperatura: "))

    sumaTodasTamparaturas = sumaTodasTamparaturas + temperatura

    if i == 1:
        tamparaturaMaxima = temperatura

    if temperatura > tamparaturaMaxima:
        tamparaturaMaxima = temperatura

    if temperatura > 0:
        contadorTamparaturasPositivas = contadorTamparaturasPositivas + 1
        sumaTamparaturasPositivas = sumaTamparaturasPositivas + temperatura

    elif temperatura < 0:
        contadorTamparaturasNagativas = contadorTamparaturasNagativas + 1
        sumaTamparaturasNagativas = sumaTamparaturasNagativas + temperatura

    else:
        contadorTamparaturasCeros = contadorTamparaturasCeros + 1

    if temperatura >= 30 and temperatura <= 50:
        contadorTamparaturas30a50 = contadorTamparaturas30a50 + 1

    if temperatura >= -11 and temperatura <= -3:
        contadorTamparaturasMenos3Menos11 = contadorTamparaturasMenos3Menos11 + 1

if contadorTamparaturasPositivas > 0:
    promedioTamparaturasPositivas = sumaTamparaturasPositivas / contadorTamparaturasPositivas
else:
    promedioTamparaturasPositivas = 0

if contadorTamparaturasNagativas > 0:
    promedioTamparaturasNagativas = sumaTamparaturasNagativas / contadorTamparaturasNagativas
else:
    promedioTamparaturasNagativas = 0

promedioTodasTamparaturas = sumaTodasTamparaturas / 10

print("Promedio temperaturas positivas:", promedioTamparaturasPositivas)
print("Promedio temperaturas negativas:", promedioTamparaturasNagativas)
print("Promedio de todas las temperaturas:", promedioTodasTamparaturas)
print("Cantidad de temperaturas en cero:", contadorTamparaturasCeros)
print("Cantidad de temperaturas entre 30 y 50:", contadorTamparaturas30a50)
print("Cantidad de temperaturas entre -3 y -11:", contadorTamparaturasMenos3Menos11)
print("Temperatura maxima:", tamparaturaMaxima)