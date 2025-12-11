

# Importamos los widgets y clases necesarios desde PySide6.
# QApplication → Necesaria para iniciar la aplicación Qt.
# QMainWindow → Ventana principal con barra de estado, menú, etc.
# QWidget → Contenedor básico de widgets.
# QVBoxLayout → Layout vertical para organizar widgets uno debajo de otro.
# QLabel → Etiquetas de texto.
# QCheckBox → Casilla de verificación.
# QPushButton → Botón simple.
# QLineEdit → Campo de texto de una línea.
# QRadioButton → Botones de selección exclusiva.
# QComboBox → Desplegable de opciones.
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QCheckBox, QPushButton, QLineEdit, QRadioButton, QComboBox
)
import sys
import os



class MainWindow(QMainWindow):
    def __init__(self):
        # Llamamos al constructor de la clase padre (QMainWindow)
        super().__init__()

        # Título de la ventana principal
        self.setWindowTitle("Ventana principal")

        # -----------------------------
        # CREACIÓN DEL CONTENEDOR Y LAYOUT PRINCIPAL
        # -----------------------------

        # QWidget será el contenedor central de los widgets
        contenedor = QWidget()

        # Layout vertical para colocar los widgets de arriba a abajo
        layout = QVBoxLayout()

        # Espaciado entre widgets (en píxeles)
        layout.setSpacing(18)

        # -----------------------------
        # TÍTULO Y TEXTOS INFORMATIVOS
        # -----------------------------

        # Título principal del formulario
        titulo = QLabel("Fútbol")
        layout.addWidget(titulo)

        # Texto introductorio del cuestionario
        layout.addWidget(QLabel("Pequeño cuestionario sobre fútbol:"))

        # -----------------------------
        # CHECKBOX (casilla de verificación)
        # -----------------------------

        # Creamos un checkbox para aceptar términos
        self.checkbox = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.checkbox)

        # -----------------------------
        # PREGUNTA CON BOTÓN
        # -----------------------------

        layout.addWidget(QLabel("¿Te gusta el fútbol?"))

        # Botón para "Confirmar"
        # (Aquí podría conectarse a una función con .clicked.connect)
        self.boton = QPushButton("Confirmar")
        layout.addWidget(self.boton)

        # -----------------------------
        # LINEEDIT (campo de texto)
        # -----------------------------

        layout.addWidget(QLabel("¿Cuál ha sido la máxima categoría en la que ha estado CD Gerena?"))

        # QLineEdit → Entrada de texto de una sola línea
        self.line = QLineEdit()

        # Texto que aparece en gris cuando está vacío
        self.line.setPlaceholderText("Escribelo aquí")
        layout.addWidget(self.line)

        # -----------------------------
        # RADIOBUTTONS (elección exclusiva)
        # -----------------------------

        layout.addWidget(QLabel("Mejor equipo del mundo"))

        # Tres opciones. Los QRadioButton del mismo layout se excluyen entre sí.
        self.radio1 = QRadioButton("Real Madrid")
        self.radio2 = QRadioButton("FC Barcelona")
        self.radio3 = QRadioButton("CDM Gerena")

        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)

        # -----------------------------
        # COMBOBOX (lista desplegable)
        # -----------------------------

        layout.addWidget(QLabel("Mejor entrenador del mundo"))

        # Desplegable con tres opciones (en tu caso repetidas)
        self.combo = QComboBox()
        self.combo.addItems(["JC Mora", "JC Mora", "JC Mora"])
        layout.addWidget(self.combo)

        # -----------------------------
        # APLICAR EL LAYOUT Y MOSTRAR LA VENTANA
        # -----------------------------

        # Aplicamos el layout al contenedor
        contenedor.setLayout(layout)

        # Establecemos el contenedor como widget central del QMainWindow
        self.setCentralWidget(contenedor)



# --------------------------------------------------
# FUNCIÓN PARA CARGAR ESTILOS DESDE UN ARCHIVO QSS
# --------------------------------------------------

def cargar_estilos(app, archivo_qss):
    """
    Carga los estilos visuales desde un archivo .qss
    y los aplica a toda la aplicación.

    - app: el QApplication que controla toda la interfaz.
    - archivo_qss: nombre del archivo de estilos.
    """

    # Obtenemos la ruta absoluta del directorio donde está este script
    ruta_script = os.path.abspath(os.path.dirname(__file__))

    # Construimos la ruta completa al archivo .qss
    ruta_qss = os.path.join(ruta_script, archivo_qss)

    # Abrimos el .qss y lo aplicamos como StyleSheet
    with open(ruta_qss, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        app.setStyleSheet(contenido)



# --------------------------------------------------
# BLOQUE PRINCIPAL DE EJECUCIÓN
# --------------------------------------------------

if __name__ == "__main__":
    # QApplication → Obligatorio antes de crear cualquier ventana
    app = QApplication(sys.argv)

    # Cargamos los estilos visuales del archivo QSS
    cargar_estilos(app, "Mora_JC_estilos_T3.1.qss")

    # Creamos y mostramos la ventana principal
    ventana = MainWindow()
    ventana.show()

    # Ejecutamos el loop principal de Qt
    sys.exit(app.exec())