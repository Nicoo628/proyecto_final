from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

# Crear una instancia de Enfermedad
covid = Enfermedad(infeccion_probable=0.3, promedio_pasos=18)

# Crear una instancia de Comunidad con ciudadanos y configuraciones iniciales
talca = Comunidad(num_ciudadanos=20000, promedio_conexion_fisica=8, enfermedad=covid, num_infectados=100, probabilidad_conexion_fisica=0.8, archivo_nombres="nombres_apellidos.csv")

# Crear una instancia de Simulador
sim = Simulador()
sim.set_comunidad(comunidad=talca)  # Establecer la comunidad en el simulador
sim.run(pasos=45)  # Ejecutar la simulación por un número de días
