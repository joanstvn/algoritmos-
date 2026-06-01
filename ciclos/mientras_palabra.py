#Realice un algoritmo que lea una palabra mientras no sea "fin"

palabra = ""


while palabra != "fin":
    palabra = input("Digite una palabra: ")




#Realice un algoritmo que lea una palabra mientras no sea "fin" con un contador 

contador = 0
palabra = ""


while palabra != "fin":
    palabra = input("Digite una palabra: ")
    contador = contador + 1

print("La cantidad de palabras digitadas es: ", contador)