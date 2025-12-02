# José Carlos Mora 2ºDAM
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction, QKeySequence

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal con menús")

        barra_menu = self.menuBar()

        menu_archivo = barra_menu.addMenu("&Archivo")

        
        accion_mensaje = QAction("Mostrar mensaje", self)
        accion_mensaje.setShortcut(QKeySequence("Ctrl+M"))
        accion_mensaje.triggered.connect(self.mostrar_mensaje)
        menu_archivo.addAction(accion_mensaje)

      
        menu_archivo.addSeparator()

        
        accion_titulo = QAction("Cambiar título", self)
        accion_titulo.setShortcut(QKeySequence("Ctrl+L"))
        accion_titulo.triggered.connect(self.cambiar_titulo)
        menu_archivo.addAction(accion_titulo)

        
        menu_archivo.addSeparator()

       
        accion_salir = QAction("Salir", self)
        accion_salir.setShortcut(QKeySequence("Ctrl+Q"))
        accion_salir.triggered.connect(self.close)
        menu_archivo.addAction(accion_salir)

    def mostrar_mensaje(self):
        print("Hola desde el menú")

    def cambiar_titulo(self):
        self.setWindowTitle("Título cambiado desde el menú")

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
