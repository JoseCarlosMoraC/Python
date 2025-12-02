#José Carlos Mora 2ºDAM

from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QMessageBox)
import sys


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de tareas")

        boton = QPushButton("Gestionar tarea")
        boton.clicked.connect(self.gestionar_tarea)
        self.setCentralWidget(boton)

    def gestionar_tarea(self):
        respuesta = QMessageBox.question(
            self,
            "Acción sobre la tarea",
            "¿Qué quieres hacer con la tarea seleccionada?",
            buttons=QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore,
            defaultButton=QMessageBox.Ignore
        )

        if respuesta == QMessageBox.Yes:
            QMessageBox.information(self, "Tarea completada", "La tarea se ha marcado como completada.")
        elif respuesta == QMessageBox.No:
            QMessageBox.information(self, "Tarea pospuesta", "La tarea se ha pospuesto para más tarde.")
        else:
            QMessageBox.information(self, "Sin cambios", "La tarea se mantiene sin cambios.")



app = QApplication()
ventana = VentanaPrincipal()
ventana.show()
app.exec()