import tkinter as tk
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

        # Crear los botones y aplicar el efecto de brillo a cada uno
        self.boton1 = tk.Button(self.ventana, text="distribución de los proyectos por área de investigación", bg="black", fg="white", command=self.on_button_click)
        self.boton1.place(relx=0.5, rely=0.3, anchor="center")  # Posiciona el botón en el centro
        self.aplicar_efecto_brillo(self.boton1)  # Aplicar el efecto de brillo al botón

        self.boton2 = tk.Button(self.ventana, text="porcentaje de participación de las mujeres en los diferentes proyectos según el rol quedesempeña", bg="black", fg="white", command=self.on_button_click)
        self.boton2.place(relx=0.5, rely=0.4, anchor="center")  # Posiciona el botón en el centro
        self.aplicar_efecto_brillo(self.boton2)  # Aplicar el efecto de brillo al botón

        self.boton3 = tk.Button(self.ventana, text="tiempo promedio de terminación", bg="black", fg="white", command=self.on_button_click)
        self.boton3.place(relx=0.5, rely=0.5, anchor="center")  # Posiciona el botón en el centro
        self.aplicar_efecto_brillo(self.boton3)

        self.boton4 = tk.Button(self.ventana, text="porcentaje de proyectos que han utilizado tecnologías emergentes", bg="black", fg="white", command=self.on_button_click)
        self.boton4.place(relx=0.5, rely=0.6, anchor="center")  # Posiciona el botón en el centro
        self.aplicar_efecto_brillo(self.boton4)

        self.boton5 = tk.Button(self.ventana, text="lista de proyectos", bg="black", fg="white", command=self.on_button_click)
        self.boton5.place(relx=0.5, rely=0.7, anchor="center")  # Posiciona el botón en el centro
        self.aplicar_efecto_brillo(self.boton5)

        self.boton6 = tk.Button(self.ventana, text="Financiamiento Solicitado/Otorgado", bg="black", fg="white", command=self.on_button_click)
        self.boton6.place(relx=0.5, rely=0.8, anchor="center")  # Posiciona el botón en el centro
        self.aplicar_efecto_brillo(self.boton6)

        self.boton7 = tk.Button(self.ventana, text="Cerrar", bg="black", fg="white", command=self.ventana.destroy) 
        self.boton7.place(relx=0.5, rely=0.9, anchor="center")  # Posiciona el botón en el centro
        self.aplicar_efecto_brillo(self.boton7)
        
    def toggle_fullscreen(window):
        window.attributes("-fullscreen", True)

    def on_button_click(self):
        print("Botón clickeado")

    def on_enter(self, event):
        event.widget.config(bg='gray')  # Cambiar color al pasar el mouse

    def on_leave(self, event):
        event.widget.config(bg='black')  # Restaurar color al quitar el mouse

    def aplicar_efecto_brillo(self, boton):
        boton.bind("<Enter>", self.on_enter)
        boton.bind("<Leave>", self.on_leave)

    def run(self):
        self.backend.setup()
        self.ventana.mainloop()

# Crear una instancia de la clase GUI y ejecutar la aplicación
instance= GUI()

#####################################################################################
# + Para llamar al backend y ejecutar sus distintas funciones no estando en este archivo (self.backend en este caso)
# debo llamar de la siguiente manera: instance.backend.funcion() (donde funcion es la funcion que quiero ejecutar)
#####################################################################################
