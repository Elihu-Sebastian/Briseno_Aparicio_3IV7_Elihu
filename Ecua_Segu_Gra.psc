Algoritmo Ecua_Segu_Gra
	Definir a, b, c Como Entero
	Mientras inf <> 2 Hacer
		Escribir "Calcular una ecuacion de segundo grado - 1"
		Escribir "Salir - 2"
		Leer inf
		
		Segun inf Hacer
		Caso 1:
	Escribir "Ingresa el valor a"
	Leer a
	Escribir "Ingresa el valor b"
	Leer b
	escribir "Ingresa el valor c"
	Leer c

	d <- b*b + 4*a*c
	Si d < 0 Entonces
		d <- -d
		r <- Raiz(d)
		s <- 2*a
		Escribir b,"+","_/",d,"i","/",s
		Escribir b,"-","_/",d,"i","/",s
	
Sino
	Si d >= 0 Entonces
	r <- Raiz(d)
	x = -b + r / 2*a
	xprima <- -b - r / 2*a
	Escribir x
	Escribir xprima
FinSi
FinSi
Caso 2:
	Escribir "Gracias por utilizar este programa"
FinSegun
FinMientras


FinAlgoritmo
