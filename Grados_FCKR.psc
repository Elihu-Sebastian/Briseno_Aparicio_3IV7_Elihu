Funcion FAHRENHEIT(f, c, k, r)
	Limpiar Pantalla
	Escribir "Introduce los grados Fahrenheit"
	Leer f
	Limpiar Pantalla
	Mientras inf <> 4 Hacer
		Escribir "Elije una temperatura para hacer un conversion"
		Escribir "Celsius - 1"
		Escribir "Kelvine - 2"
		Escribir "Rankine - 3"
		Escribir "Elejir otro grado - 4"
		Leer inf
		Segun inf Hacer
			Caso 1:
				Limpiar Pantalla
				c <- (5/9) * (f-32)
				Escribir "Los ",f " Grados Fahrenheit dan como resultado: ",c " Grados Celsius"
				
			Caso 2:
				Limpiar Pantalla
				k <- (F+479.67) * (5/9)
				Escribir "Los ",f " Grados Faherenheit dan como resultado: ",k " Grados Kelvin"
				
			Caso 3:
				Limpiar Pantalla
				r <- f + 459.67
				Escribir "Los ",f " Grados Fahrenheit dan como resultado: ",r " Grados Rankine"
				
			Caso 4:
				Limpiar Pantalla
		Fin Segun
	FinMientras
FinFuncion

Funcion CELSIUS(f,c,k,r)
	Limpiar Pantalla
	Escribir "Introduce los grados Celsius"
	Leer c
	Limpiar Pantalla
	Mientras inf <> 4 Hacer
		Escribir "Elije una temperatura para hacer un conversion"
		Escribir "Fahrenheit - 1"
		Escribir "Kelvine - 2"
		Escribir "Rankine - 3"
		Escribir "Salir - 4"
		Leer inf
		Segun inf Hacer
			Caso 1:
				Limpiar Pantalla
				f <- ((9/5)*c)+ 32
				Escribir "Los ", c " Grados Celsius dan como resultado: ",f " Grados Fahrenheit" 
			Caso 2:
				Limpiar Pantalla
				k <- c + 273.15
				Escribir "Los ",c " Grados Celsius dan como resultado: ",k " Grados Kelvin"
			Caso 3:
				Limpiar Pantalla
				r <- c * 1.8 + 491.67
				Escribir "Los ",c " Grados Celsius dan como resultado: ",r " Grados Rankine"
			Caso 4:
				Limpiar Pantalla
		Fin Segun
	FinMientras
FinFuncion

Funcion KELVINE(f, c, k,r)
	Limpiar Pantalla
	Escribir "Introduce los grados Kelvine"
	Leer k
	Limpiar Pantalla
	Mientras inf <> 4 Hacer
		Escribir "Elije una temperatura para hacer un conversion"
		Escribir "Fahrenheit - 1"
		Escribir "Celsius - 2"
		Escribir "Rankine - 3"
		Escribir "Salir - 4"
		Leer inf
		Segun inf Hacer
			Caso 1:
				Limpiar Pantalla
				f <- 1.8 *(k-273) +32
				Escribir "Los ",k " Grados Kelvin dan como resultado: ",f " Grados Fahrenheit"
			Caso 2:
				Limpiar Pantalla
				c <- k - 273.15
				Escribir "Los ",k " Grados kelvin dan como resultado: ",c " Grados Celsius"
			Caso 3:
				Limpiar Pantalla
				r <- k * 1.8
				Escribir "Los ",k " Grados Kelvin dan como resultado: ",r " Grados Rankine"
			Caso 4:
				Limpiar Pantalla
		Fin Segun
	FinMientras
FinFuncion

Funcion RANKINE(f, c,k,r)
	Limpiar Pantalla
	Escribir "Introduce los grados Rankine"
	Leer r
	Limpiar Pantalla
	Mientras inf <> 4 Hacer
		Escribir "Elije una temperatura para hacer un conversion"
		Escribir "Fahrenheit - 1"
		Escribir "Celsius - 2"
		Escribir "Kelvine - 3"
		Escribir "Salir - 4"
		Leer inf
		Segun inf Hacer
			Caso 1:
				Limpiar Pantalla
				f <- r - 459.67
				Escribir "Los ",r " Grados Rankine dan como resultado: ",f " Grados Fahrenheit"
			Caso 2:
				Limpiar Pantalla
				c <- (r - 491.67)/1.8
				Escribir "Los ",r " Grados Rankine dan como resultado: ",c " Grados Celsius"
			Caso 3:
				Limpiar Pantalla
				k <- r * (5/9)
				Escribir "Los ",r " Grados Rankine dan como resultado: ",k " Grados Kelvin"
			Caso 4:
				Limpiar Pantalla
		Fin Segun
	FinMientras
FinFuncion
Algoritmo Grados_FCKR
	Mientras inf <> 5 Hacer
		Escribir "Elije una temperatura"
		Escribir "Fahrenheit - 1"
		Escribir "Celsius - 2"
		Escribir "Kelvine - 3"
		Escribir "Rankine - 4"
		Escribir "Salir - 5"
		Leer inf
		
		Segun inf Hacer
			Caso 1:
				FAHRENHEIT(f, c, k, r)
				
			Caso 2:
				CELSIUS(f,c,k,r)
				
			Caso 3:
				KELVINE(f, c, k,r)
				
			Caso 4:
				RANKINE(f, c,k,r)
				
			Caso 5:
				Escribir "Gracias por utilizar este programa"
		Fin Segun
		
	FinMientras
FinAlgoritmo
