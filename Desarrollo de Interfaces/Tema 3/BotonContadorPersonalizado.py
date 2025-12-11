from PySide6.QtWidgets import *
from PySide6.QtCore import Signal
import sys


# ============================================================
# BOTÓN PERSONALIZADO
# ============================================================

class BotonContador(QPushButton):
    # Señal que enviará el número de clics
    clickRegistrado = Signal(int)

    def __init__(self):
        super().__init__("Haz clic")
        self.contador = 0

        # Cuando se pulse, llamará a registrar()
        self.clicked.connect(self.registrar)

    def registrar(self):
        # Suma 1 al contador
        self.contador += 1

        # Emitimos la señal con el número actualizado
        self.clickRegistrado.emit(self.contador)


# ============================================================
# VENTANA PRINCIPAL
# ============================================================

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contador de clics")

        # Layout principal
        cont = QWidget()
        layout = QVBoxLayout()

        # Botón personalizado
        self.boton = BotonContador()

        # Etiqueta que mostrará los clics
        self.lbl = QLabel("Clics: 0")

        # Botón de reset
        self.reset = QPushButton("Resetear")
        self.reset.clicked.connect(self.reiniciar)

        # Conectar señal personalizada del botón
        self.boton.clickRegistrado.connect(self.actualizar)

        layout.addWidget(self.boton)
        layout.addWidget(self.lbl)
        layout.addWidget(self.reset)

        cont.setLayout(layout)
        self.setCentralWidget(cont)

    def actualizar(self, valor):
        # Actualiza la etiqueta con el número recibido
        self.lbl.setText("Clics: " + str(valor))

    def reiniciar(self):
        # Resetea contador y etiqueta
        self.boton.contador = 0
        self.lbl.setText("Clics: 0")


# Lanzar aplicación
app = QApplication(sys.argv)
v = Ventana()
v.show()
app.exec()
