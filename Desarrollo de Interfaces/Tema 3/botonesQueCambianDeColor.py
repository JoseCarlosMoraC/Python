from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGroupBox, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPalette, QColor


# Clase EstadoWidget para mostrar el estado con colores personalizados
class EstadoWidget(QLabel):
    def __init__(self):
        super().__init__("APAGADO")  # Inicializamos con el texto "APAGADO"
        self.setAlignment(Qt.AlignCenter)  # Alineamos el texto al centro
        self.setFont(QFont("Arial", 25))  # Establecemos la fuente con tipo "Arial" y tamaño 25

        self.setAutoFillBackground(True)  # Permitimos que el fondo se rellene con color
        self.cambiar_estado("APAGADO")  # Establecemos el estado inicial como "APAGADO"

    def cambiar_estado(self, estado):
        """ Cambia el texto y color de fondo del widget según el estado """
        self.setText(estado)  # Cambia el texto del widget

        paleta = self.palette()  # Obtenemos la paleta de colores actual del widget

        if estado == "APAGADO":
            paleta.setColor(QPalette.Window, QColor(80, 0, 0))  # Fondo rojo oscuro
            paleta.setColor(QPalette.WindowText, Qt.white)  # Texto blanco

        elif estado == "ENCENDIDO":
            paleta.setColor(QPalette.Window, QColor(0, 120, 0))  # Fondo verde
            paleta.setColor(QPalette.WindowText, Qt.white)  # Texto blanco

        elif estado == "ESPERA":
            paleta.setColor(QPalette.Window, QColor(150, 150, 0))  # Fondo amarillo
            paleta.setColor(QPalette.WindowText, Qt.black)  # Texto negro

        self.setPalette(paleta)  # Aplicamos la nueva paleta al widget


# Clase Ventana para la interfaz principal
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control de Estado")  # Establecemos el título de la ventana

        # Creamos el widget para mostrar el estado
        self.estado = EstadoWidget()

        # Creamos los botones para cambiar el estado
        self.btn_apagar = QPushButton("Apagar")
        self.btn_encender = QPushButton("Encender")
        self.btn_espera = QPushButton("Espera")

        # Conectamos los botones a las funciones correspondientes
        self.btn_apagar.clicked.connect(self.apagar)
        self.btn_encender.clicked.connect(self.encender)
        self.btn_espera.clicked.connect(self.espera)

        # Creamos un grupo para contener los botones
        botones = QGroupBox("Controles")
        hb = QHBoxLayout()  # Layout horizontal para los botones
        hb.addWidget(self.btn_apagar)  # Añadimos el botón "Apagar"
        hb.addWidget(self.btn_encender)  # Añadimos el botón "Encender"
        hb.addWidget(self.btn_espera)  # Añadimos el botón "Espera"
        botones.setLayout(hb)  # Establecemos el layout en el grupo

        # Creamos un layout vertical para organizar los elementos
        layout = QVBoxLayout()
        layout.addWidget(self.estado)  # Añadimos el widget que muestra el estado
        layout.addWidget(botones)  # Añadimos el grupo de botones

        self.setLayout(layout)  # Establecemos el layout principal de la ventana

    # Métodos para manejar los clics de los botones
    def apagar(self):
        self.estado.cambiar_estado("APAGADO")  # Cambiamos el estado a "APAGADO"

    def encender(self):
        self.estado.cambiar_estado("ENCENDIDO")  # Cambiamos el estado a "ENCENDIDO"

    def espera(self):
        self.estado.cambiar_estado("ESPERA")  # Cambiamos el estado a "ESPERA"


# Creamos la aplicación y la ventana
app = QApplication([])  # Instanciamos la aplicación
v = Ventana()  # Creamos la ventana principal
v.show()  # Mostramos la ventana
app.exec()  # Ejecutamos el ciclo de eventos de la aplicación
