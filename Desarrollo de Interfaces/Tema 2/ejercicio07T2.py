#José Carlos Mora 2º DAM
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")
        
     
        self.line = QLineEdit()
        self.line.setMaxLength(20)
        self.line.setPlaceholderText("Escribe tu ciudad")

        
        self.line.returnPressed.connect(self.cambiar_titulo)

        self.setCentralWidget(self.line)

    def cambiar_titulo(self):
        texto = self.line.text()
        if texto == "":
            self.setWindowTitle("Sin ciudad")
        else:
            self.setWindowTitle(texto)



app = QApplication([])
window = MainWindow()
window.show()
app.exec()