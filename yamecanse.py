import os

ARCHIVO = "alumnos.txt"
Cartas = []

# Crear una función para cargar datos
def cargar_datos():
    # Verificar si existe el archivo
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) >= 10:
                    nombre = partes[0]
                    calidad = partes[1]
                    elixir = partes[2]
                    tipodetropa = partes[3]
                    vida = partes[4]
                    rango = partes[5]
                    rapidezdeataque = partes[6]
                    objetivo = partes[7]
                    daño = partes[8]
                    mazo = list(map(float, partes[9:]))  # Aseguramos que mazo sea una lista de floats
                    carta = {
                        "nombre": nombre, 
                        "Calidad": calidad, 
                        "Elixir": elixir, 
                        "Tipo": tipodetropa, 
                        "Vida": vida, 
                        "Rango": rango,
                        "Rapidez": rapidezdeataque,
                        "Objetivo": objetivo,
                        "Daño": daño,
                        "Mazo": mazo,
                    }
                    Cartas.append(carta)

# Función para guardar datos
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for carta in Cartas:
            f.write(f"{carta['nombre']},{carta['Calidad']},{carta['Elixir']},{carta['Tipo']},{carta['Vida']},{carta['Rango']},{carta['Rapidez']},{carta['Objetivo']},{carta['Daño']},{','.join(map(str, carta['Mazo']))}\n")

# Función para registrar una carta
def registrar_alumno():
    nombre = input("Ingresa el nombre de la carta: ")
    calidad = input("Ingresa la calidad de la carta: ")
    elixir = input("Ingresa el coste de elixir de la carta: ")
    tipodetropa = input("Ingresa el tipo de tropa de la carta: ")
    vida = input("Ingresa la vida de la carta: ")
    rango = input("Ingresa el rango de la carta: ")
    rapidezdeataque = input("Ingresa la rapidez de la carta: ")
    objetivo = input("Ingresa el objetivo principal de la carta: ")
    daño = input("Ingresa el daño que causa la carta: ")
    
    mazo = []
    for i in range(3):  
        mazos = float(input(f"Escribe un mazo donde se utiliza esta carta: "))
        mazo.append(mazos)

    carta = {
        "nombre": nombre, 
        "Calidad": calidad, 
        "Elixir": elixir, 
        "Tipo": tipodetropa, 
        "Vida": vida, 
        "Rango": rango,
        "Rapidez": rapidezdeataque,
        "Objetivo": objetivo,
        "Daño": daño,
        "Mazo": mazo, 
    }
    
    Cartas.append(carta)
    guardar_datos()
    print("La carta se registró correctamente")

# Función para consultar cartas
def consultar_alumnos():
    print("Lista de Cartas:\n")
    for carta in Cartas:
        print(f"Nombre: {carta['nombre']}, Calidad: {carta['Calidad']}, Coste de elixir: {carta['Elixir']}, Tipo: {carta['Tipo']}, Vida: {carta['Vida']}, Rango: {carta['Rango']}, Rapidez: {carta['Rapidez']}, Objetivo principal: {carta['Objetivo']}, Daño: {carta['Daño']}, Mazos donde se utiliza: {carta['Mazo']}\n")

# Función para editar una carta
def editar_alumno():
    nombre = input("Ingresa el nombre de la carta que desea editar: ")
    for carta in Cartas:
        if carta['nombre'] == nombre:
            carta['nombre'] = input("Ingresa el nuevo nombre o presiona Enter para mantener el actual: ") or carta['nombre']
            carta['Calidad'] = input("Ingresa la nueva calidad o presiona Enter para mantener el actual: ") or carta['Calidad']
            carta['Elixir'] = input("Ingresa el nuevo coste de elixir o presiona Enter para mantener el actual: ") or carta['Elixir']
            carta['Tipo'] = input("Ingresa el nuevo tipo de tropa o presiona Enter para mantener el actual: ") or carta['Tipo']
            carta['Vida'] = input("Ingresa la nueva vida o presiona Enter para mantener el actual: ") or carta['Vida']
            carta['Rango'] = input("Ingresa el nuevo rango o presiona Enter para mantener el actual: ") or carta['Rango']
            carta['Rapidez'] = input("Ingresa la nueva rapidez o presiona Enter para mantener el actual: ") or carta['Rapidez']
            carta['Objetivo'] = input("Ingresa el nuevo objetivo o presiona Enter para mantener el actual: ") or carta['Objetivo']
            carta['Daño'] = input("Ingresa el nuevo daño o presiona Enter para mantener el actual: ") or carta['Daño']
            carta['Mazo'] = list(map(float, input("Ingresa los nuevos mazos separados por comas o presiona Enter para mantener el actual: ").split(','))) or carta['Mazo']
            guardar_datos()
            print("Carta editada correctamente")
            break
    else:
        print("Carta no encontrada")

# Función para eliminar una carta
def eliminar_alumno():
    nombre = input("Ingresa el nombre de la carta que deseas eliminar: ")
    for i, carta in enumerate(Cartas):
        if carta['nombre'] == nombre:
            del Cartas[i]
            guardar_datos()
            print("Carta eliminada correctamente")
            return
    print("Carta no encontrada")

# Menú principal
def main():
    cargar_datos()
    while True:
        print("\nMenú de Gestión de Cartas")
        print("1- Registrar carta")
        print("2- Consultar cartas")
        print("3- Editar carta")
        print("4- Eliminar carta")
        print("5- Salir")
       
        opcion = input("Seleccione una opción: ")
       
        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            consultar_alumnos()
        elif opcion == "3":
            editar_alumno()
        elif opcion == "4":
            eliminar_alumno()
        elif opcion == "5":
            print("Adiós")
            break
        else:
            print("Opción no válida")

main()
