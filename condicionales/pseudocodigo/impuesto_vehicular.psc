Proceso impuesto_vehicular
	Definir tipo_vehiculo, tipo_electrico, multas Como Caracter
	Definir descuento, valor_final, valor_impuesto Como Real
	
	Escribir "Ingrese el tipo de vehiculo"
	Leer tipo_vehiculo
	
	Escribir "Ingrese si el vehiculo es electrico (si/no)"
	Leer tipo_electrico
	
	Escribir "Ingrese si tiene multas pendientes (si/no)"
	Leer multas
	
	Escribir "El tipo de vehiculo es: ", tipo_vehiculo
	
	Si tipo_vehiculo = "Moto" Entonces
		valor_impuesto <- 100000
	FinSi
	Si tipo_vehiculo = "Carro" Entonces
		valor_impuesto <- 300000
	FinSi
	Si tipo_vehiculo = "Camión" Entonces
		valor_impuesto <- 800000
	FinSi
	
	Escribir "El valor base del impuesto es: ", valor_impuesto
	
	Si multas = "si" Entonces
		Escribir "No es posible realizar el pago del impuesto porque el propietario tiene multas pendientes."
	FinSi
	
	Si tipo_electrico = "si" Entonces
		descuento <- (valor_impuesto * 0.50) 
		valor_final <- valor_impuesto - descuento
		Escribir "El descuento aplicado es de: ", descuento
		Escribir "El valor final a pagar es de: ", valor_final
	FinSi	
FinProceso
