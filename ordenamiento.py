import time
import tkinter as tk
from tkinter import messagebox, simpledialog

# Métodos de ordenamiento
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:  
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def seleccion_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
    return lista

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista)//2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quick_sort(izquierda) + medio + quick_sort(derecha)

# Función principal de ordenamiento
def ordenar_lista():
    entrada = simpledialog.askstring("Entrada de datos", "Ingresa una lista de números separados por comas (máximo 40):")
    if not entrada:
        messagebox.showerror("Error", "No ingresaste ninguna lista.")
        return

    try:
        lista_original = [int(x) for x in entrada.split(",")][:40]
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa solo números separados por comas.")
        return

    metodo = simpledialog.askinteger(
        "Método de ordenamiento",
        "Selecciona el método de ordenamiento:\n"
        "1. Burbuja\n"
        "2. Selección\n"
        "3. Inserción\n"
        "4. Merge Sort\n"
        "5. Quick Sort",
    )

    if metodo not in [1, 2, 3, 4, 5]:
        messagebox.showerror("Error", "Opción no válida.")
        return

    lista_ordenada = []
    inicio = time.time()

    if metodo == 1:
        lista_ordenada = burbuja(lista_original[:])
    elif metodo == 2:
        lista_ordenada = seleccion_sort(lista_original[:])
    elif metodo == 3:
        lista_ordenada = insercion(lista_original[:])
    elif metodo == 4:
        lista_ordenada = merge_sort(lista_original[:])
    elif metodo == 5:
        lista_ordenada = quick_sort(lista_original[:])

    fin = time.time()

    # Mostrar resultados
    messagebox.showinfo(
        "Resultados",
        f"Lista original: {lista_original}\n"
        f"Lista ordenada: {lista_ordenada}\n"
        f"Tiempo de ejecución: {fin - inicio:.6f} segundos",
    )

# Crear ventana principal
def main():
    root = tk.Tk()
    root.title("Ordenamiento de listas")

    tk.Label(root, text="Programa de Ordenamiento", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Iniciar", command=ordenar_lista, font=("Arial", 12), bg="lightblue").pack(pady=20)
    tk.Button(root, text="Salir", command=root.destroy, font=("Arial", 12), bg="red", fg="white").pack(pady=10)

    root.geometry("400x200")
    root.mainloop()

if __name__ == "__main__":
    main()
