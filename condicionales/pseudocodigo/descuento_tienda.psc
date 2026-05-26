Proceso descuento_tienda
	
	Definir valor_compra, porcentaje_descuento, valor_descuento, valor_totalpagar Como Real
	Definir tipo_cliente Como Caracter
	
	valor_compra <- 0
	tipo_cliente <- ""
	porcentaje_descuento <- 0
	valor_descuento <- 0
	valor_totalpagar <- 0
	
	Escribir "Ingrese el valor de la compra: "
	Leer valor_compra
	
	Escribir "Ingrese el tipo de cliente: "
	Leer tipo_cliente
	
	Si valor_compra >= 500000 Y tipo_cliente = "VIP" Entonces
		porcentaje_descuento <- 0.20
	Sino 
		porcentaje_descuento <- 0.10
	Finsi
	
	Si valor_compra <= 500000 Y tipo_cliente = "VIP" Entonces
		porcentaje_descuento <- 0.05
	Sino 
		Escribir "No recibe descuento."
	FinSi
	
	valor_descuento <- valor_compra * porcentaje_descuento
	valor_totalpagar <- valor_compra - valor_descuento
	
	Escribir "Porcentaje de descuento: ", porcentaje_descuento * 100, "%"
	Escribir "Valor del descuento: ", valor_descuento
	Escribir "Valor total a pagar: ", valor_totalpagar
	
FinProceso
