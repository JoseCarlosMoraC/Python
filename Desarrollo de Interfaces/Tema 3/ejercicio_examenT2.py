# encuesta_app.py
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QRadioButton,
    QGroupBox, QFormLayout, QCheckBox, QSlider, QTextEdit, QAction,
    QTabWidget, QDockWidget, QMessageBox, QToolBar, QStatusBar
)
from PySide6.QtCore import Qt  # Constantes y señales de Qt


# =====================================================
# DIALOGO DE LOGIN (VENTANA EMERGENTE PARA USUARIO)
# =====================================================
class DialogoLogin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Iniciar sesión")  # Título de la ventana

        # Etiquetas y cajas de texto para usuario y contraseña
        self.lbl_usuario = QLabel("Usuario:")
        self.txt_usuario = QLineEdit()

        self.lbl_pass = QLabel("Contraseña:")
        self.txt_pass = QLineEdit()
        self.txt_pass.setEchoMode(QLineEdit.EchoMode.Password)  # Oculta la contraseña

        # Botones Aceptar y Cancelar
        self.btn_ok = QPushButton("Aceptar")
        self.btn_cancel = QPushButton("Cancelar")

        # Conectar botones a funciones
        self.btn_ok.clicked.connect(self.validar)  # Validar usuario
        self.btn_cancel.clicked.connect(self.reject)  # Cierra el diálogo

        # Layout horizontal para botones
        h = QHBoxLayout()
        h.addStretch()  # Espacio flexible
        h.addWidget(self.btn_ok)
        h.addWidget(self.btn_cancel)

        # Layout vertical principal
        v = QVBoxLayout()
        v.addWidget(self.lbl_usuario)
        v.addWidget(self.txt_usuario)
        v.addWidget(self.lbl_pass)
        v.addWidget(self.txt_pass)
        v.addLayout(h)

        self.setLayout(v)

    # Función para validar que se escriba un usuario
    def validar(self):
        usuario = self.txt_usuario.text().strip()
        if usuario == "":
            QMessageBox.warning(self, "Error", "Debes escribir un usuario")
            return
        self.accept()  # Cierra el diálogo con éxito

    # Devuelve el usuario ingresado
    def obtener_usuario(self):
        return self.txt_usuario.text()


# =====================================================
# VENTANA PRINCIPAL DE LA APLICACIÓN
# =====================================================
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Encuesta de satisfacción")
        self.setMinimumSize(800, 600)

        # Variables para almacenar información de la encuesta
        self.usuario_actual = "Invitado"
        self.nombre_encuestado = ""
        self.compania = ""
        self.satisfaccion = 5
        self.recomienda = False
        self.notas = ""

        # Crear la interfaz
        self.crear_central()
        self.crear_dock_notas()
        self.crear_acciones()
        self.crear_menus()
        self.crear_toolbar()
        self.crear_statusbar()
        self.conectar_senales()

        self.slot_login()  # Mostrar diálogo de login al iniciar

    # -------------------------------------------------------------
    # Crear área central con pestañas
    def crear_central(self):
        self.tabs = QTabWidget()

        # Pestaña de encuesta
        self.tab_encuesta = QWidget()
        self.crear_formulario()

        # Pestaña de información/instrucciones
        self.tab_info = QWidget()
        vinfo = QVBoxLayout()
        lbl = QLabel("Instrucciones:\n\nRellena el formulario.")
        lbl.setWordWrap(True)
        vinfo.addWidget(lbl)
        vinfo.addStretch()
        self.tab_info.setLayout(vinfo)

        # Añadir pestañas
        self.tabs.addTab(self.tab_encuesta, "Encuesta")
        self.tabs.addTab(self.tab_info, "Información")

        self.setCentralWidget(self.tabs)

    # -------------------------------------------------------------
    # Crear formulario de la encuesta
    def crear_formulario(self):
        layout = QVBoxLayout()

        # Formulario con nombre y compañía
        form = QFormLayout()
        self.txt_nombre = QLineEdit()
        form.addRow("Nombre:", self.txt_nombre)

        self.cmb_compania = QComboBox()
        self.cmb_compania.addItems(["Seleccione...", "Empresa A", "Empresa B", "Empresa C"])
        form.addRow("Compañía:", self.cmb_compania)

        # Grupo para el slider de satisfacción
        grupo = QGroupBox("Nivel satisfacción")
        v = QVBoxLayout()
        self.sld_satisfaccion = QSlider(Qt.Horizontal)
        self.sld_satisfaccion.setRange(0, 10)
        self.sld_satisfaccion.setValue(5)
        self.lbl_sat = QLabel("5")
        v.addWidget(self.sld_satisfaccion)
        v.addWidget(self.lbl_sat)
        grupo.setLayout(v)

        # Checkbox de recomendación
        self.chk_recomienda = QCheckBox("¿Recomendaría?")

        # Botones para nueva encuesta y ver resumen
        hbot = QHBoxLayout()
        self.btn_nueva = QPushButton("Nueva encuesta")
        self.btn_resumen = QPushButton("Ver resumen")
        hbot.addWidget(self.btn_nueva)
        hbot.addWidget(self.btn_resumen)
        hbot.addStretch()

        # Layout final de la pestaña
        layout.addLayout(form)
        layout.addWidget(grupo)
        layout.addWidget(self.chk_recomienda)
        layout.addLayout(hbot)
        layout.addStretch()

        self.tab_encuesta.setLayout(layout)

    # -------------------------------------------------------------
    # Crear panel inferior para notas adicionales
    def crear_dock_notas(self):
        self.dock = QDockWidget("Notas", self)
        self.txt_notas = QTextEdit()
        self.txt_notas.setPlaceholderText("Notas adicionales...")
        self.dock.setWidget(self.txt_notas)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock)

    # -------------------------------------------------------------
    # Crear acciones del menú y barra de herramientas
    def crear_acciones(self):
        self.act_login = QAction("Iniciar sesión", self)
        self.act_nueva = QAction("Nueva encuesta", self)
        self.act_resumen = QAction("Ver resumen", self)
        self.act_salir = QAction("Salir", self)
        self.act_acerca = QAction("Acerca de", self)

    # -------------------------------------------------------------
    # Crear menús de la ventana
    def crear_menus(self):
        bar = self.menuBar()

        m1 = bar.addMenu("Archivo")
        m1.addAction(self.act_login)
        m1.addSeparator()
        m1.addAction(self.act_nueva)
        m1.addAction(self.act_resumen)
        m1.addSeparator()
        m1.addAction(self.act_salir)

        m2 = bar.addMenu("Ayuda")
        m2.addAction(self.act_acerca)

    # -------------------------------------------------------------
    # Crear barra de herramientas
    def crear_toolbar(self):
        tb = QToolBar("Barra principal")
        tb.setMovable(False)
        tb.addAction(self.act_login)
        tb.addAction(self.act_nueva)
        tb.addAction(self.act_resumen)
        self.addToolBar(tb)

    # -------------------------------------------------------------
    # Crear barra de estado inferior
    def crear_statusbar(self):
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Listo")  # Mensaje inicial

    # -------------------------------------------------------------
    # Conectar señales de widgets a funciones (slots)
    def conectar_senales(self):
        self.act_login.triggered.connect(self.slot_login)
        self.act_nueva.triggered.connect(self.slot_nueva_encuesta)
        self.act_resumen.triggered.connect(self.slot_ver_resumen)
        self.act_salir.triggered.connect(self.slot_salir)
        self.act_acerca.triggered.connect(self.slot_acerca_de)

        self.cmb_compania.currentTextChanged.connect(self.slot_compania_cambiada)
        self.sld_satisfaccion.valueChanged.connect(self.slot_satisfaccion_cambiada)
        self.chk_recomienda.clicked.connect(self.slot_recomienda_cambiado)
        self.txt_nombre.textChanged.connect(self.slot_nombre_cambiado)
        self.txt_notas.textChanged.connect(self._guardar_notas)

        self.btn_nueva.clicked.connect(self.slot_nueva_encuesta)
        self.btn_resumen.clicked.connect(self.slot_ver_resumen)

    # --------------------------- SLOTS -------------------------------
    # Mostrar diálogo de login
    def slot_login(self):
        dlg = DialogoLogin(self)
        if dlg.exec():
            self.usuario_actual = dlg.obtener_usuario()
            self.status.showMessage("Usuario: " + self.usuario_actual)
            self.setWindowTitle("Encuesta de satisfacción - Usuario: " + self.usuario_actual)

    # Limpiar el formulario para una nueva encuesta
    def slot_nueva_encuesta(self):
        r = QMessageBox.question(
            self,
            "Confirmar",
            "¿Desea limpiar el formulario?"
        )
        if r == QMessageBox.Yes:
            self.txt_nombre.clear()
            self.cmb_compania.setCurrentIndex(0)
            self.sld_satisfaccion.setValue(5)
            self.chk_recomienda.setChecked(False)
            self.txt_notas.clear()
            self.status.showMessage("Formulario reiniciado")

    # Mostrar un resumen de la encuesta en un mensaje
    def slot_ver_resumen(self):
        nombre = self.txt_nombre.text()
        comp = self.cmb_compania.currentText()
        sat = str(self.sld_satisfaccion.value())
        rec = "Sí" if self.chk_recomienda.isChecked() else "No"
        notas = self.txt_notas.toPlainText()

        resumen = (
            "Resumen de encuesta:\n\n" +
            "Nombre: " + nombre + "\n" +
            "Compañía: " + comp + "\n" +
            "Satisfacción: " + sat + "\n" +
            "Recomienda: " + rec + "\n\n" +
            "Notas:\n" + notas
        )

        QMessageBox.information(self, "Resumen", resumen)

    # Salir de la aplicación
    def slot_salir(self):
        r = QMessageBox.question(self, "Salir", "¿Seguro que desea salir?")
        if r == QMessageBox.Yes:
            QApplication.quit()

    # Mostrar información de la aplicación
    def slot_acerca_de(self):
        QMessageBox.information(
            self,
            "Acerca de",
            "Aplicación de Encuesta\nCreada sin f-strings."
        )

    # Actualizar compañía seleccionada
    def slot_compania_cambiada(self, texto):
        self.compania = texto
        self.status.showMessage("Compañía: " + texto)

    # Actualizar nivel de satisfacción
    def slot_satisfaccion_cambiada(self, valor):
        self.satisfaccion = valor
        self.lbl_sat.setText(str(valor))
        self.status.showMessage("Satisfacción: " + str(valor))

    # Actualizar si recomienda
    def slot_recomienda_cambiado(self, checked):
        self.recomienda = checked
        texto = "Sí" if checked else "No"
        self.status.showMessage("Recomienda: " + texto)

    # Actualizar nombre del encuestado y título de la ventana
    def slot_nombre_cambiado(self, nuevo):
        self.nombre_encuestado = nuevo
        if nuevo.strip() == "":
            self.setWindowTitle("Encuesta de satisfacción - Usuario: " + self.usuario_actual)
        else:
            self.setWindowTitle("Encuesta de satisfacción - " + nuevo + " (" + self.usuario_actual + ")")

    # Guardar notas ingresadas
    def _guardar_notas(self):
        self.notas = self.txt_notas.toPlainText()


# =====================================================
# EJECUCIÓN DE LA APLICACIÓN
# =====================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Estilo CSS para la aplicación
    estilo = """
    QWidget { background-color: #f4f4f4; }
    QLineEdit, QComboBox, QTextEdit {
        background:white; border:1px solid gray; padding:4px;
    }
    QPushButton {
        background-color:#0077cc; color:white; border-radius:4px; padding:6px;
    }
    QPushButton:hover {
        background-color:#005fa3;
    }
    """
    app.setStyleSheet(estilo)

    # Crear y mostrar la ventana principal
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
