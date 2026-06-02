Algoritmo contadores
	Definir numeross Como 	Entero
	Definir contador_positivo Como Entero
	Definir contador_negativo Como Entero
	
	Escribir "Ingrese un numero: "
	Leer numeross
	
	Mientras numeross <> 0 Hacer
		
		Si numeross < 0 Entonces
			contador_negativo = contador_negativo + 1
		Sino 
			contador_positivo = contador_positivo + 1
		FinSi
		
		Escribir "Ingrese un numero: "
		Leer numeross
		
	FinMientras
	
	
	Escribir "Cantidad de numeros positivos: ", contador_positivo
	Escribir "Cantiad de numeros negativos: ", contador_negativo
FinAlgoritmo
