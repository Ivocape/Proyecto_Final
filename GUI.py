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
        self.root.title("Histograma")
        
        self.frame = Frame(self.root)
        self.frame.pack()

        self.canvas = Canvas(self.frame, width=400, height=300)
        self.canvas.pack()

        self.button = Button(self.frame, text="Mostrar Histograma", command=self.histogramas.show_histogram)
        self.button.pack()
    def setup(self):

        listacsv=['users.csv', 'reservas.csv', 'room.csv','buffet.csv', 'tareas.csv', 'pedidos.csv','ingresos.csv','inversion.csv']
        for carpeta in listacsv:
            self.discoDuro.leerSETUP(carpeta)
        
    def run(self):
        self.analisis.lista_proyectos_fecha()
            
instance=HistogramGUI()
#instance.setup()
instance.run()
