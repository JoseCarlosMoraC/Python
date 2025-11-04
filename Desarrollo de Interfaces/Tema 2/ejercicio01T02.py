#José Carlos Mora 2º DAM


from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtCore import QSize

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        button = QPushButton("Púlsame muy fuerte")
        self.setCentralWidget(button)
        #self.setFixedSize(QSize(600,500))
        self.setMaximumSize(QSize(600,400))
        self.setMinimumSize(QSize(300,200))

class WidgetInd (QWidget):
    def __init__(self):
        super().__init__()
    

app = QApplication([])
window = MainWindow()
window.show()
widget = WidgetInd()
widget.show()
app.exec()

