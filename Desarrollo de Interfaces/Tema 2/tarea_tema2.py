import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QRadioButton,
    QFormLayout,
    QVBoxLayout,
    QToolBar,
    QStatusBar,
    QMessageBox
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        # ---- TÍTULO Y TAMAÑO ----
        # Establece el título de la ventana principal y un tamaño mínimo adecuado
        self.setWindowTitle("Mini Bloc de Notas")
        self.setMinimumSize(500, 400)

        # ---- DECLARACIÓN DE WIDGETS ----
        # Se definen los widgets que formarán la interfaz
        self.line_edit_titulo = None
        self.combo_categoria = None
        self.radio_prioridad_normal = None
        self.radio_prioridad_alta = None
        self.texto_nota = None

        # ---- ACCIONES ----
        # Declaración de las acciones que serán utilizadas en el menú y la barra de herramientas
        self.accion_limpiar_nota = None
        self.accion_imprimir_nota = None
        self.accion_salir = None
        self.accion_acerca_de = None

        # ---- CONSTRUCCIÓN ----
        # Métodos que configuran la interfaz y las funcionalidades
        self.crear_central()        # Crear la parte central de la ventana (formulario, texto)
        self.crear_acciones()       # Crear las acciones (limpiar, imprimir, etc.)
        self.crear_menus()          # Crear los menús (Archivo, Ayuda)
        self.crear_toolbar()        # Crear la barra de herramientas
        self.crear_statusbar()      # Crear la barra de estado
        self.conectar_senales()     # Conectar las señales y slots

    # =========================
    # CENTRAL
    # =========================
    def crear_central(self):
        # Crear un widget central que contiene los formularios y área de texto
        widget_central = QWidget()

        # ---- Crear widgets ----
        # Campo de texto para el título de la nota (QLineEdit)
        self.line_edit_titulo = QLineEdit()
        self.line_edit_titulo.setPlaceholderText("Título de la nota")  # Placeholder de texto
        self.line_edit_titulo.setMaxLength(60)  # Longitud máxima de caracteres

        # Desplegable para seleccionar la categoría de la nota (QComboBox)
        self.combo_categoria = QComboBox()
        self.combo_categoria.addItems(["Trabajo", "Ideas", "Otros"])

        # Botones de opción (QRadioButton) para seleccionar la prioridad
        self.radio_prioridad_normal = QRadioButton("Normal")
        self.radio_prioridad_alta = QRadioButton("Alta")
        self.radio_prioridad_normal.setChecked(True)  # La prioridad normal está seleccionada por defecto

        # Área de texto para el contenido de la nota (QTextEdit)
          # Placeholder

        # ---- Layouts ----
        # Usamos un QFormLayout para organizar el formulario con campos de título, categoría y prioridad
        layout_form = QFormLayout()
        layout_form.addRow("Título:", self.line_edit_titulo)
        layout_form.addRow("Categoría:", self.combo_categoria)
        layout_form.addRow("Prioridad:", self.radio_prioridad_normal)
        layout_form.addRow("", self.radio_prioridad_alta)

        # Usamos un QVBoxLayout para organizar el formulario y el área de texto
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_form)  # Agregar el formulario al layout principal
        layout_principal.addWidget(self.texto_nota)  # Agregar el área de texto al layout principal

        # Asignamos el layout al widget central
        widget_central.setLayout(layout_principal)

        # Establecer el widget central de la ventana principal
        self.setCentralWidget(widget_central)

    # =========================
    # ACCIONES, MENÚ Y TOOLBAR
    # =========================
    def crear_acciones(self):
        # Definir las acciones que se utilizarán en los menús y la barra de herramientas
        self.accion_limpiar_nota = QAction("Limpiar nota", self)
        self.accion_imprimir_nota = QAction("Imprimir nota", self)
        self.accion_salir = QAction("Salir", self)
        self.accion_acerca_de = QAction("Acerca de…", self)

        # Asignar accesos directos (shortcuts) a algunas acciones
        self.accion_salir.setShortcut("Ctrl+Q")
        self.accion_imprimir_nota.setShortcut("Ctrl+P")
        self.accion_limpiar_nota.setShortcut("Ctrl+L")

    def crear_menus(self):
        # Crear los menús en la barra superior
        barra_menus = self.menuBar()

        # Menú "Archivo" con las opciones: Limpiar, Imprimir, Salir
        menu_archivo = barra_menus.addMenu("Archivo")
        menu_archivo.addAction(self.accion_limpiar_nota)
        menu_archivo.addAction(self.accion_imprimir_nota)
        menu_archivo.addSeparator()  # Separador en el menú
        menu_archivo.addAction(self.accion_salir)

        # Menú "Ayuda" con la opción "Acerca de"
        menu_ayuda = barra_menus.addMenu("Ayuda")
        menu_ayuda.addAction(self.accion_acerca_de)

    def crear_toolbar(self):
        # Crear la barra de herramientas con accesos directos
        toolbar = QToolBar("Herramientas")
        toolbar.addAction(self.accion_limpiar_nota)
        toolbar.addAction(self.accion_imprimir_nota)
        self.addToolBar(toolbar)  # Añadir la barra de herramientas a la ventana

    def crear_statusbar(self):
        # Crear la barra de estado donde se mostrarán mensajes informativos
        barra_estado = QStatusBar()
        self.setStatusBar(barra_estado)
        self.statusBar().showMessage("Listo.")  # Mensaje inicial de la barra de estado

    # =========================
    # SEÑALES
    # =========================
    def conectar_senales(self):
        # Conectar señales a sus slots correspondientes
        self.line_edit_titulo.textChanged.connect(self.slot_titulo_cambiado)
        self.combo_categoria.currentTextChanged.connect(self.slot_categoria_cambiada)

        # Conectar las señales de los botones de prioridad
        self.radio_prioridad_normal.toggled.connect(self.slot_prioridad_cambiada)
        self.radio_prioridad_alta.toggled.connect(self.slot_prioridad_cambiada)

        # Conectar las acciones de los menús y barra de herramientas a los slots
        self.accion_limpiar_nota.triggered.connect(self.slot_limpiar_nota)
        self.accion_imprimir_nota.triggered.connect(self.slot_imprimir_nota)
        self.accion_salir.triggered.connect(self.slot_salir)
        self.accion_acerca_de.triggered.connect(self.slot_acerca_de)

    # =========================
    # UTILIDAD
    # =========================
    def obtener_prioridad_actual(self):
        # Devuelve la prioridad seleccionada (Normal o Alta)
        if self.radio_prioridad_normal.isChecked():
            return "Normal"
        else:
            return "Alta"

    def limpiar_contenido_nota(self):
        # Limpiar todos los campos del formulario
        self.line_edit_titulo.clear()
        self.combo_categoria.setCurrentIndex(0)
        self.radio_prioridad_normal.setChecked(True)
        self.texto_nota.clear()

    def imprimir_en_consola(self):
        # Imprimir el contenido de la nota en la consola
        print("====== NOTA ======")
        print("Título:", self.line_edit_titulo.text())
        print("Categoría:", self.combo_categoria.currentText())
        print("Prioridad:", self.obtener_prioridad_actual())
        print("Contenido:")
        print(self.texto_nota.toPlainText())
        print("===================")

    # =========================
    # SLOTS
    # =========================
    def slot_limpiar_nota(self):
        # Confirmación antes de limpiar la nota
        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            "¿Deseas limpiar la nota?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            self.limpiar_contenido_nota()
            self.statusBar().showMessage("Nota limpiada.")  # Mostrar mensaje en la barra de estado

    def slot_imprimir_nota(self):
        # Imprimir la nota en la consola
        self.imprimir_en_consola()
        self.statusBar().showMessage("Nota impresa en consola.")  # Mensaje de éxito

    def slot_salir(self):
        # Confirmación antes de salir de la aplicación
        respuesta = QMessageBox.question(
            self,
            "Salir",
            "¿Deseas cerrar la aplicación?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            self.close()

    def slot_acerca_de(self):
        # Mostrar información acerca de la aplicación
        QMessageBox.information
