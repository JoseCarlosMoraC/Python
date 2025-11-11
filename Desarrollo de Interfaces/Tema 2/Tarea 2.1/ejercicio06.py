# José Carlos Mora 2º DAM

## He creado un QDial como widget central para controlar el volumen
# El rango va de 0 a 10 y las muescas son visibles para facilitar la selección
# Cada vez que cambio el valor, se actualiza el título de la ventana con el volumen actual
# Si se alcanza el valor máximo (10), se muestra un mensaje en la consola

from PySide6.QtWidgets import QApplication, QMainWindow, QDial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

     
        self.dial = QDial()
        self.dial.setRange(0, 10)          
        self.dial.setNotchesVisible(True)   
        self.dial.setValue(0)              

        
        self.dial.valueChanged.connect(self.cambiar_volumen)

        
        self.setCentralWidget(self.dial)

       
        self.cambiar_volumen(self.dial.value())

    def cambiar_volumen(self, valor):
        
        self.setWindowTitle("Volumen: " + str(valor) + " / 10")

        
        if valor == 10:
            print("¡Volumen máximo alcanzado!")



app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
