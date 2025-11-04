#José Carlos Mora 2ºDAM
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")

        etiqueta = QLabel("Sistema en espera")

        fuente = etiqueta.font()
        fuente.setPointSize(24) 
        etiqueta.setFont(fuente)
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        self.setCentralWidget(etiqueta)

        etiqueta.setText("Sistema operativo iniciado")

app = QApplication()
window = MainWindow()
window.show()
app.exec()
