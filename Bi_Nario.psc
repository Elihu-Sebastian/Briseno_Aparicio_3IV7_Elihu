Algoritmo Bi_Nario
	Definir num, residuo Como entero
	Definir binario Como texto
	
	//El binario lo tengo que concatenar
	Binario = ""
	
	Mientras inf <> 2 Hacer
		Escribir "Convertir un numero a Binario - 1"
		Escribir "Salir - 2"
		Leer inf
		
		Segun inf Hacer
			Caso 1:
	Escribir "introduce el numero que decea convertir a binario"
	Leer num
	
	Si num >= 0 Entonces
		Mientras num > 0 Hacer
			residuo = num%2
			//Tengo que ir armando el binario
			nuevobinario <- ConvertirATexto(residuo)
			binario = nuevobinario + binario
			
			num = Trunc(num/2)
		FinMientras
		
		//Si el numero es cero
		Si binario = "" Entonces
			binario = "0"
			
		FinSi
		Escribir "El numero binario es: ", binario
	FinSi
Caso 2:
	Escribir "Gracias por utilizar este programa"
FinSegun
FinMientras
FinAlgoritmo
