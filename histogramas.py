import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


  
class histogramas:
  def __init__(self):
    pass

  def mostrar_popup(self, mensaje_principal, datos=None):
    nuevaventana = tk.Tk()
    nuevaventana.title("Popup")
    nuevaventana.geometry("600x200")
    nuevaventana.configure(bg="lightblue")

    #crear una etiqueta con el mensaje principal
    label_principal = tk.Label(nuevaventana, text=mensaje_principal, bg="white", fg="black", justify="left", font=("Arial", 30))
    label_principal.pack()

    if datos is not None:
      #crear una etiqueta con los datos
      label_datos = tk.Label(nuevaventana, text=datos, bg="white", fg="black", justify="left")
      label_datos.pack()
    else:
       #mostrar mensaje indicando que no hay datos
       label_no_datos = tk.Label(nuevaventana, text="No hay datos para mostrar", bg="red", fg="black", justify="left", font=("Arial", 26))
       label_no_datos.pack()
    nuevaventana.mainloop()

  # def mostrar_popup(self,texto,tipo):
  #   from GUI import instance
  #   nuevaventana = tk.Tk()
  #   nuevaventana.title("No hay data para mostrar POPUP")
  #   nuevaventana.geometry("600x100")
  #   nuevaventana.configure(bg="red")
  #   label = tk.Label(nuevaventana, text=(texto + str(tipo)), bg="black", fg="orange")
  #   label.pack()
  #   nuevaventana.mainloop()

  def grafico_de_tortas(self,porcentaje1,porcentaje2,texto1,texto2,titulo):
    # Datos para el histograma
    nuevaventana = tk.Tk()
    
    nuevaventana.title("Grafico de tortas")
    print(porcentaje1,porcentaje2)
    porcentajes = [porcentaje1,porcentaje2]
    # Crear figura de Matplotlib
    fig = Figure(figsize=(9, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Etiquetas para cada sección del gráfico
    etiquetas = [texto1, texto2]

    # Colores para cada sección del gráfico
    colores = ['#E74C3C', '#85C1E9']

    # Crear el gráfico de torta
    ax.pie(porcentajes, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)

    # Configuraciones adicionales del gráfico
    ax.set_title(titulo)

    # Crear el lienzo para el gráfico en tkinter
    canvas = FigureCanvasTkAgg(fig, master=nuevaventana)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True,fill='both',)
    
  def mostrar_dato(self,categoria):
    nuevaventana = tk.Tk()
    
    nuevaventana.title("Mostrar Dato")
  
  
  def tabla(self,lista):
    nuevaventana = tk.Tk()
    tree = ttk.Treeview(nuevaventana, columns=('Fecha', 'Titulo'), show='headings')
    tree.heading('Fecha', text='Fecha')
    tree.heading('Titulo', text='Titulo')
    tree.column('Fecha', width=100)
    tree.column('Titulo', width=600)

    # Agregar filas al Treeview desde PrettyTable
    for row in lista:
        tree.insert('', 'end', values=row)

    # Mostrar el Treeview
    tree.pack(padx=10, pady=10, fill='both',expand=True)
 
  def histograma_tabla(self,categorias,lista,referencia):
    
      # Contar la frecuencia de cada categoría
    nuevaventana=tk.Tk()
    frecuencia = Counter(categorias)

    # Obtener las categorías y las frecuencias por separado
    categorias = list(frecuencia.keys())
    valores = list(frecuencia.values())

    # Crear el gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(categorias, valores, color='#95EBF7')

    # Añadir etiquetas y título
    
    ax.set_ylabel('Cantidad de proyectos')
    if referencia == 'area':
        ax.set_title('Cantidad de proyectos por area')
        ax.set_xlabel('Codigo de area')
    elif referencia == 'gran_area':
        ax.set_title('Cantidad de proyectos por gran area')
        ax.set_xlabel('Codigo de gran area')

    # Mostrar el gráfico
    canvas = FigureCanvasTkAgg(fig, master=nuevaventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side='left', padx=10, pady=10,fill='both', expand=True)


    # Crear el Treeview y agregar las columnas
    tree = ttk.Treeview(nuevaventana, columns=('Código', 'Referencia'), show='headings')
    tree.heading('Código', text='Código')
    tree.heading('Referencia', text='Referencia')

    # Agregar filas al Treeview desde PrettyTable
    for row in lista:
        tree.insert('', 'end', values=row)

    # Mostrar el Treeview
    tree.pack(side='right', padx=10, pady=10, fill='both')
  

    
