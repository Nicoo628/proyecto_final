import numpy as np
from ciudadano import Ciudadano
from nombres_apellidos import NombresApellidosManager

class Comunidad:
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica, archivo_nombres):
        self.num_ciudadanos = num_ciudadanos
        self.ciudadanos = []
        self.enfermedad = enfermedad

        # Cargar nombres y apellidos desde archivo CSV
        self.nombres_apellidos_manager = NombresApellidosManager(archivo_nombres)
        self.__crear_comunidad(num_infectados, probabilidad_conexion_fisica)  # Crear la comunidad con ciudadanos

    def __crear_comunidad(self, num_infectados, probabilidad_conexion_fisica):
        for _ in range(self.num_ciudadanos):
            nombre, apellido = self.nombres_apellidos_manager.obtener_nombre_apellido()
            ciudadano = Ciudadano(nombre, apellido, self.enfermedad)
            self.ciudadanos.append(ciudadano)  # Añadir cada ciudadano a la lista de ciudadanos
        self.inicializar_infectados_aleatorios(num_infectados)  # Inicializar un número de infectados aleatorios

    def simular_dia(self):
        for ciudadano in self.ciudadanos:
            ciudadano.procesar_dia()  # Procesar el estado diario de cada ciudadano

    def contar_estado(self, estado):
        return sum(1 for ciudadano in self.ciudadanos if ciudadano.estado == estado)  # Contar ciudadanos en un estado dado
    
    def crear_grupos(self, tamano_grupo):
        grupos = [self.ciudadanos[i:i + tamano_grupo] for i in range(0, self.num_ciudadanos, tamano_grupo)]
        return grupos  # Crear grupos de ciudadanos

    def generar_muestra_aleatoria(self, tamano_muestra):
        return np.random.choice(self.ciudadanos, tamano_muestra, replace=False)  # Generar una muestra aleatoria de ciudadanos

    def inicializar_infectados_aleatorios(self, num_infectados):
        muestra = self.generar_muestra_aleatoria(num_infectados)  # Seleccionar una muestra aleatoria de ciudadanos
        for ciudadano in muestra:
            ciudadano.infectar()  # Infectar a los ciudadanos en la muestra
