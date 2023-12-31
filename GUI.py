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
        self.ruta_imagen = "../fotoArg.png"  
        self.imagen_fondo = tk.PhotoImage(file=self.ruta_imagen)

        # Crear un widget Canvas para la imagen de fondo
        self.canvas = tk.Canvas(self.ventana, width=self.ancho_ventana, height=self.alto_ventana)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0,anchor="nw" ,image=self.imagen_fondo)

        #valores elegidos en los combobox
        self.valoreselegidos={}
        
    #   Metodo modularizado de creacion de texto    
    def agregar_texto(self,texto, relx, rely):
        label = tk.Label(self.ventana, text=texto, font=("Arial", 12), fg="black", width=100)
        label.place(relx=relx, rely=rely,anchor="center")

    #   Metodo modularizado de creacion de combobox
    def crear_combobox(self, clavecombobox, opciones, rely_combobox):
        self.valoreselegidos[clavecombobox] = tk.StringVar()
        combobox = ttk.Combobox(self.ventana, width=80, values=opciones)
        combobox.place(relx=0.5, rely=rely_combobox, anchor="center")
        combobox.bind("<KeyRelease>", lambda event, opciones=opciones,clave=clavecombobox: self.filtrar_combobox(event, opciones,clave))
        combobox.bind("<<ComboboxSelected>>",lambda event, clave=clavecombobox: self.on_select(event,clave))
    
    def filtrar_combobox(self, event, opciones, clavecombobox):
        texto_ingresado = event.widget.get().lower()
        self.ventana.after(200, lambda: self.actualizar_combobox(event, opciones, texto_ingresado, clavecombobox))

    def actualizar_combobox(self, event, opciones, texto_ingresado, clavecombobox):
        opciones_filtradas = [opcion for opcion in opciones if texto_ingresado in opcion.lower()]
        event.widget['values'] = opciones_filtradas
        self.valoreselegidos[clavecombobox].set(texto_ingresado)
        event.widget.event_generate('<Down>')
    
    # Metodo modularizado de creacion de botones    
    def crear_boton(self,texto,relx_boton,rely_boton,funcion):
        boton = tk.Button(self.ventana, text=texto, bg="black", fg="white", command=funcion)
        boton.place(relx=relx_boton, rely=rely_boton, anchor="center")
        self.aplicar_efecto_brillo(boton)
    def crear_boton2(self,texto,relx_boton,rely_boton,funcion):
        boton = tk.Button(self.ventana, text=texto, bg="red", fg="white", command=funcion)
        boton.place(relx=relx_boton, rely=rely_boton, anchor="center")
        self.aplicar_efecto_brillo2(boton)

    def on_select(self, event, clavecombobox):
        self.valoreselegidos[clavecombobox].set(event.widget.get())

    
    # FUNCIONES A USAR
    def histograma1(self,categoria):
        self.backend.analisis.areas(categoria)
    def histograma2(self):
        self.backend.analisis.gran_areas()
    def histograma3(self,categoria):
        self.backend.analisis.disciplinasgrafico(categoria)
    def grafico_de_tortas(self,categoria,pin):
        #elige el grafico a mostrar segun el pin
        match pin:
            case 0:
                self.backend.analisis.porcentaje_participacion_gran_areas(categoria)
            case 1:
                self.backend.analisis.porcentaje_participacion_disciplinas(categoria)
            case 2:
                self.backend.analisis.porcentaje_participacion_areas(categoria)
            case 3:
                self.backend.analisis.porcentaje_proyectos_tecnologia()
            case 4:
                self.backend.analisis.porcentaje_participacion_generos()



    def mostrar_popup(self, categoria):
        self.backend.analisis.tiempo_promedio_proyectos_gran_area(categoria)
    
    def mostrar_proyectos(self):
        self.backend.analisis.lista_proyectos_fecha()
    
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
        from GUI import instance
        # Aca creo varios textos de manera dinamica y que reutilizo codigo al haber modularizado la creacion de los mismos
        self.agregar_texto("Bienvenido al Centro de Computo de la Nacion Argentina", 0.5, 0.05)
        self.agregar_texto("Seleccione el gran area de su interes", 0.5, 0.1)
        self.agregar_texto("Seleccione el area de su interes", 0.5, 0.25)
        self.agregar_texto("Seleccione la disciplina de su interes", 0.5, 0.4)
        self.agregar_texto("Seleccione la funcion de su interes", 0.5, 0.65)

        # Aca creo varios combobox y sus botones correspondientes de manera dinamica y que reutilizo codigo al haber modularizado la creacion de los mismos
        self.crear_combobox(1,list(self.backend.cache.lista_Gran_Areas), 0.15)
        self.crear_boton("Ver Distribucion en el Gran Area seleccionada",0.2,0.2,lambda valorelegido=self.valoreselegidos[1]: self.histograma1(valorelegido.get()))
        self.crear_boton("% Hombre/Mujer",0.5,0.2,lambda valorelegido=self.valoreselegidos[1]: self.grafico_de_tortas(valorelegido.get(),0))
        self.crear_boton("Tiempo Promedio Finalizacion",0.8,0.2,lambda valorelegido=self.valoreselegidos[1]: instance.backend.analisis.tiempo_promedio_proyectos_gran_area(valorelegido.get()))
        
        self.crear_combobox(2,list(self.backend.cache.lista_Areas), 0.3)
        self.crear_boton("Ver Distribucion en el Area seleccionada",0.2,0.35,lambda valorelegido=self.valoreselegidos[2]: self.histograma3(valorelegido.get()))
        self.crear_boton("% Hombre/Mujer",0.5,0.35,lambda valorelegido=self.valoreselegidos[2]: self.grafico_de_tortas(valorelegido.get(),2))
        self.crear_boton("Tiempo Promedio Finalizacion",0.8,0.35,lambda valorelegido=self.valoreselegidos[2]:instance.backend.analisis.tiempo_promedio_proyectos_area(valorelegido.get()))
        
        self.crear_combobox(3,(list(self.backend.cache.lista_Disciplinas)),0.45)
        self.crear_boton("% Hombre/Mujer",0.5,0.5,lambda valorelegido=self.valoreselegidos[3]: self.grafico_de_tortas(valorelegido.get(),1))
        

       #CREACION DE BOTONES
        self.crear_boton('Tecnologias empleadas',0.2,0.82,lambda:self.grafico_de_tortas(0,3))
        self.crear_boton("Ver Distribucion General",0.2,0.75,self.histograma2)
        self.crear_boton('Participacion generos general',0.5,0.75,lambda :self.grafico_de_tortas(0,4))
        self.crear_boton2("Salir",0.8,0.9,lambda:self.ventana.destroy())
        self.crear_boton('Ver Proyectos',0.8,0.75,lambda:self.mostrar_proyectos())
        self.crear_boton('Developers',0.5,0.82,lambda:self.backend.histogramas.creators())
        self.crear_boton('Ver Financiacion Proyectos',0.8,0.82,lambda:self.backend.analisis.lista_proyectos_financiacion())
        self.ventana.mainloop()
        
        

# Crear una instancia de la clase GUI y ejecutar la aplicación
instance= GUI()


