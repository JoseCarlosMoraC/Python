import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt

class CirculoRojo(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor("red"))
        painter.setPen(QPen(Qt.black))
        painter.drawEllipse(self.rect())

class CirculoAmarillo(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor("yellow"))
        painter.setPen(QPen(Qt.black))
        painter.drawEllipse(self.rect())

class CirculoVerde(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor("green"))
        painter.setPen(QPen(Qt.black))
        painter.drawEllipse(self.rect())

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Semaforo")

        # Crear widgets de los círculos
        circulo_rojo = CirculoRojo()
        circulo_amarillo = CirculoAmarillo()
        circulo_verde = CirculoVerde()

     
        layout = QVBoxLayout()
        layout.addWidget(circulo_rojo)
        layout.addWidget(circulo_amarillo)
        layout.addWidget(circulo_verde)

        # Crear un widget contenedor para el layout
        container = QWidget()
        container.setLayout(layout)

        # Establecer el widget contenedor como el central
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
