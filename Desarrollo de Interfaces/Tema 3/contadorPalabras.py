# Importamos las bibliotecas necesarias de PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QLabel
from PySide6.QtCore import Signal

# Clase AreaPalabras que hereda de QTextEdit para personalizar el área de texto
class AreaPalabras(QTextEdit):
    # Definimos señales para enviar la cantidad de palabras y si se supera el límite
    palabras_cambiadas = Signal(int)  # Señal para emitir el número de palabras
    limite_superado = Signal(bool)  # Señal para indicar si el límite de palabras ha sido superado
    LIMITE = 20  # Límite de palabras permitido

    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Escribe algo...")  # Establecemos el texto de sugerencia (placeholder)

        self.textChanged.connect(self.comprobar)  # Conectamos la señal de cambio de texto con el método comprobar

    def comprobar(self):
        """Método que se ejecuta cada vez que el texto cambia"""
        texto = self.toPlainText().strip()  # Obtenemos el texto del área y eliminamos espacios innecesarios
        palabras = len(texto.split()) if texto else 0  # Contamos las palabras en el texto

        # Emitimos la señal con el número de palabras
        self.palabras_cambiadas.emit(palabras)
        # Emitimos la señal indicando si el límite de palabras ha sido superado
        self.limite_superado.emit(palabras > self.LIMITE)


# Clase Ventana que hereda de QMainWindow para crear la ventana principal
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contador de palabras")  # Establecemos el título de la ventana

        # Creamos un widget contenedor y un layout vertical
        cont = QWidget()
        layout = QVBoxLayout()

        # Creamos el área de texto y la etiqueta para mostrar la cantidad de palabras
        self.area = AreaPalabras()
        self.info = QLabel("Palabras: 0 / 20")

        # Conectamos las señales de AreaPalabras con los métodos de la ventana
        self.area.palabras_cambiadas.connect(self.actualizar_contador)  # Actualiza el contador de palabras
        self.area.limite_superado.connect(self.aviso)  # Muestra un aviso si se supera el límite

        # Añadimos los widgets al layout
        layout.addWidget(self.area)
        layout.addWidget(self.info)

        # Establecemos el layout en el contenedor
        cont.setLayout(layout)
        # Establecemos el contenedor como el widget central de la ventana
        self.setCentralWidget(cont)

    def actualizar_contador(self, n):
        """Actualiza el texto de la etiqueta con el número de palabras actuales"""
        self.info.setText(f"Palabras: {n} / 20")

    def aviso(self, superado):
        """Cambia el color de la etiqueta si se supera el límite de palabras"""
        if superado:
            self.info.setStyleSheet("color: red;")  # Si se supera el límite, el texto se pone rojo
        else:
            self.info.setStyleSheet("color: black;")  # Si no se supera el límite, el texto es negro

# Creamos la aplicación y la ventana principal
app = QApplication([])  # Creamos una instancia de la aplicación
v = Ventana()  # Creamos la ventana
v.show()  # Mostramos la ventana
app.exec()  # Ejecutamos el ciclo de eventos de la aplicación
