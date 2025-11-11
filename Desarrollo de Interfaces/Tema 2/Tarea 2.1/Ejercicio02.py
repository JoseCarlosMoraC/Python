# José Carlos Mora 2º DAM

from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pestaña 1")

   
        self.tabs = QTabWidget()

        
        self.tabs.addTab(QLabel("Bienvenido"), "Pestaña 1")
        self.tabs.addTab(QLabel("Segunda pestaña"), "Pestaña 2")
        self.tabs.addTab(QLabel("Tercera pestaña"), "Pestaña 3")

      
        self.titulos = ["Pestaña 1", "Pestaña 2", "Pestaña 3"]


        self.tabs.currentChanged.connect(self.cambiar_titulo)


        self.setCentralWidget(self.tabs)

    def cambiar_titulo(self, indice):
        print(indice)
        self.setWindowTitle(self.titulos[indice])



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
