#José Carlos Mora 2ºDAM
import os
import sys
import platform
import getpass
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")

      
        barra_menus = self.menuBar()
        menu_archivo = barra_menus.addMenu("&Archivo")


        ruta_base = os.path.dirname(__file__)
        icono_temp = QIcon(os.path.join(ruta_base, "mensaje.png"))
        icono_clear = QIcon(os.path.join(ruta_base, "titulo.png"))
        icono_info = QIcon(os.path.join(ruta_base, "boton-de-encendido.png"))

       
        self.accion_temp = QAction(icono_temp, "Mostrar mensaje temporal", self)
        self.accion_temp.setShortcut(QKeySequence("Ctrl+T"))
        self.accion_temp.triggered.connect(self.mostrar_mensaje_temporal)

       
        self.accion_clear = QAction(icono_clear, "Limpiar mensaje", self)
        self.accion_clear.setShortcut(QKeySequence("Ctrl+L"))
        self.accion_clear.triggered.connect(self.limpiar_mensaje)

       
        self.accion_info = QAction(icono_info, "Mostrar información del sistema", self)
        self.accion_info.setShortcut(QKeySequence("Ctrl+I"))
        self.accion_info.triggered.connect(self.mostrar_info_sistema)

  
        menu_archivo.addAction(self.accion_temp)
        menu_archivo.addAction(self.accion_clear)
        menu_archivo.addAction(self.accion_info)

     
        barra_principal = QToolBar("Barra principal")
        barra_principal.addAction(self.accion_temp)
        barra_principal.addAction(self.accion_clear)
        barra_principal.addAction(self.accion_info)
        barra_principal.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(barra_principal)

      
        self.barra_estado = self.statusBar()

        
        usuario = getpass.getuser()
        self.barra_estado.addPermanentWidget(QLabel(f"Usuario: {usuario}"))

   
        self.barra_estado.showMessage("Aplicación iniciada correctamente", 2000)

       
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mensaje_alternado)
        self.timer.start(3000)
        self.flag = True

    def mostrar_mensaje_temporal(self):
        self.barra_estado.showMessage("Mensaje temporal: desaparece en 3 segundos", 3000)

    def limpiar_mensaje(self):
        self.barra_estado.clearMessage()

    def mostrar_info_sistema(self):
        sistema = platform.system()
        self.barra_estado.addWidget(QLabel(sistema))

    def mensaje_alternado(self):
        if self.flag:
            self.barra_estado.showMessage("Esperando acción…", 1500)
        else:
            self.barra_estado.showMessage("Listo para trabajar", 1500)
        self.flag = not self.flag


app = QApplication()
ventana = VentanaPrincipal()
ventana.show()
app.exec()
