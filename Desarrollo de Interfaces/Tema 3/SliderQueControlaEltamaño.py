from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPainter, QColor
import sys


class VentanaCirculo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control de tamaño del círculo")
        self.setGeometry(200, 100, 400, 400)

        # Tamaño inicial del círculo
        self.tamano = 50

        # Slider para modificar el tamaño
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(20)
        self.slider.setMaximum(200)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.cambiar_tamano)

        # Etiqueta que muestra el valor actual
        self.lbl = QLabel("Tamaño: 50")

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.lbl)
        layout.addStretch()

        self.setLayout(layout)

    def cambiar_tamano(self, valor):
        self.tamano = valor
        self.lbl.setText("Tamaño: " + str(valor))
        self.update()  # Redibujar

    def paintEvent(self, event):
        p = QPainter(self)
        p.setBrush(QColor(100, 150, 255))

        # Dibujamos el círculo centrado
        x = (self.width() - self.tamano) // 2
        y = (self.height() - self.tamano) // 2 - 50

        p.drawEllipse(x, y, self.tamano, self.tamano)


app = QApplication(sys.argv)
v = VentanaCirculo()
v.show()
app.exec()
