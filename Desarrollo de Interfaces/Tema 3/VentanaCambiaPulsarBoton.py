from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QPalette, QColor
import sys


class CambiarColor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cambio de color")

        self.btn = QPushButton("Cambiar fondo")
        self.btn.clicked.connect(self.cambiar)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        self.setLayout(l)

        self.colores = [QColor("red"), QColor("green"), QColor("blue"), QColor("yellow")]
        self.indice = 0

    def cambiar(self):
        pal = self.palette()
        pal.setColor(QPalette.Window, self.colores[self.indice])
        self.setPalette(pal)
        self.indice = (self.indice + 1) % len(self.colores)


app = QApplication(sys.argv)
v = CambiarColor()
v.show()
app.exec()
