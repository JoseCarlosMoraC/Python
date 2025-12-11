from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PySide6.QtCore import Qt
import sys


class BarraProgreso(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Barra de progreso")

        self.barra = QProgressBar()
        self.barra.setRange(0, 100)
        self.barra.setValue(0)

        # Color personalizado mediante estilo
        self.barra.setStyleSheet("""
            QProgressBar {
                border: 2px solid black;
                padding: 3px;
            }
            QProgressBar::chunk {
                background-color: green;
            }
        """)

        self.btn = QPushButton("Avanzar")
        self.btn.clicked.connect(self.avanzar)

        l = QVBoxLayout()
        l.addWidget(self.barra)
        l.addWidget(self.btn)

        self.setLayout(l)

    def avanzar(self):
        valor = self.barra.value()
        if valor < 100:
            self.barra.setValue(valor + 10)


app = QApplication(sys.argv)
v = BarraProgreso()
v.show()
app.exec()
