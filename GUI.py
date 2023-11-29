from procesos import *
from discoDuro import *
from menus import *
from tkinter import *

class App:
    def __init__(self):
        
        self.discoDuro=DiscoDuro()
        self.cache=Cache()
    
    def setup(self):
        listacsv=['users.csv', 'reservas.csv', 'room.csv','buffet.csv', 'tareas.csv', 'pedidos.csv','ingresos.csv','inversion.csv']
        for carpeta in listacsv:
            self.discoDuro.leerSETUP(carpeta)
            
            
instance=App()
instance.setup()
instance.run()