class Ciudadano: #base de atributos simples por ahora
    def __init__(self, comunidad, _id,nombre_y_apellido, familia, emfermedad, estado):
        self.comunidad = comunidad
        self._id = _id
        self.nombre_y_apellido
        self.familia
        
        self.enfermedad = None
        #probablemente esto no va a funcionar asi q despues veo como lo voy a hacer
        self.estado = True # enfermo
        self.estado = False #no enfermo
