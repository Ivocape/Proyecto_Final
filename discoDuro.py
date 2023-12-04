import csv
#####################################################################################
# ESTE DISCO DURO DEBE DE ENCARGARSE DE GUARDAR TODA INFORMACION DE USUARIOS, CLIENTES, PERSONAL, ADMINS,
#####################################################################################
class DiscoDuro():
    # Crear el disco duro
    def __init__(self) -> None:
        pass

    def leerSETUP (self, carpeta):    
        # Abrir el archivo CSV
        with open("../" + carpeta,'r', newline='',encoding='utf-8') as csvfile: 
            # Crear un objeto lector CSV
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            next(reader)
            match carpeta:
                case "proyectos_2015.csv":
                            
                    for row in reader:
                        # Extraigo la informacion de cada fila de los proyectos del 2015
                        año=2015
                        proyecto_id = row[0]
                        fuente = row[1]
                        titulo = row[2]
                        fecha_inicio=row[3]
                        fecha_fin=row[4]
                        resumen = row[5]
                        moneda_id = row[6]
                        monto_total_solicitado = row[7]
                        monto_total_adjudicado = row[8]
                        monto_financiado_solicitado= row[9]
                        monto_financiado_adjudicado = row[10]
                        tipo_proyecto_id = row[11]
                        codigo_identificacion= row[12]
                        palabras_clave = row[13]
                        estado_id = row[14]
                        fondo_anpcyt= row[15]
                        cantidad_miembros_F = row[16]
                        cantidad_miembros_M = row[17]
                        sexo_director = row[18]
                        from GUI import instance
                        instance.backend.cache.cargar(año,proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director)
                case "proyectos_2016.csv":
                    for row in reader:
                        # Extraigo la informacion de cada fila de los proyectos del 2016
                        año=2016 
                        proyecto_id = row[0]
                        fuente = row[1]
                        titulo = row[2]
                        fecha_inicio=row[3]
                        fecha_fin=row[4]
                        resumen = row[5]
                        moneda_id = row[6]
                        monto_total_solicitado = row[7]
                        monto_total_adjudicado = row[8]
                        monto_financiado_solicitado= row[9]
                        monto_financiado_adjudicado = row[10]
                        tipo_proyecto_id = row[11]
                        codigo_identificacion= row[12]
                        palabras_clave = row[13]
                        estado_id = row[14]
                        fondo_anpcyt= row[15]
                        cantidad_miembros_F = row[16]
                        cantidad_miembros_M = row[17]
                        sexo_director = row[18]
                        from GUI import instance
                        instance.backend.cache.cargar(año,proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director)
                case "proyectos_2017.csv":
                    for row in reader:
                        # Extraigo la informacion de cada fila de los proyectos del 2017
                        año=2017
                        proyecto_id = row[0]
                        fuente = row[1]
                        titulo = row[2]
                        fecha_inicio=row[3]
                        fecha_fin=row[4]
                        resumen = row[5]
                        moneda_id = row[6]
                        monto_total_solicitado = row[7]
                        monto_total_adjudicado = row[8]
                        monto_financiado_solicitado= row[9]
                        monto_financiado_adjudicado = row[10]
                        tipo_proyecto_id = row[11]
                        codigo_identificacion= row[12]
                        palabras_clave = row[13]
                        estado_id = row[14]
                        fondo_anpcyt= row[15]
                        cantidad_miembros_F = row[16]
                        cantidad_miembros_M = row[17]
                        sexo_director = row[18]
                        from GUI import instance
                        instance.backend.cache.cargar(año,proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director)
                case "proyectos_2018.csv":
                    for row in reader:
                        # Extraigo la informacion de cada fila de los proyectos del 2018
                        año=2018
                        proyecto_id = row[0]
                        fuente = row[1]
                        titulo = row[2]
                        fecha_inicio=row[3]
                        fecha_fin=row[4]
                        resumen = row[5]
                        moneda_id = row[6]
                        monto_total_solicitado = row[7]
                        monto_total_adjudicado = row[8]
                        monto_financiado_solicitado= row[9]
                        monto_financiado_adjudicado = row[10]
                        tipo_proyecto_id = row[11]
                        codigo_identificacion= row[12]
                        palabras_clave = row[13]
                        estado_id = row[14]
                        fondo_anpcyt= row[15]
                        cantidad_miembros_F = row[16]
                        cantidad_miembros_M = row[17]
                        sexo_director = row[18]
                        from GUI import instance
                        instance.backend.cache.cargar(año,proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director)
                case "ref_disciplina.csv":
                    for row in reader:
                        # Extraigo la informacion de cada fila de las disciplinas
                        disciplina_id=row[0]
                        gran_area_codigo=row[1]
                        gran_area_descripcion=row[2]
                        area_codigo=row[3]
                        area_descripcion=row[4]
                        disciplina_codigo=row[5]
                        disciplina_descripcion=row[6]
                        from GUI import instance
                        instance.backend.cache.cargar_disciplina(disciplina_id,gran_area_codigo,gran_area_descripcion,area_codigo,area_descripcion,disciplina_codigo,disciplina_descripcion)
                case "ref_estado_proyecto.csv":
                    for row in reader:
                        # Extraigo la informacion de cada fila de los estados de los proyectos
                        estado_id=row[0]
                        estado_descripcion=row[1]
                        from GUI import instance
                        instance.backend.cache.cargar_estado_proyecto(estado_id,estado_descripcion)
                case "ref_funcion.csv":
                    for row in reader:
                        # Extraigo la informacion de cada fila de las funciones
                        funcion_id=row[0]
                        funcion_descripcion=row[1]
                        from GUI import instance
                        instance.backend.cache.cargar_funcion(funcion_id,funcion_descripcion)
                case "ref_moneda.csv":
                    for row in reader:
                        # Extraigo la informacion de cada fila de las monedas
                        moneda_id=row[0]
                        moneda_descripcion=row[1]
                        codigo_iso=row[2]
                        from GUI import instance
                        instance.backend.cache.cargar_moneda(moneda_id,moneda_descripcion,codigo_iso)
                case "ref_tipo_proyecto.csv":
                    for row in reader:
                        # Extraigo la informacion de cada fila de los tipos de proyectos
                        id=row[0]
                        sigla=row[1]
                        descripcion=row[2]
                        tipo_proyecto_id=row[3]
                        tipo_proyecto_descripcion=row[4]
                        from GUI import instance
                        instance.backend.cache.cargar_tipo_proyecto(id,sigla,descripcion,tipo_proyecto_id,tipo_proyecto_descripcion)
                case "proyecto_disciplina.csv":
                    for row in reader:
                        # Extraigo la informacion de cada fila de los proyectos y sus disciplinas
                        proyecto_id=row[0]
                        disciplina_id=row[1]
                        from GUI import instance
                        instance.backend.cache.cargar_proyecto_disciplina(proyecto_id,disciplina_id)
                case "proyecto_participante.csv":
                    for row in reader:
                        # Extraigo la informacion de cada fila de los proyectos y sus participantes
                        proyecto_id=row[0]
                        persona_id=row[1]
                        funcion_id=row[2]
                        fecha_inicio=row[3]
                        fecha_fin=row[4]
                        from GUI import instance
                        instance.backend.cache.cargar_proyecto_participante(proyecto_id,persona_id,funcion_id,fecha_inicio,fecha_fin)
