import os
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

ARCHIVO = "clash.txt"
Cartas = []

# Crear una función para cargar datos
def cargar_datos():
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
                    mazo = partes[9:]
                    
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
            f.write(f"{carta['nombre']},{carta['Calidad']},{carta['Elixir']},{carta['Tipo']},{carta['Vida']},{carta['Rango']},{carta['Rapidez']},{carta['Objetivo']},{carta['Daño']},{','.join(carta['Mazo'])}\n")

# Función para registrar una carta
def registrar_alumno():
    nombre = simpledialog.askstring("Registro", "Ingresa el nombre de la carta:")
    calidad = simpledialog.askstring("Registro", "Ingresa la calidad de la carta:")
    elixir = simpledialog.askstring("Registro", "Ingresa el coste de elixir de la carta:")
    tipodetropa = simpledialog.askstring("Registro", "Ingresa el tipo de tropa de la carta:")
    vida = simpledialog.askstring("Registro", "Ingresa la vida de la carta:")
    rango = simpledialog.askstring("Registro", "Ingresa el rango de la carta:")
    rapidezdeataque = simpledialog.askstring("Registro", "Ingresa la rapidez de la carta:")
    objetivo = simpledialog.askstring("Registro", "Ingresa el objetivo principal de la carta:")
    daño = simpledialog.askstring("Registro", "Ingresa el daño que causa la carta:")

    mazo = []
    for i in range(3):
        mazo.append(simpledialog.askstring("Registro", f"Ingrese el nombre de un mazo donde se utiliza esta carta ({i+1}/3):"))

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
    messagebox.showinfo("Registro", "La carta se registró correctamente")

# Función para consultar cartas y mostrar en una tabla
def consultar_alumnos():
    ventana = tk.Toplevel()
    ventana.title("Lista de Cartas")

    tree = ttk.Treeview(ventana, columns=("Nombre", "Calidad", "Elixir", "Tipo", "Vida", "Rango", "Rapidez", "Objetivo", "Daño", "Mazo"), show="headings")
    headers = ["Nombre", "Calidad", "Elixir", "Tipo", "Vida", "Rango", "Rapidez", "Objetivo", "Daño", "Mazo"]
    
    for header in headers:
        tree.heading(header, text=header)

    actualizar_tabla(tree)  # Llamar a la función para actualizar la tabla con los datos cargados

    tree.pack(fill=tk.BOTH, expand=True)

# Función para actualizar la tabla de datos
def actualizar_tabla(tree):
    for row in tree.get_children():
        tree.delete(row)
    for carta in Cartas:
        tree.insert("", tk.END, values=(carta["nombre"], carta["Calidad"], carta["Elixir"], carta["Tipo"], carta["Vida"], carta["Rango"], carta["Rapidez"], carta["Objetivo"], carta["Daño"], ', '.join(carta["Mazo"])))

# Función para buscar una carta
def Buscar_Carta():
    nombre = simpledialog.askstring("Buscar Carta", "Ingresa el nombre de la carta que deseas buscar:")
    for carta in Cartas:
        if carta['nombre'] == nombre:
            messagebox.showinfo("Carta Encontrada", f"Nombre: {carta['nombre']}\nCalidad: {carta['Calidad']}\nCoste de elixir: {carta['Elixir']}\nTipo: {carta['Tipo']}\nVida: {carta['Vida']}\nRango: {carta['Rango']}\nRapidez: {carta['Rapidez']}\nObjetivo: {carta['Objetivo']}\nDaño: {carta['Daño']}\nMazos: {', '.join(carta['Mazo'])}")
            return
    messagebox.showerror("Error", "Carta no encontrada")

# Función para editar una carta
def editar_alumno():
    nombre = simpledialog.askstring("Editar Carta", "Ingresa el nombre de la carta que desea editar:")
    for carta in Cartas:
        if carta['nombre'] == nombre:
            carta['nombre'] = simpledialog.askstring("Editar", "Ingresa el nuevo nombre o presiona Enter para mantener el actual:", initialvalue=carta['nombre']) or carta['nombre']
            carta['Calidad'] = simpledialog.askstring("Editar", "Ingresa la nueva calidad o presiona Enter para mantener el actual:", initialvalue=carta['Calidad']) or carta['Calidad']
            carta['Elixir'] = simpledialog.askstring("Editar", "Ingresa el nuevo coste de elixir o presiona Enter para mantener el actual:", initialvalue=carta['Elixir']) or carta['Elixir']
            carta['Tipo'] = simpledialog.askstring("Editar", "Ingresa el nuevo tipo de tropa o presiona Enter para mantener el actual:", initialvalue=carta['Tipo']) or carta['Tipo']
            carta['Vida'] = simpledialog.askstring("Editar", "Ingresa la nueva vida o presiona Enter para mantener el actual:", initialvalue=carta['Vida']) or carta['Vida']
            carta['Rango'] = simpledialog.askstring("Editar", "Ingresa el nuevo rango o presiona Enter para mantener el actual:", initialvalue=carta['Rango']) or carta['Rango']
            carta['Rapidez'] = simpledialog.askstring("Editar", "Ingresa la nueva rapidez o presiona Enter para mantener el actual:", initialvalue=carta['Rapidez']) or carta['Rapidez']
            carta['Objetivo'] = simpledialog.askstring("Editar", "Ingresa el nuevo objetivo o presiona Enter para mantener el actual:", initialvalue=carta['Objetivo']) or carta['Objetivo']
            carta['Daño'] = simpledialog.askstring("Editar", "Ingresa el nuevo daño o presiona Enter para mantener el actual:", initialvalue=carta['Daño']) or carta['Daño']
            mazo = simpledialog.askstring("Editar", "Ingresa los nuevos mazos separados por comas o presiona Enter para mantener el actual:", initialvalue=','.join(carta['Mazo']))
            carta['Mazo'] = mazo.split(',') if mazo else carta['Mazo']
            guardar_datos()
            messagebox.showinfo("Editar Carta", "Carta editada correctamente")
            return
    messagebox.showerror("Error", "Carta no encontrada")

# Función para eliminar una carta
def eliminar_alumno():
    nombre = simpledialog.askstring("Eliminar Carta", "Ingresa el nombre de la carta que deseas eliminar:")
    for i, carta in enumerate(Cartas):
        if carta['nombre'] == nombre:
            del Cartas[i]
            guardar_datos()
            messagebox.showinfo("Eliminar Carta", "Carta eliminada correctamente")
            return
    messagebox.showerror("Error", "Carta no encontrada")

# Función principal
def main():
    cargar_datos()
    
    root = tk.Tk()
    root.title("Gestión de Cartas")
    
    # Botones de opciones
    btn_registrar = tk.Button(root, text="Registrar carta", command=registrar_alumno)
    btn_consultar = tk.Button(root, text="Consultar cartas", command=consultar_alumnos)
    btn_editar = tk.Button(root, text="Editar carta", command=editar_alumno)
    btn_eliminar = tk.Button(root, text="Eliminar carta", command=eliminar_alumno)
    btn_buscar = tk.Button(root, text="Buscar carta", command=Buscar_Carta)
    btn_salir = tk.Button(root, text="Salir", command=root.quit)

    # Organizar botones en la ventana
    btn_registrar.pack(fill=tk.X)
    btn_consultar.pack(fill=tk.X)
    btn_editar.pack(fill=tk.X)
    btn_eliminar.pack(fill=tk.X)
    btn_buscar.pack(fill=tk.X)
    btn_salir.pack(fill=tk.X)

    root.mainloop()

main()
