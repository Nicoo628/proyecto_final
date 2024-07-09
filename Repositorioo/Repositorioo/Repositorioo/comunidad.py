import numpy as np
from ciudadano import Ciudadano
from nombres_apellidos import NombresApellidosManager

class Comunidad:
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad, num_infectados, probabilidad_conexion_fisica, archivo_nombres):
        self.num_ciudadanos = num_ciudadanos
        self.ciudadanos = []
        self.enfermedad = enfermedad
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica

        # Cargar nombres y apellidos desde archivo CSV
        self.nombres_apellidos_manager = NombresApellidosManager(archivo_nombres)
        self.__crear_comunidad(num_infectados)  # Crear la comunidad con ciudadanos

    def __crear_comunidad(self, num_infectados):
        for _ in range(self.num_ciudadanos):
            nombre, apellido = self.nombres_apellidos_manager.obtener_nombre_apellido()
            ciudadano = Ciudadano(nombre, apellido, self.enfermedad)
            self.ciudadanos.append(ciudadano)  # Añadir cada ciudadano a la lista de ciudadanos
        self.inicializar_infectados_aleatorios(num_infectados)  # Inicializar un número de infectados aleatorios

    def simular_dia(self):
        for ciudadano in self.ciudadanos:
            ciudadano.procesar_dia()  # Procesar el estado diario de cada ciudadano
        self.propagar_infeccion()  # Propagar la infección entre ciudadanos

    def propagar_infeccion(self):
        for ciudadano in self.ciudadanos:
            if ciudadano.estado == "Infectado":
                for _ in range(np.random.poisson(self.probabilidad_conexion_fisica)):
                    otro_ciudadano = np.random.choice(self.ciudadanos)
                    ciudadano.intentar_infectar(otro_ciudadano, self.enfermedad.infeccion_probable)

    def contar_estado(self, estado):
        return sum(1 for ciudadano in self.ciudadanos if ciudadano.estado == estado)  # Contar ciudadanos en un estado dado
    
    def generar_muestra_aleatoria(self, tamano_muestra):
        return np.random.choice(self.ciudadanos, tamano_muestra, replace=False)  # Generar una muestra aleatoria de ciudadanos

    def inicializar_infectados_aleatorios(self, num_infectados):
        muestra = self.generar_muestra_aleatoria(num_infectados)  # Seleccionar una muestra aleatoria de ciudadanos
        for ciudadano in muestra:
            ciudadano.infectar()  # Infectar a los ciudadanos en la muestra
