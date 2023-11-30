import matplotlib.pyplot as plt
from procesos import *
from discoDuro import *
from menus import *
from analisis import *
from histogramas import *
import tkinter as tk

class HistogramGUI():
    def __init__(self):
        self.discoDuro=DiscoDuro()
        self.cache=Cache()
        self.histogramas=histogramas()
        self.analisis=Analisis()
    
        self.root = Tk()
        self.root.title("Menu Principal")
        ventana = tk.Tk()
        # Cargar la imagen de fondo
        ruta_imagen = "descarga.png"  ## Reemplaza con la ruta de tu imagen
        imagen_fondo = tk.PhotoImage(file=ruta_imagen)

        # Crear un widget Canvas para la imagen de fondo
        canvas = tk.Canvas(width=600, height=400)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, anchor="nw", image=imagen_fondo)

        # Aquí agregar el resto de tus botones

        # Integrar el botón que se ilumina al pasar el mouse
        boton = tk.Button(ventana, text="Ejemplo Botón", bg="black", fg="white")
        boton.place(relx=0.5, rely=0.5, anchor="center")  # Posiciona el botón en el centro

        def on_enter(event):
            boton.config(bg='gray')  # Cambiar color al pasar el mouse

        def on_leave(event):
            boton.config(bg='black')  # Restaurar color al quitar el mouse

        boton.bind("<Enter>", on_enter)
        boton.bind("<Leave>", on_leave)

        self.button = Button(ventana, text="distribución de los proyectos por área de investigación", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(ventana, text="porcentaje de participación de las mujeres en los diferentes proyectos según el rol quedesempeña", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(ventana, text="tiempo promedio de terminación", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(ventana, text=" porcentaje de proyectos que han utilizado tecnologías emergentes", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(ventana, text="lista de proyectos", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(ventana, text="Financiamiento Solicitado/Otorgado", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(ventana, text="Cerrar", command=self.root.destroy)
        self.button.pack()

    def setup(self):

        listacsv=['proyectos_2015.csv','proyectos_2016.csv','proyectos_2017.csv','proyectos_2018.csv','proyecto_disciplina.csv','proyecto_participante.csv','ref_disciplina.csv','ref_estado_proyecto.csv','ref_funcion.csv','ref_moneda.csv','ref_tipo_proyecto.csv']
        for carpeta in listacsv:
            self.discoDuro.leerSETUP(carpeta)
        
    def run(self):
        self.root.mainloop()
            
instance=HistogramGUI()
