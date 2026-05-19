Proceso algoritmo_edades
	Definir edad Como Entero
	
	Escribir "Ingrese su edad"
	Leer edad
	
	Si edad >= 0 Y edad <= 4 Entonces
		Escribir "Bebé"
	Sino si edad >= 5 Y edad <= 10 Entonces
			Escribir "Niño"
		Sino si edad >= 11 Y edad <= 15 Entonces
				Escribir "Adolecente"
			Sino si edad >= 16 Y edad <= 25 Entonces
					Escribir "Joven"
				Sino si edad >= 26 Y edad <= 75 Entonces
						Escribir "Adulto"
					Sino si edad >= 75 Y edad <= 100 Entonces
							Escribir "Anciano"
						Sino si edad >= 101 Y edad <= 125 Entonces
								Escribir "Longevo"
							Sino si edad < 0 Entonces
									Escribir "Edad no permitida"
								Sino si edad > 125 Entonces
										Escribir "Superviviente"
									FinSi
								Finsi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	
FinProceso
