import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from prettytable import PrettyTable

class histogramas:
  def __init__(self):
    pass
  def crear_histograma(self,categorias):
    # Contar la frecuencia de cada categoría
    frecuencia = Counter(categorias)

    # Obtener las categorías y las frecuencias por separado
    categorias = list(frecuencia.keys())
    valores = list(frecuencia.values())

    # Crear el gráfico de barras
    plt.bar(categorias, valores, color='blue')

    # Añadir etiquetas y título
    plt.xlabel('Codigo de Areas')
    plt.ylabel('Frecuencia')
    plt.title('Gráfico de Barras de Frecuencia')
    
    # Mostrar el gráfico
    plt.show()

    
  def grafico_de_tortas(self,porcentaje1,porcentaje2):
    # Datos para el histograma
    from GUI import instance
    instance.ventana = tk.Tk()
    
    instance.ventana.title("Tortas con Matplotlib")
    print(porcentaje1,porcentaje2)
    porcentajes = [porcentaje1,porcentaje2]
    # Crear figura de Matplotlib
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Etiquetas para cada sección del gráfico
    etiquetas = ['Porcentaje A', 'Porcentaje B']

    # Colores para cada sección del gráfico
    colores = ['blue', 'orange']

    # Crear el gráfico de torta
    ax.pie(porcentajes, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)

    # Configuraciones adicionales del gráfico
    ax.set_title('Gráfico de Torta de Dos Porcentajes')

    # Crear el lienzo para el gráfico en tkinter
    canvas = FigureCanvasTkAgg(fig, master=instance.ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()
  def mostrar_dato(self,categoria):
    from GUI import instance
    instance.ventana = tk.Tk()
    
    instance.ventana.title("Mostrar Dato")
  
  
  
#TRABAJO DUSTINNN################################################################################
  def histograma_tabla(self,categorias,listaareas):
    
    from GUI import instance
      # Contar la frecuencia de cada categoría
    frecuencia = Counter(categorias)

    # Obtener las categorías y las frecuencias por separado
    categorias = list(frecuencia.keys())
    valores = list(frecuencia.values())

    # Crear el gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(categorias, valores, color='blue')

    # Añadir etiquetas y título
    ax.set_xlabel('Codigo de Areas')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Gráfico de Barras de Frecuencia')

    # Mostrar el gráfico
    canvas = FigureCanvasTkAgg(fig, master=instance.ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side='left', padx=10, pady=10)

    # Crear la tabla PrettyTable
    tabla = PrettyTable(['Código', 'Referencia'])
    for codigo, descripcion in listaareas:
        tabla.add_row([codigo, descripcion])

    # Crear el Treeview y agregar las columnas
    tree = ttk.Treeview(instance.ventana, columns=('Código', 'Referencia'), show='headings')
    tree.heading('Código', text='Código')
    tree.heading('Referencia', text='Referencia')

    # Agregar filas al Treeview desde PrettyTable
    for row in tabla:
        tree.insert('', 'end', values=row)

    # Mostrar el Treeview
    tree.pack(side='right', padx=10, pady=10)
