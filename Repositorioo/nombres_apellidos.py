import pandas as pd

class NombresApellidos: #lee archivo csv y lo hace dataframe
    def __init__(self, archivo):
        self.nombres_apellidos = pd.read_csv(archivo).values.tolist()

    def obtener_nombre_apellido(self, id):
        return self.nombres_apellidos[id % len(self.nombres_apellidos)]
