import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib
from simulador import Simulador
from comunidad import Comunidad
from enfermedad import Enfermedad

class VentanaPrincipal(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(title="Simulacion Enfermedad. Proyecto final PA" , application=app)
        self.set_default_size(800, 600)

        # la caja vertical
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_child(vbox)

        # boton para ir avanzando los dias
        self.step_button = Gtk.Button(label="AVANZAR DIA")
        self.step_button.connect("clicked", self.on_step_button_clicked)
        vbox.append(self.step_button)

    #en donde se van a mostrar los resultados en texto
        self.textview = Gtk.TextView()
        self.textview.set_editable(False)
        self.textbuffer = self.textview.get_buffer()
        vbox.append(self.textview)

    # los datos de la simulacion
        covid = Enfermedad(infeccion_probable=0.3, promedio_pasos=18)
        talca = Comunidad(num_ciudadanos=2000, promedio_conexion_fisica=8, enfermedad=covid, num_infectados=10, probabilidad_conexion_fisica=0.8, archivo_nombres="nombres_apellidos.csv")

        self.simulador = Simulador()
        self.simulador.set_comunidad(comunidad=talca)
        self.dia_actual = 0

    def on_step_button_clicked(self, widget):
        self.dia_actual += 1
        self.simulador.comunidad.simular_dia()  
        susceptibles = self.simulador.comunidad.contar_estado("Susceptible")
        infectados = self.simulador.comunidad.contar_estado("Infectado")
        recuperados = self.simulador.comunidad.contar_estado("Recuperado")
        total_contagios = infectados + recuperados  
        
        #Imprimir los resultados del dia
        texto_resultado = f"Día {self.dia_actual}: Susceptibles: {susceptibles}, Infectados: {infectados}, Recuperados: {recuperados}, Total Contagios: {total_contagios}\n"
        self.textbuffer.insert(self.textbuffer.get_end_iter(), texto_resultado)


class AplicacionSimulacion(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.example.simulacion')

    def do_activate(self):
        ventana = VentanaPrincipal(self)
        ventana.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = AplicacionSimulacion()
app.run()
