from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicación")
        self.setMinimumSize(QSize(480, 320))

        texto = QLineEdit()
        texto.textChanged.connect(self.texto_modificado)
        self.setCentralWidget(texto)

        self.texto = texto

    def texto_modificado(self): 
        self.setWindowTitle(self.texto.text())

app = QApplication()
window = MainWindow()
window.show()
app.exec()
