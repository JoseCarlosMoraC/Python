from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt
import sys


class Dibujo(QWidget):
    def __init__(self):
        super().__init__()

        # Título y tamaño de la ventana
        self.setWindowTitle("Panel de dibujo")
        self.setGeometry(200, 200, 600, 400)

        # Lista donde guardamos todas las líneas dibujadas
        self.lineas = []

        # Variable que indica si el usuario está dibujando
        self.dibujando = False

        # Botón para borrar el dibujo
        self.boton = QPushButton("Borrar dibujo")
        self.boton.clicked.connect(self.borrar)

        # Etiqueta para contar cuántas líneas se han dibujado
        self.info = QLabel("Líneas: 0")

        # Layout inferior
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.boton)
        layout.addWidget(self.info)
        self.setLayout(layout)

    def borrar(self):
        # Eliminamos todas las líneas dibujadas
        self.lineas.clear()
        self.info.setText("Líneas: 0")
        self.update()

    # ------------------- EVENTOS DEL RATÓN -------------------

    def mousePressEvent(self, event):
        # Cuando se pulsa el botón del ratón, empieza una nueva línea
        self.dibujando = True
        self.lineas.append([])  # Nueva línea vacía
        self.lineas[-1].append(event.pos())  # Primer punto
        self.update()

    def mouseMoveEvent(self, event):
        # Si estamos dibujando, añadimos puntos continuamente
        if self.dibujando:
            self.lineas[-1].append(event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        # Cuando se suelta el ratón se termina la línea
        self.dibujando = False
        self.info.setText("Líneas: " + str(len(self.lineas)))

    # ---------------------------------------------------------

    def paintEvent(self, event):
        # Dibujamos todas las líneas
        p = QPainter(self)

        # Configuramos el lápiz (color azul y grosor 3)
        lapiz = QPen(QColor(0, 70, 200), 3)
        p.setPen(lapiz)

        # Dibujar cada línea punto a punto
        for linea in self.lineas:
            for i in range(len(linea) - 1):
                p.drawLine(linea[i], linea[i + 1])


# Lanzar programa
app = QApplication(sys.argv)
v = Dibujo()
v.show()
app.exec()
