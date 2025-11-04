
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        etiqueta = QLabel()
        etiqueta.setPixmap(QPixmap(r"C:\Users\alumno\Desktop\DAM\Proyectos Python\foto.jpg"))  
        etiqueta.setScaledContents(True)
        self.setCentralWidget(etiqueta)

app = QApplication([])
window = MainWindow()
window.show()  
app.exec()
