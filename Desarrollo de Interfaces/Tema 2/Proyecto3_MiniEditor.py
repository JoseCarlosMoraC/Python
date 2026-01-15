# Proyecto 3 - Mini editor de notas con menús, barra de herramientas y archivos
# José Carlos Mora 2º DAM

# IMPORTACIONES
from PySide6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QTextEdit,
                               QWidget, QVBoxLayout, QPushButton, QMessageBox,
                               QToolBar, QFileDialog)
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # CONFIGURACIÓN INICIAL
        self.setWindowTitle("Editor de notas")
        
        # CREAR CONTENEDOR Y LAYOUT
        # Necesitamos un contenedor porque vamos a usar varios widgets
        contenedor = QWidget()
        # QVBoxLayout organiza los widgets verticalmente (uno debajo del otro)
        layout = QVBoxLayout()
        contenedor.setLayout(layout)
        
        # CREAR QLINEEDIT PARA EL TÍTULO
        # Este campo será para el título de la nota
        self.line_titulo = QLineEdit()
        self.line_titulo.setPlaceholderText("Título de la nota")
        
        # CONECTAR textChanged
        # textChanged se emite cada vez que cambia el texto (incluso si borras)
        # Lo conectamos para actualizar el título de la ventana en tiempo real
        self.line_titulo.textChanged.connect(self.actualizar_titulo)
        
        # CREAR QTEXTEDIT PARA EL CONTENIDO
        # QTextEdit es un área de texto multilínea (como un editor)
        self.text_contenido = QTextEdit()
        
        # setPlainText() establece texto inicial (plano, sin formato)
        self.text_contenido.setPlainText("Bienvenido al editor de notas. Escribe aquí tu contenido...")
        
        # Conectar textChanged del QTextEdit
        # Se ejecutará cada vez que el usuario escriba o borre algo
        self.text_contenido.textChanged.connect(self.mostrar_contenido)
        
        # CREAR BOTÓN "ACERCA DE"
        boton_acerca = QPushButton("Acerca de")
        boton_acerca.clicked.connect(self.mostrar_acerca_de)
        
        # AÑADIR WIDGETS AL LAYOUT
        # El orden de addWidget determina el orden visual (de arriba a abajo)
        layout.addWidget(self.line_titulo)  # Título arriba
        layout.addWidget(self.text_contenido)  # Contenido en medio (ocupará más espacio)
        layout.addWidget(boton_acerca)  # Botón abajo
        
        # Establecer como widget central
        self.setCentralWidget(contenedor)
        
        # CREAR MENÚ ARCHIVO
        barra_menu = self.menuBar()
        menu_archivo = barra_menu.addMenu("&Archivo")  # Alt+A
        
        # CREAR ACCIONES DEL MENÚ
        # Acción 1: Nuevo
        self.accion_nuevo = QAction("Nuevo", self)
        self.accion_nuevo.triggered.connect(self.nuevo)
        menu_archivo.addAction(self.accion_nuevo)
        
        # Acción 2: Abrir
        self.accion_abrir = QAction("Abrir...", self)
        self.accion_abrir.triggered.connect(self.abrir)
        menu_archivo.addAction(self.accion_abrir)
        
        # Acción 3: Guardar como
        self.accion_guardar = QAction("Guardar como...", self)
        self.accion_guardar.triggered.connect(self.guardar)
        menu_archivo.addAction(self.accion_guardar)
        
        # CREAR BARRA DE HERRAMIENTAS
        barra_herramientas = QToolBar("Barra principal")
        # Añadimos las tres acciones a la toolbar
        barra_herramientas.addAction(self.accion_nuevo)
        barra_herramientas.addAction(self.accion_abrir)
        barra_herramientas.addAction(self.accion_guardar)
        self.addToolBar(barra_herramientas)
        
        # CREAR BARRA DE ESTADO
        self.barra_estado = self.statusBar()
        self.barra_estado.showMessage("Listo. Esperando acción...", 3000)
    
    # MÉTODO PARA ACTUALIZAR EL TÍTULO DE LA VENTANA
    def actualizar_titulo(self):
        # Obtenemos el texto actual del campo de título
        texto = self.line_titulo.text()
        
        # Si está vacío, mostramos el título por defecto
        if texto == "":
            self.setWindowTitle("Editor de notas")
        else:
            # Si tiene texto, lo usamos como título de la ventana
            self.setWindowTitle(texto)
    
    # MÉTODO PARA MOSTRAR CONTENIDO EN CONSOLA
    def mostrar_contenido(self):
        # toPlainText() devuelve todo el texto del QTextEdit sin formato
        contenido = self.text_contenido.toPlainText()
        
        # Mostramos solo los primeros 50 caracteres para no saturar la consola
        # [:50] es slicing de Python: toma desde el inicio hasta el carácter 50
        print("Contenido modificado: " + contenido[:50] + "...")
    
    # MÉTODO PARA CREAR NUEVA NOTA
    def nuevo(self):
        # clear() limpia completamente el contenido de los campos
        self.line_titulo.clear()
        self.text_contenido.clear()
        
        # Mensaje en barra de estado
        self.barra_estado.showMessage("Nota nueva", 2000)
    
    # MÉTODO PARA ABRIR ARCHIVO
    def abrir(self):
        # QFileDialog.getOpenFileName muestra un cuadro para seleccionar archivo
        # Devuelve una tupla: (ruta_seleccionada, filtro_usado)
        # Usamos _ para el filtro porque no nos interesa
        ruta, _ = QFileDialog.getOpenFileName(
            self,  # Ventana padre
            "Abrir archivo",  # Título del diálogo
            "",  # Directorio inicial (vacío = directorio actual)
            "Archivos de texto (*.txt)"  # Filtro de archivos
        )
        
        # Si el usuario seleccionó un archivo (no canceló)
        if ruta:
            # Mostramos la ruta en consola
            print("Ruta seleccionada: " + ruta)
            
            # Mostramos la ruta en la barra de estado
            self.barra_estado.showMessage("Archivo seleccionado: " + ruta, 3000)
    
    # MÉTODO PARA GUARDAR ARCHIVO
    def guardar(self):
        # QFileDialog.getSaveFileName muestra un cuadro para guardar archivo
        # Similar a getOpenFileName pero para guardar
        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo como...",
            "",
            "Archivos de texto (*.txt)"
        )
        
        if ruta:
            print("Ruta de guardado: " + ruta)
            self.barra_estado.showMessage("Ruta de guardado elegida: " + ruta, 3000)
    
    # MÉTODO PARA MOSTRAR DIÁLOGO "ACERCA DE"
    def mostrar_acerca_de(self):
        # QMessageBox.information para mostrar información general
        # Usamos \n para saltos de línea en el mensaje
        QMessageBox.information(
            self,
            "Acerca de",
            "Este es un editor de notas de prueba.\nCreado con PySide6 para practicar interfaces."
        )

# EJECUCIÓN
app = QApplication([])
window = MainWindow()
window.show()
app.exec()