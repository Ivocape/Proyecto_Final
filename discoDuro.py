import csv
import pandas as pd
import datetime
#####################################################################################
# ESTE DISCO DURO DEBE DE ENCARGARSE DE GUARDAR TODA INFORMACION DE USUARIOS, CLIENTES, PERSONAL, ADMINS,
#####################################################################################
class DiscoDuro():
    # Crear el disco duro
    def __init__(self) -> None:
        pass

    def leerSETUP (self, carpeta):    
        # Abrir el archivo CSV
        with open(carpeta,'r', newline='') as csvfile: 
            # Crear un objeto lector CSV
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            match carpeta:
                case "proyectos_2015.csv":
                            
                    for row in reader:
                        # Extraigo la informacion de cada fila de los proyectos del 2015
                        año=2015
                        proyecto_id = row[0]
                        fuente = row[1]
                        titulo = row[2]
                        fecha_inicio = row[3]
                        fecha_fin = row[4]
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
                        
                        instance.cache.cargar(año,proyecto_id,fuente, titulo,fecha_inicio,fecha_fin,resumen,moneda_id,monto_total_solicitado,monto_total_adjudicado,monto_financiado_solicitado,monto_financiado_adjudicado,tipo_proyecto_id,codigo_identificacion,palabras_clave,estado_id,fondo_anpcyt,cantidad_miembros_F,cantidad_miembros_M,sexo_director)
                        
