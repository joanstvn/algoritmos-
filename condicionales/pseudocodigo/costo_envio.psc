Proceso costo_envio
	Definir peso, valor_base, aumento_valor, descuento_aplicado, valor_final Como Real
	Definir tipo_envio, tipo_cliente Como Caracter
	
	Escribir "Ingrese el peso: "
	Leer peso
	
	Escribir "Tipo de cliente: "
	Leer tipo_cliente
	
	Escribir "Tipo de envio: "
	Leer tipo_envio
	
	Si peso < 1 Entonces
		valor_base <- 8000
	FinSi
	Si peso >= 1 Y peso <= 5 Entonces
		valor_base <- 15000
	FinSi
	Si peso > 5 Entonces
		valor_base <- 30000
	FinSi
	
	Escribir "Costo base del envio: ", valor_base
	
	Si tipo_envio = "INTERNACIONAL" Entonces
		aumento_valor <- (valor_base * 0.40) + valor_base
		valor_final <- valor_base - aumento_valor
		Escribir "Valor adicional aplicado: ", aumento_valor
		Escribir "Valor final a pagar: ", valor_final
	Sino 
		Escribir "No aplica aumento adicional."
	FinSi
	
	Si tipo_cliente = "PREMIUM" Entonces
		descuento_aplicado <- (valor_base * 0.20)
		valor_final <- valor_base - descuento_aplicado
		Escribir "Valor de descuento aplicado: ", descuento_aplicado
		Escribir "Valor final a pagar: ", valor_final
	SiNo
		Escribir "No aplica descuento"
	FinSi
	
FinProceso
