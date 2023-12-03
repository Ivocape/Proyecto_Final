import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


  
class histogramas:
  def __init__(self):
    pass
 
  def mostrar_popup(self,texto,tipo):
    from GUI import instance
    instance.ventana = tk.Tk()
    instance.ventana.title("No hay data para mostrar POPUP")
    instance.ventana.geometry("600x100")
    instance.ventana.configure(bg="red")
    label = tk.Label(instance.ventana, text=(texto + str(tipo)), bg="black", fg="orange")
    label.pack()
    instance.ventana.mainloop()

  def grafico_de_tortas(self,porcentaje1,porcentaje2,texto1,texto2,titulo):
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
    etiquetas = [texto1, texto2]

    # Colores para cada sección del gráfico
    colores = ['purple', 'blue']

    # Crear el gráfico de torta
    ax.pie(porcentajes, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)

    # Configuraciones adicionales del gráfico
    ax.set_title(titulo)

    # Crear el lienzo para el gráfico en tkinter
    canvas = FigureCanvasTkAgg(fig, master=instance.ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
  def mostrar_dato(self,categoria):
    from GUI import instance
    instance.ventana = tk.Tk()
    
    instance.ventana.title("Mostrar Dato")
  
  
  
 
  def histograma_tabla(self,categorias,lista,referencia):
    
    from GUI import instance
      # Contar la frecuencia de cada categoría
    instance.ventana=tk.Tk()
    frecuencia = Counter(categorias)

    # Obtener las categorías y las frecuencias por separado
    categorias = list(frecuencia.keys())
    valores = list(frecuencia.values())

    # Crear el gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(categorias, valores, color='blue')

    # Añadir etiquetas y título
    
    ax.set_ylabel('Cantidad de proyectos')
    if referencia == 'area':
        ax.set_title('Cantidad de proyectos por area')
        ax.set_xlabel('Codigo de area')
    elif referencia == 'gran_area':
        ax.set_title('Cantidad de proyectos por gran area')
        ax.set_xlabel('Codigo de gran area')

    # Mostrar el gráfico
    canvas = FigureCanvasTkAgg(fig, master=instance.ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side='left', padx=10, pady=10,fill='both', expand=True)


    # Crear el Treeview y agregar las columnas
    tree = ttk.Treeview(instance.ventana, columns=('Código', 'Referencia'), show='headings')
    tree.heading('Código', text='Código')
    tree.heading('Referencia', text='Referencia')

    # Agregar filas al Treeview desde PrettyTable
    for row in lista:
        tree.insert('', 'end', values=row)

    # Mostrar el Treeview
    tree.pack(side='right', padx=10, pady=10, fill='both')
    
    
