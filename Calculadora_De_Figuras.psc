SubProceso Cuadrado(lado)
        Definir area, perimetro Como Real
        area = lado*lado
        perimetro = 4*lado
        Escribir "EL area del cuadrado es: ", area
        Escribir "El perimetro del cuadrado es: ", perimetro
FinSubProceso

SubProceso Pentagono(lado, apotema)
    Definir area, perimetro Como Real
    perimetro = 5* lado
    area = (perimetro*apotema) / 2
    Escribir "EL area del pentagono es: ", area
    Escribir "El perimetro del pentagonp es: ", perimetro
FinSubProceso


SubProceso Hexagono(lado, apotema)
    Definir area, perimetro Como Real
    perimetro = 6* lado
    area = (perimetro*apotema) / 2
    Escribir "EL area del hexagono es: ", area
    Escribir "El perimetro del hexagono es: ", perimetro
FinSubProceso


SubProceso trapecio(base, basemenor, altura, lado1,lado2)
    Definir area, perimetro Como Real
    area = ((base * basemenor) / 2) * altura
    perimetro = lado1+lado2+base+basemenor
    Escribir "EL area del trapecio es: ", area
    Escribir "El perimetro del trapecio es: ", perimetro
FinSubProceso


SubProceso Octagono(apotema, lado)
    Definir area, perimetro Como Real
    perimetro = 8* lado
    area = (perimetro*apotema) / 2
    Escribir "EL area del octagono es: ", area
    Escribir "El perimetro del octagono es: ", perimetro
FinSubProceso


SubProceso Rectangulo(base, altura)
    Definir area, perimetro Como Real
    area = base * altura
    perimetro = 2*(base+altura)
    Escribir "EL area del rectangulo es: ", area
    Escribir "El perimetro del rectangulo es: ", perimetro
FinSubProceso

Algoritmo Calculadora_De_Figuras
    Definir opcion Como Caracter
    Definir apotema, base, basemenor, altura, lado,lado1, lado2 Como Real
    //Crear menu
	Mientras opcion <> "G" Hacer
		
    Escribir "Selecciona una opcion: "
    Escribir "A- Area y perimetro del cuadrado"
    Escribir "B- Area y perimetro del Pentagono"
	Escribir "C- Area y perimetro del Hexagono"
	Escribir "D- Area y perimetro del Trapecio"
	Escribir "E- Area y perimetro del Octagono"
	Escribir "F- Area y perimetro del Rectangulo"
	Escribir "G- Salir"
    Leer opcion
	
    Segun opcion Hacer
            //Caso 1
        Caso"A":
            Escribir "Ingresa el lado del cuadrado"
            Leer lado
			Si lado < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer lado
			FinSi
			Cuadrado(lado)
        Caso "B":
            Escribir "Ingresa el lado del pentagono"
            Leer lado
			Si lado < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer lado
			FinSi
            Escribir "Ingresa el apotema del pentagono"
            Leer apotema
			Si apotema < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer apotema
			FinSi
			Pentagono(lado, apotema)
		Caso "C":
			Escribir "Ingresa el lado del hexagono"
            Leer lado
			Si lado < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer lado
			FinSi
            Escribir "Ingresa el apotema del hexagono"
            Leer apotema
			Si apotema < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer apotema
			FinSi
			Hexagono(lado, apotema)
		Caso "D":
			Escribir "Ingresa una base del trapecio"
            Leer base
			Si base < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer base
			FinSi
			Escribir "Ingresa una base del trapecio"
		    Leer basemenor
			Si basemenor < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer basemenor
			FinSi
            Escribir "Ingresa la altura del trapecio"
            Leer altura
			Si altura < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer altura
			FinSi
            Escribir "Ingrese un lado"
            Leer lado1
			Si lado1 < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer lado1
			FinSi
            Escribir "Ingrese un lado"
            Leer lado2
			Si lado2 < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer lado2
			FinSi
			trapecio(base, basemenor, altura, lado1,lado2)
		Caso "E":
			Escribir "Ingresa un lado del octagono"
            Leer lado
			Si lado < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer lado
			FinSi
            Escribir "Ingresa el apotema del octagono"
            Leer apotema
			Si apotema < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer apotema
			FinSi
			Octagono(apotema, lado)
		Caso "F":
			Escribir "Ingresa la base del rectangulo"
            Leer base
			Si base < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer base
			FinSi
            Escribir "Ingresa la altura del rectangulo"
            Leer altura
			Si altura < 0 Entonces
				Escribir "Ingrese una cantidad positiva"
				Leer altura
			FinSi
            Rectangulo(base, altura)
		Caso "G":
			Escribir "Gracias de utilizar este programa"
        De Otro Modo:
            Escribir "Opcion no valida"
    FinSegun
FinMientras	
FinAlgoritmo
