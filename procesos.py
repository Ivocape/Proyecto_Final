import datetime
import pandas as pd
class Proyecto:
    def __init__ (self, proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director):
        self.proyecto_id=proyecto_id
        self.fuente=fuente
        self.titulo=titulo
        self.fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y/%m/%d %H:%M:%S.%f')
        if fecha_fin == "":
            self.fecha_fin = ''
        else: 
            self.fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y/%m/%d %H:%M:%S.%f')
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.resumen=resumen
        self.moneda_id=moneda_id
        self.monto_total_solicitado=float(monto_total_solicitado)
        self.monto_total_adjudicado=float(monto_total_adjudicado)
        self.monto_financiado_solicitado=float(monto_financiado_solicitado)
        self.monto_financiado_adjudicado=float(monto_financiado_adjudicado)
        self.tipo_proyecto_id=tipo_proyecto_id
        self.codigo_identificacion=codigo_identificacion
        self.palabras_clave=palabras_clave
        self.estado_id=estado_id
        self.fondo_anpcyt=fondo_anpcyt
        self.cantidad_miembros_F=int(cantidad_miembros_F)
        self.cantidad_miembros_M=int(cantidad_miembros_M)
        self.sexo_director=sexo_director

class Disciplina:
    def __init__(self,disciplina_id,gran_area_codigo,gran_area_descripcion,area_codigo,area_descripcion,disciplina_codigo,disciplina_descripcion):
        self.disciplina_id=disciplina_id
        self.gran_area_codigo=gran_area_codigo
        self.gran_area_descripcion=gran_area_descripcion
        self.area_codigo=area_codigo
        self.area_descripcion=area_descripcion
        self.disciplina_codigo=disciplina_codigo
        self.disciplina_descripcion=disciplina_descripcion
class Estado_proyecto:
    def __init__(self,estado_id,estado_descripcion):
        self.estado_id=estado_id
        self.estado_descripcion=estado_descripcion
class Funcion:
    def __init__(self,funcion_id,funcion_descripcion):
        self.funcion_id=funcion_id
        self.funcion_descripcion=funcion_descripcion
class Moneda:
    def __init__(self,moneda_id,moneda_descripcion,codigo_iso):
        self.moneda_id=moneda_id
        self.moneda_descripcion=moneda_descripcion
        self.codigo_iso=codigo_iso
class Tipo_proyecto:
    def __init__(self,id,sigla,descripcion,tipo_proyecto_id,tipo_proyecto_descripcion):
        self.id=id
        self.sigla=sigla
        self.descripcion=descripcion
        self.tipo_proyecto_id=tipo_proyecto_id
        self.tipo_proyecto_descripcion=tipo_proyecto_descripcion    
class Proyecto_disciplina:
    def __init__(self,proyecto_id,disciplina_id):
        self.proyecto_id=proyecto_id
        self.disciplina_id=disciplina_id
class Proyecto_participante:
    def __init__(self,proyecto_id,participante_id,funcion_id,fecha_inicio,fecha_fin):
        self.proyecto_id=proyecto_id
        self.participante_id=participante_id
        self.funcion_id=funcion_id
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        
       


class Cache:
    def __init__(self):
        self.proyec2015=set()
        self.proyec2016=set()
        self.proyec2017=set()
        self.proyec2018=set()
        self.proyectotal=set()
        self.ref_disciplina=set()
        self.ref_estado_proyecto=set()
        self.ref_funcion=set()
        self.ref_moneda=set()
        self.ref_tipo_proyecto=set()
        self.proyecto_disciplina=set()
        self.proyecto_participante=set()
        #listas para combobox
        self.lista_Gran_Areas=set()
        self.lista_Areas=set()
        self.lista_Disciplinas=set()
    def cargar(self,año,proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director):
        if cantidad_miembros_F=='':
            cantidad_miembros_F=0
        if cantidad_miembros_M=='':
            cantidad_miembros_M=0
        proyecto=Proyecto(proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director)
        
        if año==2015:
            self.proyec2015.add(proyecto)
            self.proyectotal.add(proyecto)
        elif año==2016:
            self.proyec2016.add(proyecto)
            self.proyectotal.add(proyecto)
        elif año==2017:
            self.proyec2017.add(proyecto)
            self.proyectotal.add(proyecto)
        elif año==2018:
            self.proyec2018.add(proyecto)
            self.proyectotal.add(proyecto)
        else:
            print("Año incorrecto")
    def cargar_disciplina(self,disciplina_id,gran_area_codigo,gran_area_descripcion,area_codigo,area_descripcion,disciplina_codigo,disciplina_descripcion):
        disciplina=Disciplina(disciplina_id,gran_area_codigo,gran_area_descripcion,area_codigo,area_descripcion,disciplina_codigo,disciplina_descripcion)
        self.ref_disciplina.add(disciplina)   
        #Creo listas para Combobox
        if disciplina.gran_area_descripcion == 'SIN DATOS':
            pass
        else:
            self.lista_Gran_Areas.add(disciplina.gran_area_descripcion)
        if disciplina.area_descripcion == 'SIN DATOS':
            pass
        else:
            self.lista_Areas.add(disciplina.area_descripcion)
        if disciplina.disciplina_descripcion == 'SIN DATOS':
            pass
        else:
            self.lista_Disciplinas.add(disciplina.disciplina_descripcion)

    def cargar_estado_proyecto(self,estado_id,estado_descripcion):
        estado=Estado_proyecto(estado_id,estado_descripcion)
        self.ref_estado_proyecto.add(estado)
    def cargar_funcion(self,funcion_id,funcion_descripcion):
        funcion=Funcion(funcion_id,funcion_descripcion)
        self.ref_funcion.add(funcion)
    def cargar_moneda(self,moneda_id,moneda_descripcion,codigo_iso):
        moneda=Moneda(moneda_id,moneda_descripcion,codigo_iso)
        self.ref_moneda.add(moneda)
    def cargar_tipo_proyecto(self,id,sigla,descripcion,tipo_proyecto_id,tipo_proyecto_descripcion):
        tipo_proyecto=Tipo_proyecto(id,sigla,descripcion,tipo_proyecto_id,tipo_proyecto_descripcion)
        self.ref_tipo_proyecto.add(tipo_proyecto)
    def cargar_proyecto_disciplina(self,proyecto_id,disciplina_id):
        proyecto_disciplina=Proyecto_disciplina(proyecto_id,disciplina_id)
        self.proyecto_disciplina.add(proyecto_disciplina)
    def cargar_proyecto_participante(self,proyecto_id,participante_id,funcion_id,fecha_inicio,fecha_fin):
        proyecto_participante=Proyecto_participante(proyecto_id,participante_id,funcion_id,fecha_inicio,fecha_fin)
        self.proyecto_participante.add(proyecto_participante)     
            

     
 





