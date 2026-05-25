respuesta = 0 

respuesta = input("¿Tiene hambre? (si/no): ").lower()

if respuesta == "si":
    print("Ir a comer")
elif respuesta == "no":
    print("No ir a comer")
else:
    print("Respuesta invalida")