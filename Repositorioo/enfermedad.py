class Enfermedad:
    def __init__(self, infeccion_probable, promedio_pasos):
        self.infeccion_probable = infeccion_probable# Probabilidad de alguien sano se infecte de forma fisica
        self.promedio_pasos = promedio_pasos # el tiempo en el cual puede infectar antes de que se recupere o se muera
        self.enfermo = False
        self.contador = 0

    def infectar(self):   # aca va a ir eso de 0.3 de enfermarse y 0.8 de posibilidad 
        self.enfermo = True
        self.contador = self.promedio_pasos

    def paso(self):
        if self.enfermo:
            self.contador -= 1 # los pasos durante esta infectado el ciudadano
            if self.contador <= 0:# valor para el numero del tiempo
                self.enfermo = False
