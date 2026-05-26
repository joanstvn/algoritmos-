edad = 0 

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad <= 4: 
    print("Bebé")
elif edad >= 5 and edad <= 10:
    print("Niño")
elif edad >= 11 and edad <= 15:
    print("Adolecente")
elif edad >= 16 and edad <= 25:
    print("Joven")
elif edad >= 26 and edad <= 75:
    print("Adulto") 
elif edad >= 76 and edad <= 100:
    print("Anciano") 
elif edad >= 101 and edad <= 125:
    print("Longevo") 
elif edad < 0:
    print("Edad no permitida")
elif edad > 125:
    print("Superviviente")  