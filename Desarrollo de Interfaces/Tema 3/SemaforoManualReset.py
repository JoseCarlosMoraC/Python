from PySide6.QtWidgets import *
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QTimer
import sys


class Semaforo(QWidget):
    def __init__(self):
        super().__init__()

        # Estado inicial del semáforo
        self.__estado = "rojo"

        # Timer para modo automático
        self.timer = QTimer()
        self.timer.setInterval(1500)
        self.timer.timeout.connect(self.cambiar)

        self.modo_auto = False

        self.setWindowTitle("Semáforo completo")
        self.setGeometry(200, 100, 300, 450)

        # Botón para cambiar manualmente
        self.botonCambiar = QPushButton("Cambiar")
        self.botonCambiar.clicked.connect(self.cambiar)

        # Botón activar/desactivar modo automático
        self.botonAuto = QPushButton("Auto")
        self.botonAuto.clicked.connect(self.alternar)

        # Botón resetear a ROJO
        self.botonReset = QPushButton("Reset")
        self.botonReset.clicked.connect(self.resetear)

        # Layout inferior
        l = QVBoxLayout()
        l.addStretch()
        l.addWidget(self.botonCambiar)
        l.addWidget(self.botonAuto)
        l.addWidget(self.botonReset)
        self.setLayout(l)

    # Cambiar estado del semáforo manual o automático
    def cambiar(self):
        if self.__estado == "rojo":
            self.__estado = "amarillo"
        elif self.__estado == "amarillo":
            self.__estado = "verde"
        else:
            self.__estado = "rojo"

        # Redibujar
        self.update()

    # Activar / desactivar automático
    def alternar(self):
        if self.modo_auto:
            self.timer.stop()
            self.modo_auto = False
            self.botonAuto.setText("Auto")
        else:
            self.timer.start()
            self.modo_auto = True
            self.botonAuto.setText("Parar")

    # Resetear semáforo al estado inicial
    def resetear(self):
        self.__estado = "rojo"
        self.update()

        # Apagar automático si estaba encendido
        if self.modo_auto:
            self.timer.stop()
            self.modo_auto = False
            self.botonAuto.setText("Auto")

    # Dibujar luces
    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        apagado = QColor(70, 70, 70)

        rojo = QColor(255, 0, 0)
        amarillo = QColor(255, 255, 0)
        verde = QColor(0, 255, 0)

        # Caja del semáforo
        p.setBrush(QColor(40, 40, 40))
        p.drawRoundedRect(70, 20, 160, 350, 20, 20)

        # Luz ROJA
        if self.__estado == "rojo":
            p.setBrush(rojo)
        else:
            p.setBrush(apagado)
        p.drawEllipse(110, 50, 80, 80)

        # Luz AMARILLA
        if self.__estado == "amarillo":
            p.setBrush(amarillo)
        else:
            p.setBrush(apagado)
        p.drawEllipse(110, 150, 80, 80)

        # Luz VERDE
        if self.__estado == "verde":
            p.setBrush(verde)
        else:
            p.setBrush(apagado)
        p.drawEllipse(110, 250, 80, 80)


# Ejecutar
app = QApplication(sys.argv)
v = Semaforo()
v.show()
app.exec()
