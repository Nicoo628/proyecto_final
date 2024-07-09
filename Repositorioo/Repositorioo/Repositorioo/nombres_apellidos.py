import csv
import random

# Lista de nombres y apellidos
nombres = [
    "Juan", "Maria", "Carlos", "Ana", "Pedro", "Laura", "Diego", "Sofia",
    "Luis", "Elena", "Javier", "Marta", "Fernando", "Carmen", "Pablo", "Lucia",
    "Alberto", "Rosa", "Manuel", "Paula", "Ricardo", "Sara", "Enrique", "Clara",
    "Nicolas", "Catalina", "Fabio", "Cristopher", "Danilo", "Cristobal", "Patricio", "Sebastian",
    "Andrea", "Valentina", "Gabriel", "Emilia", "Andres", "Victoria", "Felipe", "Matias",
    "Mariana", "Julian", "Daniela", "Leonardo", "Angela", "Hugo", "Isabel", "Gonzalo",
    "Martina", "Rodrigo", "Renata", "Francisco", "Alicia", "Ignacio", "Camila", "Esteban",
    "Silvia", "Raul", "Teresa", "Marcos", "Luciana", "Eduardo", "Valeria", "Sergio"
]

apellidos = [
    "Perez", "Gomez", "Rodriguez", "Martinez", "Diaz", "Fernandez", "Alvarez",
    "Ruiz", "Torres", "Gutierrez", "Jimenez", "Sanchez", "Lopez", "Morales",
    "Ortega", "Vargas", "Ramos", "Castro", "Romero", "Molina", "Suarez", "Ordoñez",
    "Hernandez", "Garcia", "Rivera", "Vega", "Cortes", "Figueroa", "Acosta", "Mendoza",
    "Vasquez", "Navarro", "Medina", "Reyes", "Castillo", "Soto", "Silva", "Carrasco",
    "Cruz", "Flores", "Moreno", "Herrera", "Rojas", "Sosa", "Lozano", "Guerrero",
    "Paredes", "Miranda", "Castellanos", "Espinoza", "Blanco", "Campos", "Mejia", "Aguilar",
    "Pineda", "Nunez", "Cabrera", "Salazar", "Robles", "Cardenas", "Benitez", "Ferrer"
]


# Generar 1000 nombres y apellidos aleatorios
nombres_aleatorios = random.choices(nombres, k=1000)
apellidos_aleatorios = random.choices(apellidos, k=1000)

# Crear lista de nombres y apellidos combinados
nombres_apellidos = list(zip(nombres_aleatorios, apellidos_aleatorios))

# Escribir los nombres y apellidos en un archivo CSV
with open("nombres_apellidos.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["nombre", "apellido"])
    writer.writerows(nombres_apellidos)

print("Archivo CSV generado con éxito.")

# Clase para manejar nombres y apellidos
class NombresApellidosManager:
    def __init__(self, archivo_nombres):
        self.nombres, self.apellidos = self.cargar_nombres_apellidos(archivo_nombres)  # Cargar nombres y apellidos desde el archivo

    def cargar_nombres_apellidos(self, archivo_nombres):
        nombres = []
        apellidos = []
        with open(archivo_nombres, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombres.append(row['nombre'])
                apellidos.append(row['apellido'])
        return nombres, apellidos

    def obtener_nombre_apellido(self):
        nombre = random.choice(self.nombres)  # Seleccionar un nombre aleatorio
        apellido = random.choice(self.apellidos)  # Seleccionar un apellido aleatorio
        return nombre, apellido