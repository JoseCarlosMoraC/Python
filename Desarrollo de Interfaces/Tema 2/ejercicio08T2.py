# José Carlos Mora 2º DAM

from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")

        
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText("Bienvenido/a al editor de texto")  
        self.text_edit.setPlaceholderText("Escribe aquí tu mensaje...")  

     
        self.text_edit.textChanged.connect(self.mostrar_texto)

       
        self.setCentralWidget(self.text_edit)

    def mostrar_texto(self):

        contenido = self.text_edit.toPlainText()
        print(contenido)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
