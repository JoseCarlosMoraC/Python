#José Carlos Mora 2ºDAM

from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QDialog, QLabel, QVBoxLayout, QDialogButtonBox)
from PySide6.QtCore import Qt
import sys


class DialogoModo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Elegir modo de operación")

      
        etiqueta = QLabel("Selecciona el modo de operación que quieres activar:")

        
        botones = QDialogButtonBox.Yes | QDialogButtonBox.No | QDialogButtonBox.Help
        self.caja = QDialogButtonBox(botones)

       
        self.boton_pulsado = None

        self.caja.button(QDialogButtonBox.Yes).clicked.connect(self.boton_yes)
        self.caja.button(QDialogButtonBox.No).clicked.connect(self.boton_no)
        self.caja.button(QDialogButtonBox.Help).clicked.connect(self.boton_help)

 
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        layout.addWidget(self.caja)
        self.setLayout(layout)

    def boton_yes(self):
        self.boton_pulsado = "yes"
        self.accept()

    def boton_no(self):
        self.boton_pulsado = "no"
        self.accept()

    def boton_help(self):
        self.boton_pulsado = "help"
        self.reject()


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selección de modo de operación")


        boton = QPushButton("Elegir modo")
        boton.clicked.connect(self.abrir_dialogo)
        self.setCentralWidget(boton)

    def abrir_dialogo(self):
        dialogo = DialogoModo(self)
        resultado = dialogo.exec()

        if resultado == QDialog.Accepted:
            if dialogo.boton_pulsado == "yes":
                print("Modo A activado")
            elif dialogo.boton_pulsado == "no":
                print("Modo B activado")
        else:
            print("Se ha solicitado ayuda")



app = QApplication()
ventana = VentanaPrincipal()
ventana.show()
app.exec()