import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib
from simulador import Simulador
from comunidad import Comunidad
from enfermedad import Enfermedad


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(title="Simulación Enfermedad. Proyecto final PA", application=app)
        self.set_default_size(800, 600)

        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_child(vbox)
    
        # se crea la pestaña
        self.notebook = Gtk.Notebook()
        vbox.append(self.notebook)
    # Pestaña de los resultados diarios
        self.page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.notebook.append_page(self.page1, Gtk.Label(label="Resultados Diarios"))
    # pestaña de los ciudadanos
        self.page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.notebook.append_page(self.page2, Gtk.Label(label="Atributos Ciudadanos"))
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # botonn                                                      PESTAÑA 1
        self.step_button_page1 = Gtk.Button(label="AVANZAR DIA")
        self.step_button_page1.connect("clicked", self.on_step_button_clicked)
        self.page1.append(self.step_button_page1)

        # texto de resultados de la pestaña 1 
        self.scrolled_window_resultados = Gtk.ScrolledWindow()
        self.scrolled_window_resultados.set_vexpand(True)  #expandir para arriba y para al lado
        self.scrolled_window_resultados.set_hexpand(True)   
        self.textview_resultados = Gtk.TextView()
        self.textview_resultados.set_editable(False)
        self.textbuffer_resultados = self.textview_resultados.get_buffer()
        self.scrolled_window_resultados.set_child(self.textview_resultados)
        self.page1.append(self.scrolled_window_resultados)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Pestaña2
        # Botón para avanzar los días en la pestaña de detalles ciudadanos
        self.step_button_page2 = Gtk.Button(label="AVANZAR DIA")
        self.step_button_page2.connect("clicked", self.on_step_button_clicked)
        self.page2.append(self.step_button_page2)

        # Área de texto para mostrar detalles de ciudadanos en la pestaña de detalles ciudadanos con barra de desplazamiento
        self.scrolled_window_ciudadanos = Gtk.ScrolledWindow()
        self.scrolled_window_ciudadanos.set_vexpand(True)  # Expandir verticalmente
        self.scrolled_window_ciudadanos.set_hexpand(True)  # Expandir horizontalmente
        self.textview_ciudadanos = Gtk.TextView()
        self.textview_ciudadanos.set_editable(False)
        self.textbuffer_ciudadanos = self.textview_ciudadanos.get_buffer()
        self.scrolled_window_ciudadanos.set_child(self.textview_ciudadanos)
        self.page2.append(self.scrolled_window_ciudadanos)

        # Inicializar la simulación
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
        
        # Limitar el tamaño del buffer de texto para evitar sobrecarga
        max_lines = 20
        start_iter = self.textbuffer_resultados.get_start_iter()
        end_iter = self.textbuffer_resultados.get_end_iter()
        lines = self.textbuffer_resultados.get_text(start_iter, end_iter, True).split('\n')
        if len(lines) > max_lines:
            lines = lines[-max_lines:]
            new_text = '\n'.join(lines)
            self.textbuffer_resultados.set_text(new_text)

        # Imprimir los resultados del día
        texto_resultado = f"Día {self.dia_actual}: Susceptibles: {susceptibles}, Infectados: {infectados}, Recuperados: {recuperados}, Total Contagios: {total_contagios}\n"
        self.textbuffer_resultados.insert(self.textbuffer_resultados.get_end_iter(), texto_resultado)
        
        # Limitar el tamaño del buffer de texto para evitar sobrecarga en detalles de ciudadanos
        start_iter = self.textbuffer_ciudadanos.get_start_iter()
        end_iter = self.textbuffer_ciudadanos.get_end_iter()
        lines = self.textbuffer_ciudadanos.get_text(start_iter, end_iter, True).split('\n')
        if len(lines) > max_lines:
            lines = lines[-max_lines:]
            new_text = '\n'.join(lines)
            self.textbuffer_ciudadanos.set_text(new_text)

        # Imprimir los detalles de los ciudadanos (mostrar solo algunos detalles para reducir la carga)
        texto_ciudadanos = ""
        for i, ciudadano in enumerate(self.simulador.comunidad.ciudadanos):
            if i >= 50:  # Mostrar solo los primeros 50 ciudadanos para reducir la carga
                break
            texto_ciudadanos += f"{ciudadano.nombre} {ciudadano.apellido}, Estado: {ciudadano.estado}, Días Infectado: {ciudadano.dias_infectado}\n"
        self.textbuffer_ciudadanos.set_text(texto_ciudadanos)


class AplicacionSimulacion(Gtk.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        ventana = MainWindow(self)
        ventana.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = AplicacionSimulacion()
app.run()
