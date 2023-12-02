from histogramas import *
class Analisis:
    def __init__(self):
        self.cantidad_mujeres = 0
        self.cantidad_hombres = 0
        self.listaareascodigo=[]
        self.listaareas=set()
    
    def __str__(self) -> str:
        return 
    

    def porcentaje_participacion_generos(self):
     
        from GUI import instance  # Esto puede causar problemas de acoplamiento
        for proyecto in instance.backend.cache.proyectotal:
            self.cantidad_mujeres += proyecto.cantidad_miembros_F
            self.cantidad_hombres += proyecto.cantidad_miembros_M
        total = self.cantidad_mujeres + self.cantidad_hombres
        porcentaje_mujeres = (self.cantidad_mujeres * 100) / total
        porcentaje_hombres = (self.cantidad_hombres * 100) / total
        instance.backend.histogramas.grafico_de_tortas(porcentaje_mujeres, porcentaje_hombres)

        
    def porcentaje_participacion_gran_areas(self,gran_area):#Visualizar el porcentaje de participación de las mujeres en los diferentes proyectos según el gran area versus la participación de los hombres.
        from GUI import instance
        
        gran_areas=[disciplina.gran_area_descripcion.upper() for disciplina in instance.backend.cache.ref_disciplina]
        if gran_area.upper() not in gran_areas:
            print("El gran area ingresada no es válida.")
        else:
            cantidad_mujeres=0
            cantidad_hombres=0
            
            for disciplina in instance.backend.cache.ref_disciplina:
                if disciplina.gran_area_descripcion.upper() ==gran_area.upper():
                    id_disciplina=disciplina.disciplina_id
                    for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                        if proyecto_disciplina.disciplina_id==id_disciplina:
                            for proyecto in instance.backend.cache.proyectotal:
                                if proyecto.proyecto_id==proyecto_disciplina.proyecto_id:
                                    cantidad_mujeres+=proyecto.cantidad_miembros_F
                                    cantidad_hombres+=proyecto.cantidad_miembros_M
            
            total=cantidad_mujeres+cantidad_hombres
            if total>0:
                porcentaje_mujeres=(cantidad_mujeres*100)/total
                porcentaje_hombres=(cantidad_hombres*100)/total
                
                print("El porcentaje de mujeres es: ",porcentaje_mujeres)
                print("El porcentaje de hombres es: ",porcentaje_hombres)
            else:
                print("No hay proyectos en el gran area ",gran_area)
        
        
    def porcentaje_participacion_areas(self,area):#Visualizar el porcentaje de participación de las mujeres en los diferentes proyectos según el  area versus la participación de los hombres.
        from GUI import instance
        
        areas=set(disciplina.area_descripcion.upper() for disciplina in instance.backend.cache.ref_disciplina)
        if area.upper() not in areas:
            print('El area ingresada no es válida.')
        else:
            cantidad_mujeres=0
            cantidad_hombres=0
            
            for disciplina in instance.backend.cache.ref_disciplina:
                if disciplina.area_descripcion.upper() ==area.upper():
                    id_disciplina=disciplina.disciplina_id
                    for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                        if proyecto_disciplina.disciplina_id==id_disciplina:
                            for proyecto in instance.backend.cache.proyectotal:
                                if proyecto.proyecto_id==proyecto_disciplina.proyecto_id:
                                    cantidad_mujeres+=proyecto.cantidad_miembros_F
                                    cantidad_hombres+=proyecto.cantidad_miembros_M
        
            total=cantidad_mujeres+cantidad_hombres
            if total>0:
                porcentaje_mujeres=(cantidad_mujeres*100)/total
                porcentaje_hombres=(cantidad_hombres*100)/total
                instance.backend.histogramas.grafico_de_tortas(porcentaje_mujeres, porcentaje_hombres)
                print("El porcentaje de mujeres es: ",porcentaje_mujeres)
                print("El porcentaje de hombres es: ",porcentaje_hombres)
            else:
                print("No hay proyectos en el area",area)    

    def porcentaje_participacion_disciplinas(self,disciplinafiltrar):#Visualizar el porcentaje de participación de las mujeres en los diferentes proyectos según la disciplina versus la participación de los hombres.
        from GUI import instance
        
        disciplinas=[disciplina.disciplina_descripcion.upper() for disciplina in instance.backend.cache.ref_disciplina]
        if disciplinafiltrar.upper() not in disciplinas:
            print("El área ingresada no es válida.")
        else:
            cantidad_mujeres=0
            cantidad_hombres=0
            
            for disciplina in instance.backend.cache.ref_disciplina:
                if disciplina.disciplina_descripcion.upper() ==disciplinafiltrar.upper():
                    id_disciplina=disciplina.disciplina_id
                    for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                        if proyecto_disciplina.disciplina_id==id_disciplina:
                            for proyecto in instance.backend.cache.proyectotal:
                                if proyecto.proyecto_id==proyecto_disciplina.proyecto_id:
                                    cantidad_mujeres+=proyecto.cantidad_miembros_F
                                    cantidad_hombres+=proyecto.cantidad_miembros_M
            
            total=cantidad_mujeres+cantidad_hombres
            if total>0:
                porcentaje_mujeres=(cantidad_mujeres*100)/total
                porcentaje_hombres=(cantidad_hombres*100)/total
                print("El porcentaje de mujeres es: ",porcentaje_mujeres)
                print("El porcentaje de hombres es: ",porcentaje_hombres)
            else:
                print("No hay proyectos en la ",disciplinafiltrar)
    
 
    def lista_proyectos_fecha(self):#guardar y visualizar una lista de proyectos y la fecha de inicio por la fecha de iniciación del proyecto creciente.
        lista=[]
        from GUI import instance  
        for proyecto in instance.backend.cache.proyectotal:
            lista.append((proyecto.fecha_inicio,proyecto.titulo))
        lista.sort()
        print(lista)
    
    
    def cantidad_proyectos_gran_area(self,gran_area):# cantidad de proyectos por gran area
        from GUI import instance
        gran_areas=[disciplina.gran_area_descripcion.upper() for disciplina in instance.backend.cache.ref_disciplina]
        if gran_area.upper() not in gran_areas:
            print("El gran area ingresada no es válida.")
        else:
            cantidad=0
            
            for disciplina in instance.backend.cache.ref_disciplina:
                if disciplina.gran_area_descripcion.upper() ==gran_area.upper():
                    id_disciplina=disciplina.disciplina_id
                    for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                        if proyecto_disciplina.disciplina_id==id_disciplina:
                            cantidad+=1
            print("La cantidad de proyectos en el gran area",gran_area,"es:",cantidad)
            instance.backend.histogramas.mostrar_dato(cantidad)

    def cantidad_proyectos_area(self,area):# cantidad de proyectos por  area
        from GUI import instance
        
        areas=set(disciplina.area_descripcion.upper() for disciplina in instance.backend.cache.ref_disciplina)
        if area.upper() not in areas:
            print('El area ingresada no es válida.')
        else:
            cantidad=0
            from GUI import instance
            for disciplina in instance.backend.cache.ref_disciplina:
                if disciplina.area_descripcion ==area.upper():
                    id_disciplina=disciplina.disciplina_id
                    for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                        if proyecto_disciplina.disciplina_id==id_disciplina:
                            cantidad+=1
            print("La cantidad de proyectos en el gran area",area,"es:",cantidad)
            return cantidad
            

    def cantidad_proyectos_total_areas(self):
        from GUI import instance
        cantidadxarea=[]
        areas=set(disciplina.area_descripcion.upper() for disciplina in instance.backend.cache.ref_disciplina)
        for area in areas:
            
            cantidadxarea.append((area,self.cantidad_proyectos_area(area)))
            

    def areas(self):#lista de areas en los proyectos
        from GUI import instance
        
        for proyecto in instance.backend.cache.proyectotal:
            for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                if proyecto.proyecto_id==proyecto_disciplina.proyecto_id:
                    for disciplina in instance.backend.cache.ref_disciplina:
                        if proyecto_disciplina.disciplina_id==disciplina.disciplina_id:
                            if disciplina.area_descripcion == 'SIN DATOS':
                                pass
                            else:
                                self.listaareascodigo.append(disciplina.area_codigo)
                                self.listaareas.add((disciplina.area_codigo,disciplina.area_descripcion))
        instance.backend.histogramas.histograma_tabla(self.listaareascodigo,self.listaareas)
        

                
        
        
                        
            
    def tiempo_promedio_proyectos_area(self,area): #Visualizar el tiempo promedio de terminación de los proyectos según el área al que pertenecen.
        from GUI import instance
        
        areas=set(disciplina.area_descripcion.upper() for disciplina in instance.backend.cache.ref_disciplina)
        dias=0
        contadorproyectos=0
        if area.upper() not in areas:
            print('El area ingresada no es válida.')
        else:
            for disciplina in instance.backend.cache.ref_disciplina:
                if disciplina.area_descripcion.upper() ==area.upper():
                    id_disciplina=disciplina.disciplina_id
                    for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                        if proyecto_disciplina.disciplina_id==id_disciplina:
                            for proyecto in instance.backend.cache.proyectotal:
                                if proyecto.estado_id=='1' and proyecto.proyecto_id==proyecto_disciplina.proyecto_id:
                                
                                    dias+=(proyecto.fecha_fin-proyecto.fecha_inicio).days
                                    contadorproyectos+=1
            promedio=dias/contadorproyectos
            print("El tiempo promedio de terminacion de los proyectos del area",area,"es:",promedio,'minutos')
            

    def porcentaje_monto_financiamiento(self):#Visualizar que porcentaje del monto de financiamiento solicitado efectivamente se le otorgó, segun el monto financiado adjudicado por proyecto.         lista=[]
        lista_financiamiento_proyectos=[]
        from GUI import instance
        for proyecto in instance.backend.cache.proyectotal:
            if proyecto.monto_financiado_solicitado==0:
                porcentaje_adjudicado=0
                lista_financiamiento_proyectos.append(porcentaje_adjudicado)                
            else:
               porcentaje_adjudicado=(proyecto.monto_financiado_adjudicado*100)/proyecto.monto_financiado_solicitado
               lista_financiamiento_proyectos.append(porcentaje_adjudicado)
            
        print(lista_financiamiento_proyectos)

    def porcentaje_proyectos_tecnologia(self): # Visualizar el porcentaje de proyectos que han utilizado tecnologías emergentes (Tecnología e innovación)
        cantidad=0
        from GUI import instance
        for proyecto in instance.backend.cache.proyectotal:
            for tipo in instance.backend.cache.ref_tipo_proyecto:
                if proyecto.tipo_proyecto_id==tipo.tipo_proyecto_id and tipo.tipo_proyecto_descripcion == 'Tecnología e Innovación': 
                    cantidad+=1
        total=len(instance.backend.cache.proyectotal)
        porcentaje=(cantidad*100)/total
        print("El porcentaje de proyectos de tecnologia es:",porcentaje)


