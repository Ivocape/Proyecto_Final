import tkinter as tk
from tkinter import ttk
from backend import Backend
class GUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.backend = Backend()
        self.ventana.title("CENTRO DE COMPUTO DE LA NACION ARGENTINA")
       
        # Configurar las dimensiones de la ventana
        self.ancho_ventana = 700
        self.alto_ventana = 600
        self.ventana.geometry(f"{self.ancho_ventana}x{self.alto_ventana}")
       
        # Cargar la imagen de fondo
        self.ruta_imagen = "fotoArg.png"  # Reemplaza con la ruta de tu imagen
        self.imagen_fondo = tk.PhotoImage(file=self.ruta_imagen)

        # Crear un widget Canvas para la imagen de fondo
        self.canvas = tk.Canvas(self.ventana, width=self.ancho_ventana, height=self.alto_ventana)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0,anchor="nw" ,image=self.imagen_fondo)

    #   Metodo modularizado de creacion de texto    
    def agregar_texto(self,texto, relx, rely):
        label = tk.Label(self.ventana, text=texto, font=("Arial", 12), fg="black", width=100)
        label.place(relx=relx, rely=rely,anchor="center")

    #   Metodo modularizado de creacion de combobox y sus botones correspondientes
    def crear_combobox(self, opciones, rely_combobox, texto_boton,relx_boton ,rely_boton,pin):
        valorelegido = tk.StringVar()
        combobox = ttk.Combobox(self.ventana, width=80, values=opciones)
        combobox.place(relx=0.5, rely=rely_combobox, anchor="center")
        combobox.bind("<<ComboboxSelected>>", lambda event, valorelegido=valorelegido: self.on_select(event, valorelegido))
        
        self.crear_boton(texto_boton,relx_boton,rely_boton,lambda valorelegido=valorelegido: self.grafico_de_tortas(valorelegido.get(),pin))
        
    def crear_boton(self,texto,relx_boton,rely_boton,funcion):
        boton = tk.Button(self.ventana, text=texto, bg="black", fg="white", command=funcion)
        boton.place(relx=relx_boton, rely=rely_boton, anchor="center")
        self.aplicar_efecto_brillo(boton)
    def crear_boton2(self,texto,relx_boton,rely_boton,funcion):
        boton = tk.Button(self.ventana, text=texto, bg="red", fg="white", command=funcion)
        boton.place(relx=relx_boton, rely=rely_boton, anchor="center")
        self.aplicar_efecto_brillo2(boton)

    def on_select(self, event, valorelegido):
        valorelegido.set(event.widget.get())

    def histograma1(self):
        self.backend.analisis.areas()
    def grafico_de_tortas(self,area,pin):
        #elige el grafico a mostrar segun el pin
        match pin:
            case 0:
                self.backend.analisis.porcentaje_participacion_areas(area)
            case 1:
                self.backend.analisis.porcentaje_participacion_disciplinas(area)
    def mostrar_data(self):
        self.backend.analisis.cantidad_proyectos_gran_area("CIENCIAS NATURALES Y EXACTAS")
        
    def on_enter(self, event):
        event.widget.config(bg='gray')  # Cambiar color al pasar el mouse
    def on_leave(self, event):
        event.widget.config(bg='black')  # Restaurar color al quitar el mouse
    def on_enter2(self, event):
        event.widget.config(bg='orange')
    def on_leave2(self, event):
        event.widget.config(bg='red')  

    def aplicar_efecto_brillo(self, boton):
        boton.bind("<Enter>", self.on_enter)
        boton.bind("<Leave>", self.on_leave)
    def aplicar_efecto_brillo2(self, boton):
        boton.bind("<Enter>", self.on_enter2)
        boton.bind("<Leave>", self.on_leave2)

    def run(self):
        # Aca creo varios textos de manera dinamica y que reutilizo codigo al haber modularizado la creacion de los mismos
        self.agregar_texto("Bienvenido al Centro de Computo de la Nacion Argentina", 0.5, 0.05)
        self.agregar_texto("Seleccione el area de su interes", 0.5, 0.1)
        self.agregar_texto("Seleccione la disciplina de su interes", 0.5, 0.25)
        self.agregar_texto("Seleccione la funcion de su interes", 0.5, 0.45)

        # Aca creo varios combobox y sus botones correspondientes de manera dinamica y que reutilizo codigo al haber modularizado la creacion de los mismos
        self.crear_combobox(list(self.backend.cache.lista_Areas), 0.15, "% Hombre/Mujer",0.45 ,0.2,0)
        self.crear_combobox((list(self.backend.cache.lista_Disciplinas)), 0.3, "% Hombre/Mujer", 0.45,0.35,1)
        
        self.crear_boton("Ver Histograma",0.2,0.2,self.histograma1)
        self.crear_boton("Tiempo Promedio Finalizacion",0.8,0.2,self.histograma1)#cambiar funcion

        self.crear_boton("Ver Histograma",0.2,0.35,self.histograma1)
        self.crear_boton("Tiempo Promedio Finalizacion",0.8,0.35,self.histograma1)#cambiar funcion

        self.crear_boton("Ver Data",0.2,0.5,self.mostrar_data)
        self.crear_boton("Ver Histograma",0.45,0.5,self.histograma1)     
        self.crear_boton2("Salir",0.7,0.5,quit)
        self.ventana.mainloop()

# Crear una instancia de la clase GUI y ejecutar la aplicación
instance= GUI()

#####################################################################################
# + Para llamar al backend y ejecutar sus distintas funciones no estando en este archivo (self.backend en este caso)
# debo llamar de la siguiente manera: instance.backend.funcion() (donde funcion es la funcion que quiero ejecutar)
#####################################################################################
