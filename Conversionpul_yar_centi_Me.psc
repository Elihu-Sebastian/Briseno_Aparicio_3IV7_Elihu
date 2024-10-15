Algoritmo Conversionpul_yar_centi_Me
	Escribir "Ingresa una cantidad, (Pies)"
	Leer Pies
	
	Mientras inf <> 5 Hacer
		Escribir "Elije una conversion"
		Escribir "Pies a Pulgadas - 1"
		Escribir "Pies a Yardas - 2"
		Escribir "Pies a centimetros - 3"
		Escribir "Pies a metros - 4"
		Escribir "Salir - 5"
		Leer inf
		
		Segun inf Hacer
			Caso 1:
				Pulgadas = 12 * Pies
				Escribir Pies," Pies es igual a: ",Pulgadas " pulgadas"
			Caso 2:
				Yardas = Pies * (1/3)
				Escribir Pies," Pies es igual a: ",Yardas " yardas"
			Caso 3:
				Pulgadas = 12 * Pies
				cm = Pulgadas * 2.54
				Escribir Pies," Pies es igual a: ",cm " cm"
			Caso 4:
				Pulgadas = 12 * Pies
				cm = Pulgadas * 2.54
				Metros = cm /100
				Escribir Pies," Pies es igual a: ",Metros " M"
			Caso 5:
				Escribir "Gracias por utilizar este programa"
		Fin Segun
		
	FinMientras

FinAlgoritmo
