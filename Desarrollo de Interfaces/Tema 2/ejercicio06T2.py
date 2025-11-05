#José Carlos Mora 2ºDAM
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")

        combo = QComboBox()
        combo.addItems(["Python", "Java", "C++", "Kotlin"])
        combo.setEditable(True)
        
        combo.setInsertPolicy(QComboBox.InsertAfterCurrent)
        combo.setMaxCount(10)   
       
        combo.currentIndexChanged.connect(self.cambio_indice)
        combo.currentTextChanged.connect(self.cambio_texto)

        self.setCentralWidget(combo)

    def cambio_indice(self, i):
        print("Índice:", i)

    def cambio_texto(self, s):
        print("Texto:", s)
        self.setWindowTitle(s)

app = QApplication()
window = MainWindow()
window.show()
app.exec()