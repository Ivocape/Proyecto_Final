import tkinter as tk
from matplotlib.figure import Figure
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    plt.xlabel('Categorías')
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