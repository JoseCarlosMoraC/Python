from PySide6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.show()  # IMPORTANTE: las ventanas están ocultas por defecto.

# Inicia el bucle de eventos.
app.exec()