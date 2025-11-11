# José Carlos Mora 2º DAM

# He creado un QRadioButton como widget central
# Cuando lo marco o desmarco, cambio el título de la ventana
# para mostrar si la función está activada o desactivada
from PySide6.QtWidgets import QApplication, QMainWindow, QRadioButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Función DESACTIVADA")


        self.boton = QRadioButton("Activar función")
        self.boton.setChecked(False)  

      
        self.boton.toggled.connect(self.cambiar_titulo)


        self.setCentralWidget(self.boton)

    def cambiar_titulo(self, estado):
        if estado:
            self.setWindowTitle("Función ACTIVADA")
        else:
            self.setWindowTitle("Función DESACTIVADA")



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
