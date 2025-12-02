from PySide6.QtWidgets import(QApplication,QMainWindow, QWidget, QHBoxLayout, QPushButton)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout horizontal")

        layout_horizontal = QHBoxLayout()

        componente_principal = QWidget()
        componente_principal.setLayout(layout_horizontal)

        self.setCentralWidget(componente_principal)

        layout_horizontal.addWidget(QPushButton("Uno"))
        layout_horizontal.addWidget(QPushButton("Dos"))
        layout_horizontal.addWidget(QPushButton("Tres"))
        layout_horizontal.addWidget(QPushButton("Cuatro"))

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()