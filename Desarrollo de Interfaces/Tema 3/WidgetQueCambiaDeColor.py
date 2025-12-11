# Importamos las bibliotecas necesarias de PySide6
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt


# Clase CajaInteractiva, un QWidget personalizado que cambia de color al entrar y salir
class CajaInteractiva(QWidget):
    def __init__(self):
        super().__init__()

        # Establecemos el color inicial como verde
        self.color = QColor(0, 255, 0)  # Verde

        # Establecemos el tamaño fijo del widget (200x200 píxeles)
        self.setFixedSize(200, 200)

    # Evento cuando el mouse entra en la caja (hover)
    def enterEvent(self, event):
        self.color = QColor(255, 0, 0)  # Cambiamos el color a rojo
        self.update()  # Actualizamos el widget para que se repinte con el nuevo color

    # Evento cuando el mouse sale de la caja (hover)
    def leaveEvent(self, event):
        self.color = QColor(0, 0, 255)  # Cambiamos el color a azul
        self.update()  # Actualizamos el widget para que se repinte con el nuevo color

    # Evento de pintura (cuando el widget necesita ser repintado)
    def paintEvent(self, event):
        p = QPainter(self)  # Creamos un objeto QPainter para dibujar
        p.setBrush(self.color)  # Establecemos el color de relleno (el color actual)
        p.setPen(Qt.NoPen)  # No queremos un borde (pen)
        p.drawRect(0, 0, self.width(), self.height())  # Dibujamos un rectángulo con el tamaño del widget


# Clase Ventana, que contiene la CajaInteractiva
class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EnterEvent / LeaveEvent")  # Establecemos el título de la ventana

        # Creamos un layout vertical
        layout = QVBoxLayout()

        # Añadimos un widget CajaInteractiva al layout
        layout.addWidget(CajaInteractiva())

        # Establecemos el layout en la ventana principal
        self.setLayout(layout)


# Creamos la aplicación y la ventana principal
app = QApplication([])  # Creamos una instancia de la aplicación
v = Ventana()  # Creamos la ventana principal
v.show()  # Mostramos la ventana
app.exec()  # Ejecutamos el ciclo de eventos de la aplicación
