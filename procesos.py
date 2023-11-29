#Mostrar la distribución de los proyectos por área de investigación (por ejemplo, ciencias sociales,ciencias naturales, tecnología, etc.) y sus correspondientes sub áreas ( por ejemplo de cienciasnaturales las sub áreas de matemáticas, ciencias de la computación, ciencias físicas....)
import pandas as pd
class Proyecto:
    def __init__ (self, proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director):
        self.proyecto_id=proyecto_id
        self.fuente=fuente
        self.titulo=titulo
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.resumen=resumen
        self.moneda_id=moneda_id
        self.monto_total_solicitado=monto_total_solicitado
        self.monto_total_adjudicado=monto_total_adjudicado
        self.monto_financiado_solicitado=monto_financiado_solicitado
        self.monto_financiado_adjudicado=monto_financiado_adjudicado
        self.tipo_proyecto_id=tipo_proyecto_id
        self.codigo_identificacion=codigo_identificacion
        self.palabras_clave=palabras_clave
        self.estado_id=estado_id
        self.fondo_anpcyt=fondo_anpcyt
        self.cantidad_miembros_F=cantidad_miembros_F
        self.cantidad_miembros_M=cantidad_miembros_M
        self.sexo_director=sexo_director                        


class Cache:
    def __init__(self):
        self.proyec2015={}
        self.proyec2016={}
        self.proyec2017={}
        self.proyec2018={}
        self.ref_disciplina={}
        self.ref_estado_proyecto={}
        self.ref_funcion={}
        self.ref_moneda={}
        self.ref_tipo_proyecto={}
        self.proyecto_disciplina={}
        self.proyecto_participante={}
        
    def cargar(self,año,proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director):
        proyecto=Proyecto(proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director)
        if año==2015:
            self.proyec2015.add(proyecto)
        elif año==2016:
            self.proyec2016.add(proyecto)
        elif año==2017:
            self.proyec2017.add(proyecto)
        elif año==2018:
            self.proyec2018.add(proyecto)
        else:
            print("Año incorrecto")
            