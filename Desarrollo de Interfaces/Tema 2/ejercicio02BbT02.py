#José Carlos Mora 2ºDAM
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

   
        self.boton = QPushButton("Pulsar")
        self.setCentralWidget(self.boton)


        self.boton.pressed.connect(self.boton_presionado)
        self.boton.released.connect(self.boton_liberado)

    def boton_presionado(self):
        print("Botón presionado")
        self.boton.setText("Soltar")

    def boton_liberado(self):
        print("Botón liberado")
        self.boton.setText("Pulsar")



app = QApplication()
window= MainWindow()
window.show()
app.exec()