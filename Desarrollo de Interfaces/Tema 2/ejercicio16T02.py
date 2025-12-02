#José Carlos Mora 2ºDAM

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,QLabel, QFileDialog, QColorDialog, QFontDialog)
from PySide6.QtGui import QFont
import sys


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de archivo y preferencias")


        contenedor = QWidget()
        layout = QVBoxLayout()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

  
        self.label_texto = QLabel("(No hay texto cargado)")
        self.label_texto.setStyleSheet("background-color: white; padding: 10px;")

   
        boton_abrir = QPushButton("Abrir archivo de texto")
        boton_guardar = QPushButton("Guardar archivo como...")
        boton_color = QPushButton("Elegir color de fondo")
        boton_fuente = QPushButton("Cambiar fuente del texto")


        layout.addWidget(self.label_texto)
        layout.addWidget(boton_abrir)
        layout.addWidget(boton_guardar)
        layout.addWidget(boton_color)
        layout.addWidget(boton_fuente)


        boton_abrir.clicked.connect(self.abrir_archivo)
        boton_guardar.clicked.connect(self.guardar_archivo)
        boton_color.clicked.connect(self.cambiar_color)
        boton_fuente.clicked.connect(self.cambiar_fuente)

  
    def abrir_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir archivo de texto", "", "Archivos de texto (*.txt)")

        if ruta:
            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    contenido = archivo.read()
                self.label_texto.setText(contenido)
            except Exception as e:
                self.label_texto.setText(f"Error al abrir el archivo: {e}")

    def guardar_archivo(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo como...", "", "Archivos de texto (*.txt)")

        if ruta:
            try:
                with open(ruta, "w", encoding="utf-8") as archivo:
                    archivo.write(self.label_texto.text())
            except Exception as e:
                self.label_texto.setText(f"Error al guardar el archivo: {e}")

    def cambiar_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.label_texto.setStyleSheet(f"background-color: {color.name()}; padding: 10px;")

    def cambiar_fuente(self):
        fuente, ok = QFontDialog.getFont()

        if ok:
            self.label_texto.setFont(fuente)



app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
app.exec()
