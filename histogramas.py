import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def crear_histograma():
    # Datos para el histograma
    from GUI import instance
    datos= instance.backend.analisis.gran_area_mas_proyectos()
    # Crear figura de Matplotlib
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Crear el histograma
    ax.hist(datos, bins=30, alpha=0.7, color='blue', edgecolor='black')

    # Configuraciones adicionales del histograma
    ax.set_title('Histograma de datos aleatorios')
    ax.set_xlabel('Valores')
    ax.set_ylabel('Frecuencia')

    # Crear el lienzo para el histograma en tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Crear la ventana
ventana = tk.Tk()
ventana.title("Histograma con Matplotlib")

# Crear el botón para generar el histograma
boton_histograma = tk.Button(ventana, text="Generar Histograma", command=crear_histograma)
boton_histograma.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()