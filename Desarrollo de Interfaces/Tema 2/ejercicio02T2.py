#José Carlos Mora 2ºDAM

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")

        boton = QPushButton("Encender")
        boton.setCheckable(True)

        boton.clicked.connect(self.el_boton_fue_pulsado)
        boton.clicked.connect(self.el_boton_esta_on)

     
        self.setCentralWidget(boton)

    def el_boton_fue_pulsado(self):
        print("Botón pulsado")

    def el_boton_esta_on(self, checked):
        print("¿Está activo?", checked)
        if checked:
            self.setWindowTitle("Ventana encendida")
        else:
            self.setWindowTitle("Ventana apagada")
        

app = QApplication()
window= MainWindow()
window.show()
app.exec()