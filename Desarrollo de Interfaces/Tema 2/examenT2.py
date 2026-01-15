# José Carlos Mora 2º DAM
# Aplicación de Encuesta de Satisfacción - Proyecto Integrador

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QVBoxLayout, 
                               QHBoxLayout, QLineEdit, QPushButton, QLabel, 
                               QMessageBox, QTabWidget, QWidget, QFormLayout,
                               QComboBox, QSlider, QCheckBox, QTextEdit,
                               QToolBar, QDockWidget, QDialogButtonBox)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt


# ===================================================================
#                            LOGIN
# ===================================================================
class DialogoLogin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Iniciar sesión")
        
        layout = QVBoxLayout()
        
        # Etiqueta de bienvenida
        etiqueta_bienvenida = QLabel("Bienvenido al sistema de encuestas")
        etiqueta_bienvenida.setAlignment(Qt.AlignCenter)
        fuente = etiqueta_bienvenida.font()
        fuente.setPointSize(14)
        etiqueta_bienvenida.setFont(fuente)
        layout.addWidget(etiqueta_bienvenida)
        
        # Campo usuario
        self.campo_usuario = QLineEdit()
        self.campo_usuario.setPlaceholderText("Usuario")
        layout.addWidget(QLabel("Usuario:"))
        layout.addWidget(self.campo_usuario)
        
        # Campo contraseña
        self.campo_password = QLineEdit()
        self.campo_password.setPlaceholderText("Contraseña")
        self.campo_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(QLabel("Contraseña:"))
        layout.addWidget(self.campo_password)
        
        # Botones
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.validar)
        botones.rejected.connect(self.reject)
        layout.addWidget(botones)
        
        self.setLayout(layout)
    
    def validar(self):
        usuario = self.campo_usuario.text()
        password = self.campo_password.text()
        
        if usuario == "admin" and password == "admin":
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")


# ===================================================================
#                        VENTANA PRINCIPAL
# ===================================================================
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Encuesta de satisfacción")
        self.setMinimumSize(800, 600)
        
        # Variables necesarias
        self.usuario_logueado = None
        
        self.crear_central()
        self.crear_acciones()
        self.crear_menus()
        self.crear_toolbar()
        self.crear_statusbar()
        self.crear_dock_notas()
        self.conectar_senales()

    # ---------------------------------------------------------------
    def crear_central(self):
        # Crear widget de pestañas
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # ===== PESTAÑA 1: Datos Personales =====
        tab1 = QWidget()
        layout_tab1 = QFormLayout()
        tab1.setLayout(layout_tab1)
        
        self.line_nombre = QLineEdit()
        self.line_nombre.setPlaceholderText("Escribe tu nombre completo")
        
        self.line_email = QLineEdit()
        self.line_email.setPlaceholderText("tu@email.com")
        
        self.combo_edad = QComboBox()
        self.combo_edad.addItems(["18-25", "26-35", "36-45", "46-55", "56+"])
        
        layout_tab1.addRow("Nombre:", self.line_nombre)
        layout_tab1.addRow("Email:", self.line_email)
        layout_tab1.addRow("Rango de edad:", self.combo_edad)
        
        self.tabs.addTab(tab1, "Datos Personales")
        
        # ===== PESTAÑA 2: Encuesta =====
        tab2 = QWidget()
        layout_tab2 = QFormLayout()
        tab2.setLayout(layout_tab2)
        
        self.combo_compania = QComboBox()
        self.combo_compania.addItems(["Selecciona una compañía...", "Empresa A", 
                                      "Empresa B", "Empresa C", "Otra"])
        self.combo_compania.setEditable(True)
        
        # Slider de satisfacción
        layout_satisfaccion = QVBoxLayout()
        self.slider_satisfaccion = QSlider(Qt.Horizontal)
        self.slider_satisfaccion.setMinimum(1)
        self.slider_satisfaccion.setMaximum(10)
        self.slider_satisfaccion.setValue(5)
        self.slider_satisfaccion.setTickPosition(QSlider.TicksBelow)
        self.slider_satisfaccion.setTickInterval(1)
        
        self.label_satisfaccion = QLabel("Nivel: 5")
        layout_satisfaccion.addWidget(self.slider_satisfaccion)
        layout_satisfaccion.addWidget(self.label_satisfaccion)
        
        self.check_recomienda = QCheckBox("Sí, recomendaría el servicio")
        
        self.text_comentarios = QTextEdit()
        self.text_comentarios.setPlaceholderText("Escribe tus comentarios aquí...")
        self.text_comentarios.setMaximumHeight(100)
        
        layout_tab2.addRow("Compañía:", self.combo_compania)
        layout_tab2.addRow("Satisfacción (1-10):", layout_satisfaccion)
        layout_tab2.addRow("¿Recomendarías?:", self.check_recomienda)
        layout_tab2.addRow("Comentarios:", self.text_comentarios)
        
        self.tabs.addTab(tab2, "Encuesta")
        
        # ===== PESTAÑA 3: Resumen =====
        tab3 = QWidget()
        layout_tab3 = QVBoxLayout()
        tab3.setLayout(layout_tab3)
        
        self.label_resumen = QLabel("Completa la encuesta para ver el resumen")
        self.label_resumen.setAlignment(Qt.AlignCenter)
        self.label_resumen.setWordWrap(True)
        fuente = self.label_resumen.font()
        fuente.setPointSize(12)
        self.label_resumen.setFont(fuente)
        
        layout_tab3.addWidget(self.label_resumen)
        
        boton_ver_resumen = QPushButton("Generar resumen")
        boton_ver_resumen.clicked.connect(self.slot_ver_resumen)
        layout_tab3.addWidget(boton_ver_resumen)
        layout_tab3.addStretch()
        
        self.tabs.addTab(tab3, "Resumen")

    # ---------------------------------------------------------------
    def crear_dock_notas(self):
        # Crear dock inferior con área de texto
        self.dock_notas = QDockWidget("Notas del evaluador", self)
        
        self.text_notas = QTextEdit()
        self.text_notas.setPlaceholderText("Escribe notas adicionales sobre la encuesta...")
        
        self.dock_notas.setWidget(self.text_notas)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock_notas)

    # ---------------------------------------------------------------
    def crear_acciones(self):
        # Acción Login
        self.accion_login = QAction("Iniciar sesión", self)
        self.accion_login.setShortcut("Ctrl+L")
        self.accion_login.triggered.connect(self.slot_login)
        
        # Acción Nueva Encuesta
        self.accion_nueva = QAction("Nueva encuesta", self)
        self.accion_nueva.setShortcut("Ctrl+N")
        self.accion_nueva.triggered.connect(self.slot_nueva_encuesta)
        
        # Acción Ver Resumen
        self.accion_resumen = QAction("Ver resumen", self)
        self.accion_resumen.setShortcut("Ctrl+R")
        self.accion_resumen.triggered.connect(self.slot_ver_resumen)
        
        # Acción Salir
        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut("Ctrl+Q")
        self.accion_salir.triggered.connect(self.slot_salir)
        
        # Acción Acerca de
        self.accion_acerca = QAction("Acerca de", self)
        self.accion_acerca.triggered.connect(self.slot_acerca_de)

    # ---------------------------------------------------------------
    def crear_menus(self):
        barra_menu = self.menuBar()
        
        # Menú Archivo
        menu_archivo = barra_menu.addMenu("&Archivo")
        menu_archivo.addAction(self.accion_login)
        menu_archivo.addSeparator()
        menu_archivo.addAction(self.accion_nueva)
        menu_archivo.addAction(self.accion_resumen)
        menu_archivo.addSeparator()
        menu_archivo.addAction(self.accion_salir)
        
        # Menú Ayuda
        menu_ayuda = barra_menu.addMenu("&Ayuda")
        menu_ayuda.addAction(self.accion_acerca)

    # ---------------------------------------------------------------
    def crear_toolbar(self):
        toolbar = QToolBar("Barra principal")
        toolbar.addAction(self.accion_login)
        toolbar.addAction(self.accion_nueva)
        toolbar.addAction(self.accion_resumen)
        toolbar.addSeparator()
        toolbar.addAction(self.accion_salir)
        self.addToolBar(toolbar)

    # ---------------------------------------------------------------
    def crear_statusbar(self):
        self.barra_estado = self.statusBar()
        self.barra_estado.showMessage("Bienvenido. Inicia sesión para comenzar.", 5000)

    # ---------------------------------------------------------------
    def conectar_senales(self):
        # Conectar señales de los widgets
        self.line_nombre.textChanged.connect(self.slot_nombre_cambiado)
        self.combo_compania.currentTextChanged.connect(self.slot_compania_cambiada)
        self.slider_satisfaccion.valueChanged.connect(self.slot_satisfaccion_cambiada)
        self.check_recomienda.stateChanged.connect(self.slot_recomienda_cambiado)

    # ---------------------------------------------------------------
    def slot_login(self):
        dialogo = DialogoLogin(self)
        
        if dialogo.exec() == QDialog.Accepted:
            self.usuario_logueado = dialogo.campo_usuario.text()
            QMessageBox.information(
                self,
                "Login exitoso",
                f"Bienvenido/a {self.usuario_logueado}"
            )
            self.barra_estado.showMessage(f"Usuario: {self.usuario_logueado}", 0)

    # ---------------------------------------------------------------
    def slot_nueva_encuesta(self):
        # Confirmar antes de limpiar
        respuesta = QMessageBox.question(
            self,
            "Nueva encuesta",
            "¿Estás seguro de que quieres iniciar una nueva encuesta?\nSe perderán los datos actuales.",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            # Limpiar todos los campos
            self.line_nombre.clear()
            self.line_email.clear()
            self.combo_edad.setCurrentIndex(0)
            self.combo_compania.setCurrentIndex(0)
            self.slider_satisfaccion.setValue(5)
            self.check_recomienda.setChecked(False)
            self.text_comentarios.clear()
            self.text_notas.clear()
            self.label_resumen.setText("Completa la encuesta para ver el resumen")
            
            # Volver a la primera pestaña
            self.tabs.setCurrentIndex(0)
            
            self.barra_estado.showMessage("Nueva encuesta iniciada", 3000)

    # ---------------------------------------------------------------
    def slot_ver_resumen(self):
        # Generar resumen de la encuesta
        nombre = self.line_nombre.text() or "No especificado"
        email = self.line_email.text() or "No especificado"
        edad = self.combo_edad.currentText()
        compania = self.combo_compania.currentText()
        satisfaccion = self.slider_satisfaccion.value()
        recomienda = "Sí" if self.check_recomienda.isChecked() else "No"
        comentarios = self.text_comentarios.toPlainText() or "Sin comentarios"
        
        resumen = f"""
        ===== RESUMEN DE LA ENCUESTA =====
        
        DATOS PERSONALES:
        • Nombre: {nombre}
        • Email: {email}
        • Edad: {edad}
        
        EVALUACIÓN:
        • Compañía: {compania}
        • Satisfacción: {satisfaccion}/10
        • Recomendaría: {recomienda}
        
        COMENTARIOS:
        {comentarios}
        
        ================================
        """
        
        self.label_resumen.setText(resumen)
        self.tabs.setCurrentIndex(2)  # Ir a la pestaña de resumen
        
        # Mostrar también un MessageBox
        QMessageBox.information(
            self,
            "Resumen generado",
            "El resumen de la encuesta se ha generado correctamente.\nRevísalo en la pestaña 'Resumen'."
        )
        
        self.barra_estado.showMessage("Resumen generado correctamente", 3000)

    # ---------------------------------------------------------------
    def slot_salir(self):
        respuesta = QMessageBox.question(
            self,
            "Salir",
            "¿Estás seguro de que quieres salir de la aplicación?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            self.close()

    # ---------------------------------------------------------------
    def slot_acerca_de(self):
        QMessageBox.information(
            self,
            "Acerca de",
            "Sistema de Encuestas de Satisfacción\n\n"
            "Versión 1.0\n"
            "Desarrollado con PySide6\n\n"
            "Esta aplicación permite recopilar y gestionar\n"
            "encuestas de satisfacción de clientes."
        )

    # ---------------------------------------------------------------
    def slot_compania_cambiada(self, nueva):
        if nueva and nueva != "Selecciona una compañía...":
            self.barra_estado.showMessage(f"Compañía seleccionada: {nueva}", 2000)

    # ---------------------------------------------------------------
    def slot_satisfaccion_cambiada(self, nueva):
        self.label_satisfaccion.setText(f"Nivel: {nueva}")
        self.barra_estado.showMessage(f"Nivel de satisfacción: {nueva}/10", 2000)

    # ---------------------------------------------------------------
    def slot_recomienda_cambiado(self, estado):
        if estado == Qt.Checked:
            self.barra_estado.showMessage("Marcado: Recomendaría el servicio", 2000)
        else:
            self.barra_estado.showMessage("Desmarcado: No recomendaría el servicio", 2000)

    # ---------------------------------------------------------------
    def slot_nombre_cambiado(self, nuevo_nombre):
        if nuevo_nombre:
            self.setWindowTitle(f"Encuesta de satisfacción - {nuevo_nombre}")
        else:
            self.setWindowTitle("Encuesta de satisfacción")


# ===================================================================
#                       EJECUCIÓN DE LA APP
# ===================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()