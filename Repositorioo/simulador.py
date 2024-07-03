import random
import numpy as np
from ciudadano import Ciudadano  
from comunidad import Comunidad  
from enfermedad import Enfermedad  
from nombres_apellidos import NombresApellidos  
import pandas as pd  #dataframes. son para para organizar los datos de los steps o dias y mandarlos al csv

class Simulador:
    def __init__(self, archivo_nombres, num_ciudadanos, num_infectados_iniciales):
      
        self.nombres_apellidos = NombresApellidos(archivo_nombres)  
        self.num_ciudadanos = num_ciudadanos  # total de los ciudadano y el val inicial
        self.num_infectados_iniciales = num_infectados_iniciales  
        self.ciudadanos = []  # 0numero inicial, de infectados q despues toma el valor q le pongamos
                    #none es la enfermedad que afecta a la comunidad que despues igual se le tiene que asignar otro valo
                    # num inicial recuperados
                    #prom conexiones fisicas de los ciudadanos
        self.comunidad = Comunidad(num_ciudadanos, 0, None, 0, 8) #
        self.enfermedad = Enfermedad(0.3, 5, 0.)  # 0.3 prob de ser infectado, 5 duracion promedio en la q se recupera, 0.1, prob de recuperarse
        self.dias_simulados = 0  

        self.__crear_ciudadanos()  
        self.__infectar_inicial()  

    def __crear_ciudadanos(self):
        
        for id in range(self.num_ciudadanos):
            nombre, apellido = self.nombres_apellidos.obtener_nombre_apellido(id)  
            ciudadano = Ciudadano(id, nombre, apellido, self.comunidad)  
            self.ciudadanos.append(ciudadano)  # Agregar ciudadano a la lista general
            self.comunidad.agregar_ciudadano(ciudadano)  # Agregar ciudadano a la comunidad

    def __infectar_inicial(self):#numpy.random.normal creo q es asi
        # inicia en un num inicial USAR EL RANDOM DE NUMPY
        infectados = random.sample(self.ciudadanos, self.num_infectados_iniciales)
        for ciudadano in infectados:
            ciudadano.set_enfermedad(self.enfermedad)  
            self.comunidad.set_num_infectados(self.comunidad.get_num_infectados() + 1)  # Actualizar conteo de infectados

    def simular_dia(self):
        
        for ciudadano in self.ciudadanos:
            if ciudadano.get_enfermo():  
                if random.random() < self.enfermedad.get_prob_recuperacion():  # Probabilidad de recuperación num aleatorio, 0.1 10%
                    ciudadano.recuperar()  # Ciudadano se recupera
                    self.comunidad.set_num_infectados(self.comunidad.get_num_infectados() - 1)  # Actualizar infectados
                    self.comunidad.set_num_recuperados(self.comunidad.get_num_recuperados() + 1)  # Actualizar recuperados
                else:
                    ciudadano.incrementar_dias_enfermo()  # Incrementar días de enfermedad si no se recupera
            else:# cambiar a random de numpy, preguntar a karin 
                if random.random() < self.enfermedad.get_infeccion_probable(): #genera numero 0.0-1.0 
                    self.comunidad.set_num_infectados(self.comunidad.get_num_infectados() + 1) # se compara numero aleatorio con prob de infeccion
                                                                                               # tru se infecta
        self.dias_simulados += 1  

    def generar_reporte_diario(self):
        num_susceptibles = sum(1 for ciudadano in self.ciudadanos if not ciudadano.get_enfermo())  # Contar susceptibles
        num_infectados = sum(1 for ciudadano in self.ciudadanos if ciudadano.get_enfermo())  # Contar infectados
        num_recuperados = self.comunidad.get_num_recuperados()  # Obtener número de recuperados

        reporte = (
            f"Día {self.dias_simulados}:\n"
            f"Susceptibles: {num_susceptibles}\n"
            f"Infectados: {num_infectados}\n"
            f"Recuperados: {num_recuperados}\n"
        )
        return reporte  

    def exportar_reporte_diario(self, nombre_archivo):
        num_susceptibles = sum(1 for ciudadano in self.ciudadanos if not ciudadano.get_enfermo())  
        num_infectados = sum(1 for ciudadano in self.ciudadanos if ciudadano.get_enfermo())  
        num_recuperados = self.comunidad.get_num_recuperados()  

        # Crear un DataFrame con los datos del día actual
        data = pd.DataFrame([[self.dias_simulados, num_susceptibles, num_infectados, num_recuperados]],
                            columns=['Día', 'Susceptibles', 'Infectados', 'Recuperados'])

        # Exportar el DataFrame al archivo CSV especificado
        data.to_csv(nombre_archivo, mode='a', header=not pd.io.common.file_exists(nombre_archivo), index=False)
