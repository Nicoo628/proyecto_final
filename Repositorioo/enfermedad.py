class Enfermedad:
    def __init__(self, infeccion_probable, duracion, prob_recuperacion):
        self.infeccion_probable = infeccion_probable
        self.duracion = duracion
        self.prob_recuperacion = prob_recuperacion

    def get_infeccion_probable(self):
        return self.infeccion_probable

    def get_duracion(self):
        return self.duracion

    def get_prob_recuperacion(self):
        return self.prob_recuperacion
