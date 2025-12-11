from PySide6.QtWidgets import *
from PySide6.QtCore import Signal
from PySide6.QtGui import QColor, QPalette
import sys


# ============================================================
# QTextEdit PERSONALIZADO
# ============================================================

class TextoLimitado(QTextEdit):
    # Señales personalizadas
    longitudCambiada = Signal(int)
    limiteSuperado = Signal(bool)

    maximo = 150   # Límite de caracteres

    def __init__(self):
        super().__init__()

        self.setPlaceholderText("Escribe algo...")

        # Cuando cambia el texto → llamar verificar()
        self.textChanged.connect(self.verificar)

        # Colores iniciales
        self.restaurar_color()

    # Fondo blanco inicial
    def restaurar_color(self):
        pal = self.palette()
        pal.setColor(QPalette.Base, QColor(255, 255, 255))
        self.setPalette(pal)

    # Verificar cada vez que cambia el texto
    def verificar(self):
        texto = self.toPlainText()
        longitud = len(texto)

        # Emitir señales
        self.longitudCambiada.emit(longitud)
        self.limiteSuperado.emit(longitud > self.maximo)

        # Cambiar color de fondo
        self.cambiar_color(longitud)

    # Cambia el color según longitud
    def cambiar_color(self, longitud):
        pal = self.palette()

        if longitud > self.maximo:
            # Rojo si se excede
            pal.setColor(QPalette.Base, QColor(255, 150, 150))
        else:
            # De blanco a rojo progresivamente
            intensidad = int(255 * (1 - longitud / self.maximo))
            pal.setColor(QPalette.Base, QColor(255, intensidad, intensidad))

        self.setPalette(pal)


# ============================================================
# VENTANA PRINCIPAL
# ============================================================

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Editor con límite de caracteres")

        cont = QWidget()
        layout = QVBoxLayout()

        # Etiquetas informativas
        self.contador = QLabel("Caracteres: 0 / 150")
        self.info = QLabel("Escribe tranquilo...")

        # Editor personalizado
        self.texto = TextoLimitado()

        # Botón limpiar
        self.boton = QPushButton("Limpiar")
        self.boton.clicked.connect(self.limpiar_texto)

        # Conectar señales
        self.texto.longitudCambiada.connect(self.actualizar_contador)
        self.texto.limiteSuperado.connect(self.mostrar_estado)

        # Añadir componentes
        layout.addWidget(self.contador)
        layout.addWidget(self.texto)
        layout.addWidget(self.boton)
        layout.addWidget(self.info)

        cont.setLayout(layout)
        self.setCentralWidget(cont)

    # Actualizar texto del contador
    def actualizar_contador(self, valor):
        self.contador.setText("Caracteres: " + str(valor) + " / 150")

    # Mostrar aviso si se pasa del límite
    def mostrar_estado(self, superado):
        if superado:
            self.info.setText("Has superado el límite")
        else:
            self.info.setText("Escribe tranquilo...")

    # Borrar texto
    def limpiar_texto(self):
        self.texto.clear()
        self.info.setText("Texto borrado correctamente")


# --- Ejecutar ---
app = QApplication(sys.argv)
v = Ventana()
v.show()
app.exec()
