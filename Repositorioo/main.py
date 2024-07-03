from simulador import Simulador

archivo_nombres = 'nombres_apellidos.csv'
num_ciudadanos = 100
num_infectados_iniciales = 5


simulador = Simulador(archivo_nombres, num_ciudadanos, num_infectados_iniciales)

# empieza la simulacion
dias_a_simular = 20
for _ in range(dias_a_simular):
    simulador.simular_dia()
    reporte = simulador.generar_reporte_diario()
    print(reporte)

    # ME FALTA DEFINIR LO DE SI SON CONTACTOS ESTRECHOS
    # se van repitiendo, hacer las familias y comunidades

    # avanze en el modelo sir, definir los S I R, en implementar los pandas y me faltan los numpys
    # logre que compialar pero funciona mal, quise crear un archivo csv que vaya registrando
    # tenia problema con que me compilaran los compilados, lo logre hace poco y me di cuenta que las personas se van repitiendo
    # 
