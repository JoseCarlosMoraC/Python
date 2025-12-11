# José Carlos Mora 2ºDAM
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
       
        # Estado interno del semáforo.
        # Comenzamos siempre en rojo.
        # Se usa __ para hacerlo "privado" (encapsulación).
        self.__estado_actual = "rojo"
       
        # Configuración básica de la ventana
        self.setWindowTitle("Semáforo")
        self.setGeometry(100, 100, 250, 400)  # Posición y tamaño
       
        # Creamos la UI
        self._crear_interfaz()
   
    def _crear_interfaz(self):
        """Crea los widgets y el layout de la ventana."""
       
        # Botón para cambiar el estado del semáforo
        self.boton_cambiar = QPushButton("Cambiar", self)
        self.boton_cambiar.setFixedHeight(40)  # Altura fija para estética
       
        # Conectamos la señal clicked del botón con el método cambiar_estado()
        self.boton_cambiar.clicked.connect(self.cambiar_estado)
       
        # Layout vertical para organizar el botón
        layout = QVBoxLayout(self)
       
        # Añadimos espacio antes del botón para situarlo abajo
        layout.addStretch()
       
        # Añadimos el botón al layout
        layout.addWidget(self.boton_cambiar)
       
        # Aplicamos el layout al widget principal
        self.setLayout(layout)
   
    # -----------------------------------------------------------
    # MÉTODOS PARA GESTIONAR EL ESTADO DEL SEMÁFORO
    # -----------------------------------------------------------
   
    def estado(self):
        """Devuelve el estado actual del semáforo."""
        return self.__estado_actual
   
    def reiniciar(self):
        """Reinicia el semáforo poniendo la luz roja."""
        self.__estado_actual = "rojo"
        self.update()  # Forzamos repintado
   
    def cambiar_estado(self):
        """Cambia el estado del semáforo cada vez que se pulsa el botón."""
       
        # Secuencia: rojo -> amarillo -> verde -> rojo
        if self.__estado_actual == "rojo":
            self.__estado_actual = "amarillo"
       
        elif self.__estado_actual == "amarillo":
            self.__estado_actual = "verde"
       
        else:  # estaba en verde
            self.__estado_actual = "rojo"
       
        # update() llama internamente a paintEvent(), repintando la ventana
        self.update()
   
   
    # -----------------------------------------------------------
    # DIBUJO DEL SEMÁFORO
    # -----------------------------------------------------------
   
    def paintEvent(self, event):
        """
        Método que se ejecuta automáticamente cada vez que la ventana
        necesita repintarse. Aquí dibujamos las luces del semáforo.
        """
       
        painter = QPainter(self)  # Objeto para dibujar
        painter.setRenderHint(QPainter.Antialiasing)  # Bordes suaves
       
        # Colores principales (encendido y apagado)
        color_rojo_encendido = QColor(255, 0, 0)
        color_amarillo_encendido = QColor(255, 255, 0)
        color_verde_encendido = QColor(0, 200, 0)
       
        color_apagado = QColor(80, 80, 80)  # Gris oscuro para luces apagadas
       
        # Posiciones de cada luz dentro de la ventana
        x_centro = 75
       
        y_luz_roja = 50
        y_luz_amarilla = 150
        y_luz_verde = 250
       
        tamaño_luz = 80  # diámetro de cada luz
       
        # -------------------------------
        # LUZ ROJA
        # -------------------------------
        if self.__estado_actual == "rojo":
            painter.setBrush(color_rojo_encendido)
        else:
            painter.setBrush(color_apagado)
       
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(x_centro, y_luz_roja, tamaño_luz, tamaño_luz)
       
        # -------------------------------
        # LUZ AMARILLA
        # -------------------------------
        if self.__estado_actual == "amarillo":
            painter.setBrush(color_amarillo_encendido)
        else:
            painter.setBrush(color_apagado)
       
        painter.drawEllipse(x_centro, y_luz_amarilla, tamaño_luz, tamaño_luz)
       
        # -------------------------------
        # LUZ VERDE
        # -------------------------------
        if self.__estado_actual == "verde":
            painter.setBrush(color_verde_encendido)
        else:
            painter.setBrush(color_apagado)
       
        painter.drawEllipse(x_centro, y_luz_verde, tamaño_luz, tamaño_luz)
       
        # -------------------------------
        # DIBUJAR EL MARCO DEL SEMÁFORO
        # -------------------------------
        painter.setBrush(Qt.NoBrush)
        painter.setPen(QColor(0, 0, 0))  # Marco negro
        painter.drawRect(60, 30, 110, 310)  # Caja del semáforo


# -----------------------------------------------------------
# EJECUCIÓN DE LA APLICACIÓN
# -----------------------------------------------------------
app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()