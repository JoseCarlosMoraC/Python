from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QPushButton

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación con mensaje crítico")
        
        boton = QPushButton("Haz click aquí para ver el mensaje crítico")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        boton_pulsado = QMessageBox.critical(
            self,
            "Ejemplo de cuadro de mensaje crítico",
            "Ha ocurrido un problema al realizar la acción",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard
        )

        if boton_pulsado == QMessageBox.Discard:
            print("Descartado")
        elif boton_pulsado == QMessageBox.NoToAll:
            print("No a todo")
        else:
            print("Ignorado")

app = QApplication()
ventana = VentanaPrincipal()
ventana.show()
app.exec()
