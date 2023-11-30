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
   
   def setup(self):

      listacsv=['proyectos_2015.csv','proyectos_2016.csv','proyectos_2017.csv','proyectos_2018.csv','proyecto_disciplina.csv','proyecto_participante.csv','ref_disciplina.csv','ref_estado_proyecto.csv','ref_funcion.csv','ref_moneda.csv','ref_tipo_proyecto.csv']
      for carpeta in listacsv:
         self.discoDuro.leerSETUP(carpeta)