#José Carlos Mora 2ºDAM

import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QToolBar, QDockWidget, QTextEdit)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")


        self.setCentralWidget(QLabel("Área principal de la aplicación"))


        self.dock1 = QDockWidget("Panel 1", self)
        self.dock1.setWidget(QTextEdit("Panel de notas"))
        self.dock1.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock1)


        self.dock2 = QDockWidget("Panel 2", self)
        self.dock2.setFeatures(QDockWidget.DockWidgetFloatable)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock2)

        self.dock3 = QDockWidget("Panel 3", self)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock3)


        toolbar = QToolBar("Barra principal")
        icono = QIcon(os.path.join(os.path.dirname(__file__), "console-log-icon.png"))
        accion = QAction(icono, "Imprimir por consola", self)
        accion.triggered.connect(self.imprimir_consola)
        toolbar.addAction(accion)
        self.addToolBar(toolbar)


        self.statusBar().showMessage("Listo. Paneles creados correctamente.")


    def imprimir_consola(self):
        print("Imprimiendo por consola...")


app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
app.exec()
