# José Carlos Mora 2º DAM

# He creado un QSlider como widget central para controlar el nivel de brillo
# El rango va de 0 a 100 y el valor inicial es 50.
# Cada vez que cambio el valor, se muestra el nivel de brillo actual en la consola
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
from PySide6.QtCore import Qt  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.slider = QSlider(Qt.Horizontal) 
        self.slider.setRange(0, 100)          
        self.slider.setValue(50)              


        self.slider.valueChanged.connect(self.mostrar_brillo)


        self.setCentralWidget(self.slider)


        self.mostrar_brillo(self.slider.value())

    def mostrar_brillo(self, valor):
        print("Nivel de brillo:", valor, "%")


app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
