# Proyecto 2 - Formulario de ciudad con QLineEdit, barra de estado y confirmación
# José Carlos Mora 2º DAM

# IMPORTACIONES
from PySide6.QtWidgets import (QApplication, QMainWindow, QLineEdit, 
                               QMessageBox, QToolBar)
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # CONFIGURACIÓN INICIAL
        self.setWindowTitle("Formulario de ciudad")
        
        # CREAR Y CONFIGURAR QLINEEDIT
        # QLineEdit es un campo de texto de una sola línea
        self.line_edit = QLineEdit()
        
        # setMaxLength() limita el número máximo de caracteres que se pueden escribir
        self.line_edit.setMaxLength(20)
        
        # setPlaceholderText() muestra un texto gris cuando el campo está vacío
        # Este texto desaparece cuando el usuario empieza a escribir
        self.line_edit.setPlaceholderText("Escribe tu ciudad")
        
        # CONECTAR SEÑAL returnPressed
        # returnPressed se emite cuando el usuario pulsa Enter en el campo
        # Lo conectamos al método establecer_ciudad
        self.line_edit.returnPressed.connect(self.establecer_ciudad)
        
        # Establecer como widget central
        # QLineEdit puede ser directamente el widget central
        self.setCentralWidget(self.line_edit)
        
        # CREAR MENÚ
        barra_menu = self.menuBar()
        menu_ciudad = barra_menu.addMenu("&Ciudad")  # Alt+C
        
        # CREAR ACCIONES DEL MENÚ
        # Primera acción: Establecer ciudad
        self.accion_establecer = QAction("Establecer ciudad", self)
        # Reutilizamos el mismo método que returnPressed
        self.accion_establecer.triggered.connect(self.establecer_ciudad)
        menu_ciudad.addAction(self.accion_establecer)
        
        # Segunda acción: Borrar ciudad
        self.accion_borrar = QAction("Borrar ciudad", self)
        self.accion_borrar.triggered.connect(self.borrar_ciudad)
        menu_ciudad.addAction(self.accion_borrar)
        
        # CREAR BARRA DE HERRAMIENTAS
        barra_herramientas = QToolBar("Barra principal")
        # Añadimos ambas acciones a la toolbar
        barra_herramientas.addAction(self.accion_establecer)
        barra_herramientas.addAction(self.accion_borrar)
        self.addToolBar(barra_herramientas)
        
        # CREAR BARRA DE ESTADO
        self.barra_estado = self.statusBar()
        # Mensaje inicial sin tiempo límite (se queda permanente hasta que lo cambies)
        self.barra_estado.showMessage("Introduce tu ciudad y pulsa Enter")
    
    # MÉTODO PARA ESTABLECER LA CIUDAD
    def establecer_ciudad(self):
        # Obtenemos el texto actual del QLineEdit
        texto = self.line_edit.text()
        
        # Verificamos si el campo está vacío
        if texto == "":
            # Si está vacío, ponemos un título genérico
            self.setWindowTitle("Sin ciudad")
            # Mostramos mensaje en consola
            print("El campo está vacío")
        else:
            # Si tiene texto, lo usamos como título de la ventana
            self.setWindowTitle(texto)
            # Mostramos la ciudad en consola
            print("Ciudad actual: " + texto)
            # Actualizamos la barra de estado con mensaje temporal
            self.barra_estado.showMessage("Ciudad establecida correctamente", 2000)
    
    # MÉTODO PARA BORRAR LA CIUDAD
    def borrar_ciudad(self):
        # MOSTRAR CUADRO DE CONFIRMACIÓN
        # QMessageBox.question muestra un cuadro con pregunta y botones
        respuesta = QMessageBox.question(
            self,  # Ventana padre
            "Confirmar borrado",  # Título
            "¿Seguro que quieres borrar la ciudad?",  # Pregunta
            QMessageBox.Yes | QMessageBox.No  # Botones a mostrar (combinados con |)
        )
        
        # Verificamos qué botón pulsó el usuario
        if respuesta == QMessageBox.Yes:
            # Si pulsó Yes, borramos todo
            
            # clear() borra el contenido del QLineEdit
            self.line_edit.clear()
            
            # Restauramos el título original
            self.setWindowTitle("Formulario de ciudad")
            
            # Mensaje en barra de estado
            self.barra_estado.showMessage("Ciudad borrada", 2000)

# EJECUCIÓN DE LA APLICACIÓN
app = QApplication([])
window = MainWindow()
window.show()
app.exec()