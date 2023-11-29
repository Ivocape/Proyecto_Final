import matplotlib.pyplot as plt
from tkinter import Tk, Frame, Canvas, Button
from procesos import *
from discoDuro import *
from menus import *
from tkinter import *

class HistogramGUI:
    def __init__(self, data):
        self.data = data
        self.discoDuro=DiscoDuro()
        self.cache=Cache()
    
        self.root = Tk()
        self.root.title("Histograma")
        
        self.frame = Frame(self.root)
        self.frame.pack()

        self.canvas = Canvas(self.frame, width=400, height=300)
        self.canvas.pack()

        self.button = Button(self.frame, text="Mostrar Histograma", command=self.show_histogram)
        self.button.pack()
    def setup(self):

        listacsv=['users.csv', 'reservas.csv', 'room.csv','buffet.csv', 'tareas.csv', 'pedidos.csv','ingresos.csv','inversion.csv']
        for carpeta in listacsv:
            self.discoDuro.leerSETUP(carpeta)
            
    def show_histogram(self):
        plt.hist(self.data)
        plt.xlabel("Valores")
        plt.ylabel("Frecuencia")
        plt.title("Histograma")
        plt.show()

    def run(self):
        self.root.mainloop()

# Ejemplo de uso
data = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 10]
            
instance=HistogramGUI(data)
instance.setup()
instance.run()
