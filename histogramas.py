import matplotlib.pyplot as plt
from procesos import *

class histogramas():
    def __init__(self):
      pass
    def show_histogram(self, data):
        plt.hist()
        plt.xlabel("Valores")
        plt.ylabel("Frecuencia")
        plt.title("Histograma")
        plt.show()
