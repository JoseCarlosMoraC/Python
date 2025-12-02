#José Carlos Mora 2ºDAM

from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox)

class DialogoLogin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        layout = QVBoxLayout()

   
        self.campo_usuario = QLineEdit()
        self.campo_usuario.setPlaceholderText("Usuario")
        layout.addWidget(self.campo_usuario)

        self.campo_password = QLineEdit()
        self.campo_password.setPlaceholderText("Contraseña")
        self.campo_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.campo_password)

   
        boton_validar = QPushButton("Iniciar sesión")
        boton_validar.clicked.connect(self.validar)
        layout.addWidget(boton_validar)

        self.setLayout(layout)

    def validar(self):
        usuario = self.campo_usuario.text()
        password = self.campo_password.text()

        if usuario == "admin" and password == "admin":
            self.accept()  
        else:
            QMessageBox.warning(self, "Error", "El usuario o la contraseña son incorrectos")

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")

      
        self.label = QLabel("Ventana principal")
        self.setCentralWidget(self.label)


app = QApplication([])

dialogo = DialogoLogin()
if dialogo.exec() == QDialog.Accepted:
    ventana = VentanaPrincipal()
    ventana.showMaximized()  
    app.exec()
