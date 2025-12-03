from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QCheckBox,QPushButton, QLineEdit, QRadioButton, QComboBox)
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")

        contenedor = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(18)

        titulo = QLabel("Fútbol")
        layout.addWidget(titulo)


        layout.addWidget(QLabel("Pequeño cuestionario sobre fútbol:"))
        self.checkbox = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.checkbox)


        layout.addWidget(QLabel("¿Te gusta el fútbol?"))
        self.boton = QPushButton("Confirmar")
        layout.addWidget(self.boton)


        layout.addWidget(QLabel("¿Cuál ha sido la máxima categoría en la que ha estado CD Gerena?"))
        self.line = QLineEdit()
        self.line.setPlaceholderText("Escribelo aquí")
        layout.addWidget(self.line)


        layout.addWidget(QLabel("Mejor equipo del mundo"))
        self.radio1 = QRadioButton("Real Madrid")
        self.radio2 = QRadioButton("FC Barcelona")
        self.radio3 = QRadioButton("CDM Gerena")
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)


        layout.addWidget(QLabel("Mejor entrenador del mundo"))
        self.combo = QComboBox()
        self.combo.addItems(["JC Mora", "JC Mora", "JC Mora"])
        layout.addWidget(self.combo)

        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

def cargar_estilos(app, archivo_qss):
    ruta_script = os.path.abspath(os.path.dirname(__file__))
    ruta_qss = os.path.join(ruta_script, archivo_qss)

    with open(ruta_qss, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        app.setStyleSheet(contenido)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    cargar_estilos(app, "Mora_JC_estilos_T3.1.qss")

    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
