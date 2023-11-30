class Analisis:
    def __init__(self):
        pass
    ##########CAMBIAR TATI#############
    #Visualizar el porcentaje de participación de las mujeres en los diferentes proyectos según el rol que desempeñan versus la participación de los hombres.
    def porcentaje_participacion_generos(self):
        cantidad_mujeres=0
        cantidad_hombres=0
        from GUI import instance   
        for proyecto in instance.cache.proyectotal:
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
        from GUI import instance
        for disciplina in instance.cache.ref_disciplina:
            if disciplina.disciplina_descripcion==area:
                id_disciplina=disciplina.disciplina_id
        for proyecto in instance.cache.proyectotal:
            if proyecto.tipo_proyecto_id==id_disciplina:
                cantidad_mujeres+=proyecto.cantidad_miembros_F
                cantidad_hombres+=proyecto.cantidad_miembros_M
        total=cantidad_mujeres+cantidad_hombres
        porcentaje_mujeres=(cantidad_mujeres*100)/total
        porcentaje_hombres=(cantidad_hombres*100)/total
        print("El porcentaje de mujeres es: ",porcentaje_mujeres)
        print("El porcentaje de hombres es: ",porcentaje_hombres)
        
    
    def lista_proyectos_fecha(self):#guardar y visualizar una lista de proyectos y la fecha de inicio por la fecha de iniciación del proyecto creciente.
        lista=[]
        from GUI import instance  
        for proyecto in instance.cache.proyectotal:
            lista.append((proyecto.fecha_inicio,proyecto.titulo))
        lista.sort()
        print(lista)


  