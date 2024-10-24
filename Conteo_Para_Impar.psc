Algoritmo Conteo_Para_Impar
	Definir N Como Entero
	Definir Suma Como Entero
	
	N = 0
	Suma = 0
	
	
	Mientras inf <> 2 Hacer
		Escribir "1- Iniciar un conteo del 1 al 100 mostrando solamente los numeros impares"
		Escribir "2- Salir"
		Leer inf
		
		Segun inf Hacer
			Caso 1:
			k <- 1
				Para i <- k Hasta 100 Con Paso 1 Hacer
					Si (k%2) <> 0 Entonces
					Escribir k
					k = k + 1
				Sino
					k = k + 1
				FinSi
				Fin Para
			Caso 2:
				Escribir "Muchas gracias por utilizar este programa"
		FinSegun
	FinMientras
FinAlgoritmo
