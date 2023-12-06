
class Analisis:
    def __init__(self):
        self.cantidad_mujeres = 0
        self.cantidad_hombres = 0
        
    
    def __str__(self) -> str:
        return 
    
    #Porcentaje de participacion de las mujeres en los diferentes proyectos versus la participación de los hombres en todos los proyectos.
    def porcentaje_participacion_generos(self):
     
        from GUI import instance 
        for proyecto in instance.backend.cache.proyectotal:
            self.cantidad_mujeres += proyecto.cantidad_miembros_F
            self.cantidad_hombres += proyecto.cantidad_miembros_M
        total = self.cantidad_mujeres + self.cantidad_hombres
        porcentaje_mujeres = (self.cantidad_mujeres * 100) / total
        porcentaje_hombres = (self.cantidad_hombres * 100) / total
        instance.backend.histogramas.grafico_de_tortas(porcentaje_mujeres, porcentaje_hombres,"porcentaje de Mujeres ","Porcentaje de Hombres",'Distribucion de generos')

    #Porcentaje de participación de las mujeres en los diferentes proyectos según el GRAN AREA versus la participación de los hombres.
    def porcentaje_participacion_gran_areas(self,gran_area):
        from GUI import instance
        
        gran_areas=[disciplina.gran_area_descripcion.upper() for disciplina in instance.backend.cache.ref_disciplina]
        if gran_area.upper() not in gran_areas:
            
            instance.backend.histogramas.mostrar_popup('El area ingresada no es válida.') 
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
                instance.backend.histogramas.grafico_de_tortas(porcentaje_mujeres, porcentaje_hombres,"Porcentaje de Mujeres ","Porcentaje de Hombres",'Distribucion de generos en el gran area: '+gran_area)

            else:
                instance.backend.histogramas.mostrar_popup("No hay proyectos en el gran area: " + gran_area)


# Porcentaje de participación de las mujeres en los diferentes proyectos según el AREA (sub area) versus la participación de los hombres.
    def porcentaje_participacion_areas(self,area):
        
        from GUI import instance
        
        areas=set(disciplina.area_descripcion.upper() for disciplina in instance.backend.cache.ref_disciplina)
        if area.upper() not in areas:
            
            instance.backend.histogramas.mostrar_popup('El area ingresada no es válida.') 
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
                # linkeo a histogramas Grafico de tortas
                instance.backend.histogramas.grafico_de_tortas(porcentaje_mujeres, porcentaje_hombres,"Porcentaje de Mujeres ","Porcentaje de Hombres",'Distribucion de generos en el sub area: ' +area)
                
            else:
                instance.backend.histogramas.mostrar_popup('No hay proyectos en el area: '+ area)
                

 
 # Porcentaje de participación de las mujeres en los diferentes proyectos según la disciplina versus la participación de los hombres.
    def porcentaje_participacion_disciplinas(self,disciplinafiltrar):
        from GUI import instance
        
        disciplinas=[disciplina.disciplina_descripcion.upper() for disciplina in instance.backend.cache.ref_disciplina]
        if disciplinafiltrar.upper() not in disciplinas:
            instance.backend.histogramas.mostrar_popup('La disciplina ingresada no es válida.')
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
                #linkeo a histogramas Grafico de tortas
                instance.backend.histogramas.grafico_de_tortas(porcentaje_mujeres, porcentaje_hombres,"Porcentaje de Mujeres ","Porcentaje de Hombres",'Distribucion de generos en la disciplina: '+disciplinafiltrar)   
                
            else:
                
                instance.backend.histogramas.mostrar_popup("No hay proyectos en la disciplina: " + disciplinafiltrar)

         
    #lista de proyectos ordenadas por fechas
    def lista_proyectos_fecha(self):
        lista=[]
        from GUI import instance  
        for proyecto in instance.backend.cache.proyectotal:
            lista.append((proyecto.fecha_inicio,proyecto.titulo))
        lista.sort()
        if not lista:
            instance.backend.histogramas.mostrar_popup('No hay proyectos para mostrar.')
        else:
            
            instance.backend.histogramas.tabla(lista,'Fecha de inicio','Titulo')
            
    # lista de proyectos  mostrando financiacion         
    def lista_proyectos_financiacion(self):
        lista=[]
        from GUI import instance
        for proyecto in instance.backend.cache.proyectotal:
            if proyecto.monto_financiado_solicitado==0:
                porcentaje_adjudicado="No se solicito financiamiento"
                lista.append((porcentaje_adjudicado,proyecto.titulo))

            else:
                porcentaje_adjudicado=str((proyecto.monto_financiado_adjudicado*100)/proyecto.monto_financiado_solicitado)+"%"
                lista.append((porcentaje_adjudicado,proyecto.titulo))
        instance.backend.histogramas.tabla(lista,'Porcentaje de financiamiento adjudicado','Titulo')
    

    
            
    #lista de areas segun el gran area
    def areas(self,gran_area):
        from GUI import instance
        listaareascodigo=[]
        listaareas=set()
        if gran_area in instance.backend.cache.lista_Gran_Areas:    
            for proyecto in instance.backend.cache.proyectotal:
                for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                    if proyecto.proyecto_id==proyecto_disciplina.proyecto_id:
                        for disciplina in instance.backend.cache.ref_disciplina:
                            if proyecto_disciplina.disciplina_id==disciplina.disciplina_id:
                                if disciplina.gran_area_descripcion == gran_area:
                                    if disciplina.area_descripcion == 'SIN DATOS':
                                        pass
                                    else:
                                        listaareascodigo.append(disciplina.area_codigo)
                                        listaareas.add((disciplina.area_codigo,disciplina.area_descripcion))
            if listaareascodigo==[]:
                instance.backend.histogramas.mostrar_popup('No hay proyectos en el Gran area: '+ gran_area)                  
            instance.backend.histogramas.histograma_tabla(listaareascodigo,listaareas,'area')
        else:
            instance.backend.histogramas.mostrar_popup('No existe la gran area:'+ gran_area)
    
    #lista de gran areas en los proyectos    
    def gran_areas(self):
        from GUI import instance
        listagranareascodigo=[]
        listagranareas=set()
        for proyecto in instance.backend.cache.proyectotal:
            for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                if proyecto.proyecto_id==proyecto_disciplina.proyecto_id:
                    for disciplina in instance.backend.cache.ref_disciplina:
                        if proyecto_disciplina.disciplina_id==disciplina.disciplina_id:
                            if disciplina.gran_area_descripcion == 'SIN DATOS':
                               pass
                            else:
                                listagranareascodigo.append(disciplina.gran_area_codigo)
                                listagranareas.add((disciplina.gran_area_codigo,disciplina.gran_area_descripcion))
        if listagranareas==[]:
                instance.backend.histogramas.mostrar_popup('No hay proyectos en el Gran area: ')                  
        instance.backend.histogramas.histograma_tabla(listagranareascodigo,listagranareas,'gran area')
        
    #lista de disciplinas segun el area          
    def disciplinasgrafico(self,area):
            from GUI import instance
            listadisciplinascodigo=[]
            listadisciplinas=set()
            if area not in instance.backend.cache.lista_Areas:
            
                instance.backend.histogramas.mostrar_popup('El area ingresada no es válida.')
            else:
                for proyecto in instance.backend.cache.proyectotal:
                    for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                        if proyecto.proyecto_id==proyecto_disciplina.proyecto_id:
                            for disciplina in instance.backend.cache.ref_disciplina:
                                if proyecto_disciplina.disciplina_id==disciplina.disciplina_id:
                                    if disciplina.area_descripcion == area:
                                        if disciplina.disciplina_descripcion == 'SIN DATOS':
                                            pass
                                        else:
                                            listadisciplinascodigo.append(disciplina.disciplina_codigo)
                                            listadisciplinas.add((disciplina.disciplina_codigo,disciplina.disciplina_descripcion))
                if listadisciplinascodigo ==[]:
                    instance.backend.histogramas.mostrar_popup('No hay proyectos en el area: '+ area)                  
                instance.backend.histogramas.histograma_tabla(listadisciplinascodigo,listadisciplinas,'disciplina')
        
    #Visualizar el tiempo promedio de terminación de los proyectos según el área al que pertenecen.
    def tiempo_promedio_proyectos_area(self,area):
        from GUI import instance
        
        
        dias=0
        contadorproyectos=0
        if area not in instance.backend.cache.lista_Areas:
            
            instance.backend.histogramas.mostrar_popup('El area ingresada no es válida.')
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
            if contadorproyectos==0:
                instance.backend.histogramas.mostrar_popup('No hay proyectos en el area: '+ area)
            else:
                promedio=dias/contadorproyectos
                promedio=round(promedio,0)
                
                instance.backend.histogramas.mostrar_popup('El tiempo promedio de terminacion de los proyectos del area: '+ area + ' es: ' + str(promedio) + 'dias', datos=promedio)
    

    #Visualizar el tiempo promedio de terminación de los proyectos según el gran área al que pertenecen.
    def tiempo_promedio_proyectos_gran_area(self,gran_area): 
        from GUI import instance
        
        dias=0
        contadorproyectos=0
        
        if gran_area not in instance.backend.cache.lista_Gran_Areas:
           
            instance.backend.histogramas.mostrar_popup('El gran area ingresada no es válida.')
        else:
            for disciplina in instance.backend.cache.ref_disciplina:
                if disciplina.gran_area_descripcion ==gran_area:
                    id_disciplina=disciplina.disciplina_id
                    for proyecto_disciplina in instance.backend.cache.proyecto_disciplina:
                        if proyecto_disciplina.disciplina_id==id_disciplina:
                            for proyecto in instance.backend.cache.proyectotal:
                                if proyecto.estado_id=='1' and proyecto.proyecto_id==proyecto_disciplina.proyecto_id:
                                    dias+=(proyecto.fecha_fin-proyecto.fecha_inicio).days
                                    contadorproyectos+=1
            if contadorproyectos==0:
                instance.backend.histogramas.mostrar_popup('No hay proyectos en el gran area: '+ gran_area)
            else:
                promedio=dias/contadorproyectos
                promedio=round(promedio,0)
                
                instance.backend.histogramas.mostrar_popup('El tiempo promedio de terminacion de los proyectos del gran area: '+ gran_area + ' es: ' + str(promedio) + 'dias', datos=promedio)      

    # Visualizar el porcentaje de proyectos que han utilizado tecnologías emergentes (Tecnología e innovación)
    def porcentaje_proyectos_tecnologia(self): 
        cantidad=0
        lista=[]
        from GUI import instance
        for a in instance.backend.cache.ref_tipo_proyecto:
            if a.tipo_proyecto_descripcion=='Tecnología e Innovación':
                lista= a.id
        
        for proyecto in instance.backend.cache.proyectotal:
            if proyecto.tipo_proyecto_id in lista:
                cantidad+=1
        total=len(instance.backend.cache.proyectotal)
        porcentaje=(cantidad*100)/total
        instance.backend.histogramas.grafico_de_tortas(porcentaje, (100-porcentaje), "Con tecnologias emergentes", "Sin tecnologias emergentes", "Tecnologias emergentes")


