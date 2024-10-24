Algoritmo Conteo_Mientras
	Definir N Como Entero
	Definir Suma Como Entero
	
	N = 0
	Suma = 0
	
	
	Mientras inf <> 2 Hacer
		Escribir "1- Iniciar un conteo del 1 al 100"
		Escribir "2- Salir"
		Leer inf
		
		Segun inf Hacer
			Caso 1:
				k <- 1
				Mientras k < 101 Hacer
					Escribir k
					k = k + 1
				Fin Mientras
			Caso 2:
				Escribir "Muchas gracias por utilizar este programa"
		FinSegun
	FinMientras
FinAlgoritmo
