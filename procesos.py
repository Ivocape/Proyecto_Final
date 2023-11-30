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

class Disciplina:
    def __init__(self,disciplina_id,gran_area_codigo,gran_area_descripcion,area_codigo,area_descripcion,disciplina_codigo,disciplina_descripcion):
        self.disciplina_id=disciplina_id
        self.gran_area_codigo=gran_area_codigo
        self.gran_area_descripcion=gran_area_descripcion
        self.area_codigo=area_codigo
        self.area_descripcion=area_descripcion
        self.disciplina_codigo=disciplina_codigo
        self.disciplina_descripcion=disciplina_descripcion
                       
class Cache:
    def __init__(self):
        self.proyec2015={}
        self.proyec2016={}
        self.proyec2017={}
        self.proyec2018={}
        self.proyectotal={}
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
    def cargar_estado_proyecto(self,estado_id,estado_descripcion):
        self.ref_estado_proyecto.add(estado_id,estado_descripcion)
    def cargar_funcion(self,funcion_id,funcion_descripcion):
        self.ref_funcion.add(funcion_id,funcion_descripcion)
    def cargar_moneda(self,moneda_id,moneda_descripcion):
        self.ref_moneda.add(moneda_id,moneda_descripcion)
    def cargar_tipo_proyecto(self,tipo_proyecto_id,tipo_proyecto_descripcion):
        self.ref_tipo_proyecto.add(tipo_proyecto_id,tipo_proyecto_descripcion)
    def cargar_proyecto_disciplina(self,proyecto_id,disciplina_id):
        self.proyecto_disciplina.add(proyecto_id,disciplina_id)
    def cargar_proyecto_participante(self,proyecto_id,participante_id):
        self.proyecto_participante.add(proyecto_id,participante_id)     
            
class Analisis:
    def __init__(self):
        pass

    #Visualizar el porcentaje de participación de las mujeres en los diferentes proyectos según el rol que desempeñan versus la participación de los hombres.
    def porcentaje_participacion_generos(self):
        cantidad_mujeres=0
        cantidad_hombres=0
        for proyecto in self.proyectotal:
            cantidad_mujeres+=proyecto.cantidad_miembros_F
            cantidad_hombres+=proyecto.cantidad_miembros_M
        total=cantidad_mujeres+cantidad_hombres
        porcentaje_mujeres=(cantidad_mujeres*100)/total
        porcentaje_hombres=(cantidad_hombres*100)/total
        print("El porcentaje de mujeres es: ",porcentaje_mujeres)
        print("El porcentaje de hombres es: ",porcentaje_hombres)
        
        #Visualizar el porcentaje de participación de las mujeres en los diferentes proyectos según el gran area en el que estan versus la participación de los hombres.
    def porcentaje_participacion_gran_areas(self,gran_area):    
        cantidad_mujeres=0
        cantidad_hombres=0
        from GUI import cache
        for disciplina in self.ref_disciplina:
            if disciplina.gran_area_descripcion==gran_area:
                id_disciplina=disciplina.disciplina_id
        for proyecto in self.proyectotal:
            if proyecto.tipo_proyecto_id==id_disciplina:
                cantidad_mujeres+=proyecto.cantidad_miembros_F
                cantidad_hombres+=proyecto.cantidad_miembros_M
        total=cantidad_mujeres+cantidad_hombres
        porcentaje_mujeres=(cantidad_mujeres*100)/total
        porcentaje_hombres=(cantidad_hombres*100)/total
        print("El porcentaje de mujeres es: ",porcentaje_mujeres)
        print("El porcentaje de hombres es: ",porcentaje_hombres)

    def porcentaje_participacion_areas(self,area):
        #Visualizar el porcentaje de participación de las mujeres en los diferentes proyectos según el area de investigación que desempeñan versus la participación de los hombres.
        cantidad_mujeres=0
        cantidad_hombres=0
        from GUI import cache
        for disciplina in self.ref_disciplina:
            if disciplina.disciplina_descripcion==area:
                id_disciplina=disciplina.disciplina_id
        for proyecto in self.proyectotal:
            if proyecto.tipo_proyecto_id==id_disciplina:
                cantidad_mujeres+=proyecto.cantidad_miembros_F
                cantidad_hombres+=proyecto.cantidad_miembros_M
        total=cantidad_mujeres+cantidad_hombres
        porcentaje_mujeres=(cantidad_mujeres*100)/total
        porcentaje_hombres=(cantidad_hombres*100)/total
        print("El porcentaje de mujeres es: ",porcentaje_mujeres)
        print("El porcentaje de hombres es: ",porcentaje_hombres)

#Visualizar el porcentaje de participación de las mujeres en los diferentes proyectos según la discplina versus la participación de lso hombres.
    def porcentaje_participacion_disciplinas(self,disciplina):
        cantidad_mujeres=0
        cantidad_hombres=0
        from GUI import cache
        for disciplina in self.ref_disciplina:
            if disciplina.disciplina_descripcion==disciplina:
                id_disciplina=disciplina.disciplina_id
        for proyecto in self.proyectotal:
            if proyecto.tipo_proyecto_id==id_disciplina:
                cantidad_mujeres+=proyecto.cantidad_miembros_F
                cantidad_hombres+=proyecto.cantidad_miembros_M
        total=cantidad_mujeres+cantidad_hombres
        porcentaje_mujeres=(cantidad_mujeres*100)/total
        porcentaje_hombres=(cantidad_hombres*100)/total
        print("El porcentaje de mujeres es: ",porcentaje_mujeres)
        print("El porcentaje de hombres es: ",porcentaje_hombres)
    
    #guardar y visualizar una lista de proyectos y la fecha de inicio por la fecha de iniciación del proyecto creciente.
    def lista_proyectos_fecha(self):
        lista=[]
        for proyecto in self.proyectotal:
            lista.append((proyecto.fecha_inicio,proyecto.titulo))
        lista.sort()
        print(lista)

#Mostrar la distribución de los proyectos por área de investigación (por ejemplo, ciencias sociales,ciencias naturales, tecnología, etc.) y sus correspondientes sub áreas ( por ejemplo de cienciasnaturales las sub áreas de matemáticas, ciencias de la computación, ciencias físicas....)

# cantidad de proyectos por gran area
    def cantidad_proyectos_gran_area(self,gran_area):
        cantidad=0
        from GUI import cache
        for disciplina in self.ref_disciplina:
            if disciplina.gran_area_descripcion==gran_area:
                id_disciplina=disciplina.disciplina_id
        for proyecto in self.proyectotal:
            if proyecto.tipo_proyecto_id==id_disciplina:
                cantidad+=1
        print("La cantidad de proyectos en el gran area ",gran_area," es: ",cantidad)

# cantidad de proyectos por area
    def cantidad_proyectos_area(self,area):
        cantidad=0
        from GUI import cache
        for disciplina in self.ref_disciplina:
            if disciplina.area_descripcion==area:
                id_disciplina=disciplina.disciplina_id
        for proyecto in self.proyectotal:
            if proyecto.tipo_proyecto_id==id_disciplina:
                cantidad+=1
        print("La cantidad de proyectos en el area ",area," es: ",cantidad)
     
#Visualizar el tiempo promedio de terminación de los proyectos según el área al que pertenecen.
    def tiempo_promedio_proyectos_area(self,area):
        from GUI import cache
        for disciplina in self.ref_disciplina:
            if disciplina.area_descripcion==area:
                id_disciplina=disciplina.disciplina_id
        lista=[]
        for proyecto in self.proyectotal:
            if proyecto.tipo_proyecto_id==id_disciplina:
                lista.append(proyecto.fecha_fin-proyecto.fecha_inicio)
        promedio=sum(lista)/len(lista)
        print("El tiempo promedio de terminacion de los proyectos del area ",area," es: ",promedio) 



