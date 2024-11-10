import math


#vamos a crear una funcin para calcular el area y el perimetro

def rectangulo(base, altura):
    area = base * altura
    perimetro = 2*(base+altura)
    return area, perimetro

def triangulo(base, altura, lado1, lado2, lado3):
    area = (base * altura)/3
    perimetro = lado1 + lado2 + lado3
    return area, perimetro

def esfera(radio):
    volumen = (4/3)*math.pi*radio**3
    return volumen

def menu():
    print("Hola bienvenido a python con funciones")
    print("Escoje una opcion: ")
    print("A.- Area y perimetro del rectangulo")
    print("B.- Area y perimetro del triangulo")
    print("C.- Volumen de la esfera")

    #programa
    menu()
    opcion = input("introduce la opcion a desear: ").upper()

    if opcion == "A":
        base = float(input("introduce la base del rectangulo"))
        altura = float(input("introduce la altura del rectangulo"))
        area, perimetro = rectangulo(base, altura)
        print("El area es de: ", area)
        print("El perimetro es: ", perimetro)
    elif opcion == "B":
        base = float(input("introduce la base del triangulo"))
        altura = float(input("introduce la altura del triangulo"))
        lado1 = float(input("inroduce un lado"))
        lado2 = float(input("inroduce un lado"))
        lado3 = float(input("inroduce un lado"))
        area, perimetro = triangulo(base, altura, lado1, lado2, lado3)
        print("El area es de: ", area)
        print("El perimetro es: ", perimetro)
    if opcion == "C":
        radio = float(input("introduce el radio"))
        volumen = esfera(radio)
        print("El area es de: ", volumen)
       
    else:
        print ("Opcion no valida pendejo xd xd xd xd")

#Deben realizar el rpograma de convertit un numero decimal en binario y de binario en decimal