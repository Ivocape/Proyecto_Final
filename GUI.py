import matplotlib.pyplot as plt
from tkinter import Tk, Frame, Canvas, Button
from procesos import *
from discoDuro import *
from menus import *
from analisis import *
from histogramas import *
from tkinter import *
  
  
class HistogramGUI:
    def __init__(self):
        self.discoDuro=DiscoDuro()
        self.cache=Cache()
        self.histogramas=histogramas()
        self.analisis=Analisis()
    
        self.root = Tk()
        self.root.title("Menu Principal")
        
        self.frame = Frame(self.root)
        self.frame.pack()

        self.canvas = Canvas(self.frame, width=400, height=300)
        self.canvas.pack()

        self.button = Button(self.frame, text="distribución de los proyectos por área de investigación", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(self.frame, text="porcentaje de participación de las mujeres en los diferentes proyectos según el rol quedesempeña", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(self.frame, text="tiempo promedio de terminación", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(self.frame, text=" porcentaje de proyectos que han utilizado tecnologías emergentes", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(self.frame, text="lista de proyectos", command=self.histogramas.show_histogram)
        self.button.pack()

        self.button = Button(self.frame, text="Financiamiento Solicitado/Otorgado", command=self.histogramas.show_histogram)
        self.button.pack()

    def setup(self):

        listacsv=['proyectos_2015.csv','proyectos_2016.csv','proyectos_2017.csv','proyectos_2018.csv']
        for carpeta in listacsv:
            self.discoDuro.leerSETUP(carpeta)
        
    def run(self):
        self.root.mainloop()
            
instance=HistogramGUI()
#instance.setup()
instance.run()
