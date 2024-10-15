Algoritmo SUMAPOSITIVO_IMPAR

	Definir serie Como Entero 
	
	i = 1
	
	Dimension serie[100];

	
	//tengo que crear un menu de seleccion
	Mientras inf <> 3 Hacer
		Escribir "1- Ingresar un numero"
		Escribir "2- Conteo"
		Escribir "3- salir"
		Leer inf
		
		Segun inf Hacer
			Caso 1:
				Escribir "Ingresa un numero cualquiera ", i;
				Leer serie[i];
				Si serie[i] = 0 Entonces
					Escribir "No se puede 0 al ser un numero neutro, escribe otro numero cualquiera"
					Leer serie[i]
				FinSi
				i = i + 1
			Caso 2:
				positivos <- 0
				negativos <- 0
				Para i <- 1 Hasta i Hacer
					Si serie[i] > 0 Entonces
						positivos <- positivos + 1
					SiNo
						Si serie[i] < 0 Entonces
							negativos <- negativos + 1
						FinSi
					FinSi
				Fin Para

				
			Escribir "La cantidad de  numeros insertados positivos fueron: ", positivos
			Escribir "La cantidad de numeros negativos insertados fueron: ", negativos
			Caso 3:
		    Escribir "Gracias por utilizar este programa"
		FinSegun
	FinMientras

FinAlgoritmo
