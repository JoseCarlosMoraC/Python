#José Carlos Mora 2ºDAM

import os
import sys
from PySide6.QtCore import Qt   
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana con menú y barra de herramientas")

    
        barra_menus = self.menuBar()
        menu_archivo = barra_menus.addMenu("&Archivo")

        
        ruta_base = os.path.dirname(__file__)
        icono_mensaje = QIcon(os.path.join(ruta_base, "mensaje.png"))
        icono_titulo = QIcon(os.path.join(ruta_base, "titulo.png"))
        icono_desactivar = QIcon(os.path.join(ruta_base, "palanca.png"))
        icono_activar = QIcon(os.path.join(ruta_base, "boton-de-encendido.png"))

        
        self.accion_mensaje = QAction(icono_mensaje, "Mostrar mensaje", self)
        self.accion_mensaje.setShortcut(QKeySequence("Ctrl+M"))
        self.accion_mensaje.setWhatsThis("Muestra un mensaje 'Hola' en la consola")
        self.accion_mensaje.triggered.connect(self.mostrar_mensaje)

       
        self.accion_titulo = QAction(icono_titulo, "Cambiar título", self)
        self.accion_titulo.setShortcut(QKeySequence("Ctrl+T"))
        self.accion_titulo.setWhatsThis("Cambia el título de la ventana a 'Título cambiado'")
        self.accion_titulo.triggered.connect(self.cambiar_titulo)

        
        self.accion_desactivar = QAction(icono_desactivar, "Desactivar acciones", self)
        self.accion_desactivar.setShortcut(QKeySequence("Ctrl+D"))
        self.accion_desactivar.setWhatsThis("Desactiva las acciones de mostrar mensaje y cambiar título")
        self.accion_desactivar.triggered.connect(self.desactivar_acciones)

       
        menu_archivo.addAction(self.accion_mensaje)
        menu_archivo.addAction(self.accion_titulo)
        menu_archivo.addAction(self.accion_desactivar)

        
        barra_principal = QToolBar("Barra principal")
        barra_principal.addAction(self.accion_mensaje)
        barra_principal.addAction(self.accion_titulo)
        barra_principal.addAction(self.accion_desactivar)
        barra_principal.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
        self.addToolBar(barra_principal)

        
        barra_secundaria = QToolBar("Barra secundaria")
        self.accion_activar = QAction(icono_activar, "Activar acciones", self)
        self.accion_activar.setShortcut(QKeySequence("Ctrl+A"))
        self.accion_activar.setWhatsThis("Vuelve a activar las acciones desactivadas")
        self.accion_activar.triggered.connect(self.activar_acciones)
        barra_secundaria.addAction(self.accion_activar)
        barra_secundaria.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(barra_secundaria)

  
    def mostrar_mensaje(self):
        print("Hola")

    def cambiar_titulo(self):
        self.setWindowTitle("Título cambiado")

    def desactivar_acciones(self):
        self.accion_mensaje.setEnabled(False)
        self.accion_titulo.setEnabled(False)

    def activar_acciones(self):
        self.accion_mensaje.setEnabled(True)
        self.accion_titulo.setEnabled(True)



app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
sys.exit(app.exec())
