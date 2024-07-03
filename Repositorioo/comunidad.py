class Comunidad:
    def __init__(self, num_ciudadanos, num_infectados, enfermedad, prob_infeccion, duracion_enfermedad):
        self.num_ciudadanos = num_ciudadanos
        self.num_infectados = num_infectados
        self.num_recuperados = 0
        self.enfermedad = enfermedad
        self.prob_infeccion = prob_infeccion
        self.duracion_enfermedad = duracion_enfermedad
        self.ciudadanos = []

    def agregar_ciudadano(self, ciudadano):#append agrega ciudadano a la lista ciudadanos
        self.ciudadanos.append(ciudadano)

    def get_num_infectados(self):
        return self.num_infectados

    def set_num_infectados(self, num_infectados):
        self.num_infectados = num_infectados

    def get_num_recuperados(self):
        return self.num_recuperados

    def set_num_recuperados(self, num_recuperados):
        self.num_recuperados = num_recuperados
