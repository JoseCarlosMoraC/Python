# Proyecto 5 - Panel multipantalla con QStackedLayout y diálogos de personalización
# José Carlos Mora 2º DAM

# IMPORTACIONES
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                               QVBoxLayout, QStackedLayout, QLabel, QLineEdit,
                               QPushButton, QToolBar, QColorDialog, QFontDialog)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # CONFIGURACIÓN INICIAL
        self.setWindowTitle("Panel multipantalla")

        # CREAR LAYOUT PRINCIPAL HORIZONTAL
        # Usamos QHBoxLayout porque queremos la pila de pantallas a la izquierda
        # y los botones de navegación a la derecha
        layout_principal = QHBoxLayout()

        # CREAR QSTACKEDLAYOUT (PILA DE PANTALLAS)
        # QStackedLayout permite tener múltiples widgets apilados
        # pero solo uno visible a la vez (como pestañas pero sin la barra de pestañas)
        self.pila = QStackedLayout()

        # PANTALLA 1: Un simple QLabel
        self.pantalla1 = QLabel("Pantalla 1")
        # Alineamos el texto al centro
        self.pantalla1.setAlignment(Qt.AlignCenter)
        # Configuramos el tamaño de fuente
        fuente = self.pantalla1.font()
        fuente.setPointSize(24)
        self.pantalla1.setFont(fuente)
        # addWidget() añade un widget a la pila (índice 0)
        self.pila.addWidget(self.pantalla1)

        # PANTALLA 2: Otro QLabel similar
        self.pantalla2 = QLabel("Pantalla 2")
        self.pantalla2.setAlignment(Qt.AlignCenter)
        self.pantalla2.setFont(fuente)
        # Se añade con índice 1
        self.pila.addWidget(self.pantalla2)

        # PANTALLA 3: Más compleja, con QLineEdit y QLabel conectados
        contenedor_p3 = QWidget()
        layout_p3 = QVBoxLayout()
        contenedor_p3.setLayout(layout_p3)

        # Campo de texto
        self.line_p3 = QLineEdit()
        self.line_p3.setPlaceholderText("Escribe algo...")

        # Etiqueta que mostrará el texto
        self.label_p3 = QLabel("")
        self.label_p3.setAlignment(Qt.AlignCenter)

        # CONEXIÓN DIRECTA entre widgets
        # textChanged del QLineEdit emite el nuevo texto como parámetro
        # setText del QLabel acepta un texto como parámetro
        # Al conectarlos directamente, el texto se pasa automáticamente
        # Esto es muy útil para actualizaciones en tiempo real
        self.line_p3.textChanged.connect(self.label_p3.setText)

        # Añadir widgets al layout de la pantalla 3
        layout_p3.addWidget(self.line_p3)
        layout_p3.addWidget(self.label_p3)

        # Añadir el contenedor completo a la pila (índice 2)
        self.pila.addWidget(contenedor_p3)

        # CREAR LAYOUT LATERAL CON BOTONES DE NAVEGACIÓN
        layout_botones = QVBoxLayout()

        # Botón para ver pantalla 1
        boton1 = QPushButton("Ver pantalla 1")
        boton1.clicked.connect(self.mostrar_pantalla1)
        layout_botones.addWidget(boton1)

        # Botón para ver pantalla 2
        boton2 = QPushButton("Ver pantalla 2")
        boton2.clicked.connect(self.mostrar_pantalla2)
        layout_botones.addWidget(boton2)

        # Botón para ver pantalla 3
        boton3 = QPushButton("Ver pantalla 3")
        boton3.clicked.connect(self.mostrar_pantalla3)
        layout_botones.addWidget(boton3)

        # addStretch() añade espacio flexible que empuja los botones hacia arriba
        layout_botones.addStretch()

        # AÑADIR LAYOUTS AL PRINCIPAL
        # Primero la pila (ocupará más espacio)
        layout_principal.addLayout(self.pila)
        # Luego los botones a la derecha
        layout_principal.addLayout(layout_botones)

        # CREAR CONTENEDOR Y ESTABLECER COMO CENTRAL WIDGET
        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        # CREAR MENÚ VER
        barra_menu = self.menuBar()
        menu_ver = barra_menu.addMenu("&Ver")

        # Crear acciones para cada pantalla
        self.accion_p1 = QAction("Pantalla 1", self)
        self.accion_p1.triggered.connect(self.mostrar_pantalla1)
        menu_ver.addAction(self.accion_p1)

        self.accion_p2 = QAction("Pantalla 2", self)
        self.accion_p2.triggered.connect(self.mostrar_pantalla2)
        menu_ver.addAction(self.accion_p2)

        self.accion_p3 = QAction("Pantalla 3", self)
        self.accion_p3.triggered.connect(self.mostrar_pantalla3)
        menu_ver.addAction(self.accion_p3)

        # CREAR MENÚ FORMATO
        menu_formato = barra_menu.addMenu("&Formato")

        # Acción para cambiar color
        self.accion_color = QAction("Cambiar color del texto", self)
        self.accion_color.triggered.connect(self.cambiar_color)
        menu_formato.addAction(self.accion_color)

        # Acción para cambiar fuente
        self.accion_fuente = QAction("Cambiar fuente del texto", self)
        self.accion_fuente.triggered.connect(self.cambiar_fuente)
        menu_formato.addAction(self.accion_fuente)

        # CREAR BARRA DE HERRAMIENTAS
        barra_herramientas = QToolBar("Barra principal")
        barra_herramientas.addAction(self.accion_p1)
        barra_herramientas.addAction(self.accion_p2)
        barra_herramientas.addAction(self.accion_p3)
        self.addToolBar(barra_herramientas)

        # CREAR BARRA DE ESTADO
        self.barra_estado = self.statusBar()
        self.barra_estado.showMessage("Pantalla 1 activa")

    # MÉTODO PARA CAMBIAR DE PANTALLA 1
    def mostrar_pantalla1(self):
        self.cambiar_pantalla(0)

    # MÉTODO PARA CAMBIAR DE PANTALLA 2
    def mostrar_pantalla2(self):
        self.cambiar_pantalla(1)

    # MÉTODO PARA CAMBIAR DE PANTALLA 3
    def mostrar_pantalla3(self):
        self.cambiar_pantalla(2)

    # MÉTODO PARA CAMBIAR DE PANTALLA
    def cambiar_pantalla(self, indice):
        # setCurrentIndex cambia qué widget de la pila está visible
        # Los índices empiezan en 0
        self.pila.setCurrentIndex(indice)

        # Actualizamos la barra de estado
        mensaje = "Pantalla " + str(indice + 1) + " activa"
        self.barra_estado.showMessage(mensaje, 2000)

    # MÉTODO PARA CAMBIAR COLOR DEL TEXTO
    def cambiar_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            estilo = "color: " + color.name() + ";"
            self.label_p3.setStyleSheet(estilo)
            self.barra_estado.showMessage("Color actualizado", 2000)

    # MÉTODO PARA CAMBIAR FUENTE
    def cambiar_fuente(self):
        fuente, ok = QFontDialog.getFont()
        if ok:
            self.label_p3.setFont(fuente)
            self.barra_estado.showMessage("Fuente actualizada", 2000)

# EJECUCIÓN
app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()