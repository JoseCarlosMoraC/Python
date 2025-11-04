from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox("Esto es un checkbox")
        widget.setCheckState(Qt.Checked)

        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self,s):
        state = Qt.CheckState(s)
        print(state == Qt.CheckState.Checked)
        print(state)
        print(s)

app = QApplication([])
window = MainWindow()
window.show()  
app.exec()
  