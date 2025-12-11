from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal

class BotonModo(QPushButton):
    modo_cambiado = Signal(str)

    def __init__(self):
        super().__init__("Modo A")
        self.__modos = ["Modo A", "Modo B", "Modo C"]
        self.__indice = 0

        self.clicked.connect(self.cambiar_modo)

    def cambiar_modo(self):
        self.__indice = (self.__indice + 1) % len(self.__modos)
        nuevo_modo = self.__modos[self.__indice]
        self.setText(nuevo_modo)
        self.modo_cambiado.emit(nuevo_modo)


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Botón con modos")

        cont = QWidget()
        layout = QVBoxLayout()

        self.boton = BotonModo()
        self.etiqueta = QLabel("Estado actual: Modo A")

        self.boton.modo_cambiado.connect(self.actualizar)

        layout.addWidget(self.boton)
        layout.addWidget(self.etiqueta)

        cont.setLayout(layout)
        self.setCentralWidget(cont)

    def actualizar(self, modo):
        self.etiqueta.setText("Estado actual: " + modo)

app = QApplication([])
v = Ventana()
v.show()
app.exec()