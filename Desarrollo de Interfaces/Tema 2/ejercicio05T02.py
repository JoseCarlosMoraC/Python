#José Carlos Mora 2ºDAM
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Preferencias del usuario")

        #widget = QCheckBox("Casilla normal")
        #widget2 = QCheckBox("Casilla marcado por defecto")
        #widget2.setCheckState(Qt.Checked)
        widget3 = QCheckBox("Casilla tri-state")
        widget3.setTristate(True)
        
        #widget.stateChanged.connect(self.show_state)
        #widget2.stateChanged.connect(self.show_state)
        widget3.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget3)


    def show_state(self, s):
        if s == 2:
            print("Marcado completamente")
        elif s == 0:
            print("Desmarcado")
        else:
            print("Marcado parcialmente")
        print (s)

app = QApplication([])
window = MainWindow()
window.show()  
app.exec()
  