from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout anidados")

        layout_principal = QHBoxLayout()

    
        layout_izquierda = QVBoxLayout()
        layout_izquierda.addWidget(QPushButton("V1"))
        layout_izquierda.addWidget(QPushButton("V2"))
        layout_izquierda.addWidget(QPushButton("V3"))
        layout_izquierda.addWidget(QPushButton("V4"))
      

       
        layout_derecha = QHBoxLayout()
        layout_derecha.addWidget(QPushButton("H1"))
        layout_derecha.addWidget(QPushButton("H2"))
        layout_derecha.addWidget(QPushButton("H3"))
        layout_derecha.addWidget(QPushButton("H4"))


  
        layout_principal.addLayout(layout_izquierda)
        layout_principal.addLayout(layout_derecha)

      
        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)




app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
