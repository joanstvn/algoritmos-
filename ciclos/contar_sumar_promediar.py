# Realizar un algoritmo que solicite un numero entero mientras no se digite el numero 0 
# Contar los numeros ingresados 
# Sumar los numeros ingresados 
# Promediar los numeros ingresados 
# Imprimir la cantidad de numeros ingresados 
# Imprmimr la suma de los numeros ingresados 

# contador: Una variable que cambia de valor con una contante  
# acumulador: Una variable que cambia de valor con un variable 
# promedio: suma de todos los numeros dividido entre la cantidad de numeros

# InicioAlgoritmo

# Definicion de variables:

# numero= 1 
# ContadorNumeros = 0 (contador)
# sumaNumeros = 0  (acumulador)
# promedioNumeros = 0 (variable)

numero= 1
ContadorNumeros = 0 
sumaNumeros = 0 
promedioNumeros = 0 

while numero != 0:
    numero = int(input("Ingrese un numero entero: "))
    ContadorNumeros = ContadorNumeros + 1
    sumaNumeros = sumaNumeros + numero
    if ContadorNumeros > 1:
        ContadorNumeros = ContadorNumeros - 1
promedioNumeros = sumaNumeros / ContadorNumeros

print("cantidad de numeros ingresados: ", (ContadorNumeros))
print("suma de numeros ingresados: ", (sumaNumeros))    
print("promedio de numeros ingresados: ", (promedioNumeros))    


