class Ciudadano:
    def __init__(self, id, nombre, apellido, comunidad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.comunidad = comunidad
        self.enfermo = False
        self.dias_enfermo = 0
        self.enfermedad = None

    def set_enfermedad(self, enfermedad):
        self.enfermo = True
        self.enfermedad = enfermedad

    def get_enfermo(self):
        return self.enfermo

    def incrementar_dias_enfermo(self):
        self.dias_enfermo += 1

    def set_enfermo(self, enfermo):
        self.enfermo = enfermo

    def recuperar(self):
        self.enfermo = False
        self.enfermedad = None
        self.dias_enfermo = 0
