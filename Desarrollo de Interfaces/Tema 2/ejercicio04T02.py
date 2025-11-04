#José Carlos Mora 2ºDAM
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap

basedir = os.path.dirname(__file__)
print("Current working folder:", os.getcwd())  
print("Paths are relative to:", basedir)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        etiqueta = QLabel()
        etiqueta.setPixmap(QPixmap(os.path.join(basedir, "foto.jpg")))  
        etiqueta.setScaledContents(True)
        self.setCentralWidget(etiqueta)

app = QApplication([])
window = MainWindow()
window.show()  
app.exec()
