
def dec_Bin(dec):
    bina = ""
    bin(dec)
    bina = (int(bin(dec)[2:]))
    return bina

def bin_dec(dec):
    dec = int(str(dec), 2)
    return dec


print("Hola bienvenido a python con funciones")
print("Escoje una opcion: ")
print("A.- Convertir numero a binario")
print("B.- Convertir binario a numero")

    #programa
opcion = input("introduce la opcion a desear: ").upper()

if opcion == "A":
        dec = 0
        ndecimal = 0
        print("ingresa una numero entero para transformar a binario")
        dec = int(input())
        ndecimal = dec_Bin(dec)
        print("Numero binario", ndecimal)
elif opcion =="B":
        dec = 0
        binario = 0
        b = 0
        print("ingresa una numero entero para transformar a decimal")
        dec = int(input())
        binario = bin_dec(dec)
        print("El numero es", binario)
else:
    print("Opcion no valida") 