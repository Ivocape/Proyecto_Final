# Description: Clase que contiene los objetos de las clases que se encargan de la logica del programa
from procesos import *
from discoDuro import *
from menus import *
from analisis import *
from histogramas import *
class Backend ():
     def __init__(self):
        self.discoDuro=DiscoDuro()
        self.cache=Cache()
        self.histogramas=histogramas()
        self.analisis=Analisis()
