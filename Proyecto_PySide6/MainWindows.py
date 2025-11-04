import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclase de QMainWindow para personalizar la ventana principal de la aplicación
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        # Establecer un tamaño fijo para la ventana
        self.setFixedSize(QSize(400, 300))

        # Establecer el widget central de la ventana
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()