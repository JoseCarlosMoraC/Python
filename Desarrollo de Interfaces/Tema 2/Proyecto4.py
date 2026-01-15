# Proyecto 4 - Formulario de preferencias con QFormLayout y diálogo personalizado
# José Carlos Mora 2º DAM

# IMPORTACIONES
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFormLayout,
                               QLineEdit, QComboBox, QCheckBox, QMessageBox,
                               QToolBar, QDialog, QLabel, QVBoxLayout, QDialogButtonBox)
from PySide6.QtGui import QAction

# CLASE PARA EL DIÁLOGO PERSONALIZADO
# Heredamos de QDialog para crear nuestro propio cuadro de diálogo
class DialogoConfirmacion(QDialog):
    def __init__(self, parent=None):
        # parent=None permite que el diálogo sea independiente o tenga padre
        super().__init__(parent)
        
        # Configuración del diálogo
        self.setWindowTitle("Confirmar cambios")
        
        # Layout vertical para organizar los elementos
        layout = QVBoxLayout()
        
        # ETIQUETA CON LA PREGUNTA
        etiqueta = QLabel("¿Quieres aplicar estas preferencias?")
        layout.addWidget(etiqueta)
        
        # CREAR BOTONES CON QDialogButtonBox
        # QDialogButtonBox crea automáticamente botones estándar
        # QDialogButtonBox.Ok crea un botón "Ok"
        # QDialogButtonBox.Cancel crea un botón "Cancelar"
        # Se combinan con el operador |
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
        # CONECTAR SEÑALES DE LOS BOTONES
        # accepted se emite cuando se pulsa Ok
        # rejected se emite cuando se pulsa Cancel
        # accept() y reject() son métodos heredados de QDialog que cierran el diálogo
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        
        layout.addWidget(botones)
        
        # Establecer el layout al diálogo
        self.setLayout(layout)

# CLASE PRINCIPAL
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # CONFIGURACIÓN INICIAL
        self.setWindowTitle("Preferencias del usuario")
        
        # CREAR CONTENEDOR Y LAYOUT
        contenedor = QWidget()
        
        # QFormLayout es perfecto para formularios
        # Organiza automáticamente en dos columnas: etiqueta y campo
        form_layout = QFormLayout()
        contenedor.setLayout(form_layout)
        
        # CREAR WIDGETS DEL FORMULARIO
        # Campo 1: Nombre (QLineEdit simple)
        self.line_nombre = QLineEdit()
        
        # Campo 2: Lenguaje favorito (QComboBox)
        self.combo_lenguaje = QComboBox()
        # addItems() añade múltiples opciones a la vez (recibe una lista)
        self.combo_lenguaje.addItems(["Python", "Java", "C++", "Kotlin"])
        
        # setEditable(True) permite que el usuario escriba opciones personalizadas
        self.combo_lenguaje.setEditable(True)
        
        # setInsertPolicy define dónde se insertan los nuevos elementos
        # InsertAfterCurrent los inserta después del elemento actual
        self.combo_lenguaje.setInsertPolicy(QComboBox.InsertAfterCurrent)
        
        # setMaxCount limita el número máximo de elementos en el combo
        self.combo_lenguaje.setMaxCount(10)
        
        # Campo 3: Modo oscuro (QCheckBox)
        self.check_modo_oscuro = QCheckBox()
        
        # AÑADIR FILAS AL FORMULARIO
        # addRow() añade una fila con etiqueta y widget
        # Parámetros: (texto_etiqueta, widget)
        form_layout.addRow("Nombre:", self.line_nombre)
        form_layout.addRow("Lenguaje favorito:", self.combo_lenguaje)
        form_layout.addRow("Modo oscuro:", self.check_modo_oscuro)
        
        # Establecer como widget central
        self.setCentralWidget(contenedor)
        
        # CREAR MENÚ
        barra_menu = self.menuBar()
        menu_preferencias = barra_menu.addMenu("&Preferencias")
        
        # CREAR ACCIÓN
        self.accion_confirmar = QAction("Confirmar cambios...", self)
        self.accion_confirmar.triggered.connect(self.confirmar_cambios)
        menu_preferencias.addAction(self.accion_confirmar)
        
        # CREAR BARRA DE HERRAMIENTAS
        barra_herramientas = QToolBar("Barra principal")
        barra_herramientas.addAction(self.accion_confirmar)
        self.addToolBar(barra_herramientas)
        
        # CREAR BARRA DE ESTADO
        self.barra_estado = self.statusBar()
        self.barra_estado.showMessage("Configura tus preferencias y confirma")
    
    # MÉTODO PARA CONFIRMAR CAMBIOS
    def confirmar_cambios(self):
        # ABRIR DIÁLOGO PERSONALIZADO
        # Creamos una instancia del diálogo pasando self como padre
        dialogo = DialogoConfirmacion(self)
        
        # exec() muestra el diálogo de forma MODAL (bloquea la ventana principal)
        # Devuelve QDialog.Accepted si se pulsó Ok, QDialog.Rejected si se canceló
        resultado = dialogo.exec()
        
        # VERIFICAR EL RESULTADO
        if resultado == QDialog.Accepted:
            # El usuario aceptó: mostramos confirmación
            QMessageBox.information(
                self,
                "Preferencias aplicadas",
                "Las preferencias se han aplicado correctamente."
            )
            
            # Actualizamos la barra de estado
            self.barra_estado.showMessage("Preferencias aplicadas correctamente", 2000)
        else:
            # El usuario canceló: solo mostramos mensaje en consola
            print("Los cambios han sido descartados")

# EJECUCIÓN
app = QApplication([])
window = MainWindow()
window.show()
app.exec()