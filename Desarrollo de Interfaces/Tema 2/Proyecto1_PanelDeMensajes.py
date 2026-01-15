# Proyecto 1 - Panel de mensajes con menú, barra de herramientas y mensaje simple
# José Carlos Mora 2º DAM

# IMPORTACIONES
# Importamos las clases necesarias de PySide6
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                               QWidget, QVBoxLayout, QMessageBox, QToolBar)
from PySide6.QtGui import QAction  # Para crear acciones en menús y toolbars
from PySide6.QtCore import Qt  # Para constantes como alineación

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Llamamos al constructor de la clase padre QMainWindow
        
        # CONFIGURACIÓN INICIAL DE LA VENTANA
        self.setWindowTitle("Panel de mensajes")  # Título de la ventana
        
        # CREAR LAYOUT CONTENEDOR
        # Como QMainWindow necesita un widget central, creamos un contenedor
        contenedor = QWidget()  # Widget vacío que contendrá nuestro layout
        layout = QVBoxLayout()  # Layout vertical para organizar widgets uno debajo del otro
        contenedor.setLayout(layout)  # Asignamos el layout al contenedor
        
        # CREAR Y CONFIGURAR EL QLABEL
        # QLabel es una etiqueta de texto que se puede personalizar
        self.etiqueta = QLabel("Sistema en espera")  # Texto inicial
        
        # Configurar la fuente del texto
        fuente = self.etiqueta.font()  # Obtenemos la fuente actual
        fuente.setPointSize(20)  # Cambiamos el tamaño a 20 puntos
        self.etiqueta.setFont(fuente)  # Aplicamos la fuente modificada
        
        # Alinear el texto (horizontal y verticalmente al centro)
        # Se usa el operador | para combinar múltiples flags de alineación
        self.etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # CREAR BOTÓN PARA MOSTRAR MENSAJE
        boton_info = QPushButton("Mostrar información del sistema")
        # Conectar el clic del botón con el método mostrar_mensaje_info
        # clicked es la señal que emite el botón cuando se pulsa
        boton_info.clicked.connect(self.mostrar_mensaje_info)
        
        # AÑADIR WIDGETS AL LAYOUT
        layout.addWidget(self.etiqueta)  # Añadimos la etiqueta
        layout.addWidget(boton_info)  # Añadimos el botón debajo
        
        # ESTABLECER EL CONTENEDOR COMO WIDGET CENTRAL
        # QMainWindow requiere un widget central obligatoriamente
        self.setCentralWidget(contenedor)
        
        # CREAR MENÚ
        # menuBar() crea o devuelve la barra de menú de la ventana
        barra_menu = self.menuBar()
        # addMenu() crea un nuevo menú. El & indica que la siguiente letra será atajo
        menu_acciones = barra_menu.addMenu("&Acciones")  # Alt+A abre este menú
        
        # CREAR ACCIÓN "MOSTRAR SALUDO"
        # QAction representa una acción que puede estar en menús y toolbars
        self.accion_saludo = QAction("Mostrar saludo", self)
        # triggered es la señal que se emite cuando se activa la acción
        self.accion_saludo.triggered.connect(self.mostrar_saludo)
        # Añadimos la acción al menú
        menu_acciones.addAction(self.accion_saludo)
        
        # CREAR BARRA DE HERRAMIENTAS
        # QToolBar es una barra con iconos/botones para acceso rápido
        barra_herramientas = QToolBar("Barra principal")
        # Añadimos la misma acción a la toolbar (se puede reutilizar)
        barra_herramientas.addAction(self.accion_saludo)
        # addToolBar() añade la toolbar a la ventana
        self.addToolBar(barra_herramientas)
        
        # CREAR BARRA DE ESTADO
        # statusBar() crea o devuelve la barra de estado (parte inferior)
        self.barra_estado = self.statusBar()
        # showMessage() muestra un mensaje temporal (3000 ms = 3 segundos)
        self.barra_estado.showMessage("Listo. Esperando acción...", 3000)
    
    # MÉTODO PARA MOSTRAR SALUDO
    def mostrar_saludo(self):
        # Este método se ejecuta cuando se activa la acción desde menú o toolbar
        
        # Cambiamos el texto del QLabel
        self.etiqueta.setText("Sistema operativo iniciado")
        
        # Cambiamos el título de la ventana
        self.setWindowTitle("Sistema operativo iniciado")
        
        # Actualizamos la barra de estado con un mensaje temporal de 2 segundos
        self.barra_estado.showMessage("Saludo mostrado", 2000)
    
    # MÉTODO PARA MOSTRAR MENSAJE INFORMATIVO
    def mostrar_mensaje_info(self):
        # QMessageBox.information muestra un cuadro de diálogo informativo
        # Parámetros: ventana padre, título, mensaje
        QMessageBox.information(
            self,  # Ventana padre (este MainWindow)
            "Información del sistema",  # Título del cuadro
            "El sistema está iniciado correctamente y funcionando."  # Mensaje
        )

# CÓDIGO DE EJECUCIÓN
# Este bloque solo se ejecuta si este archivo es el principal
app = QApplication([])  # Creamos la aplicación Qt
window = MainWindow()  # Creamos nuestra ventana
window.show()  # Mostramos la ventana (por defecto está oculta)
app.exec()  # Iniciamos el bucle de eventos de la aplicación