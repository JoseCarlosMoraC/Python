from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Signal


# ============================================================
# CLASE BotonContador → botón personalizado con una señal propia
# ============================================================
class BotonContador(QPushButton):

    # Señal personalizada que enviará el número de pulsaciones
    contador_actualizado = Signal(int)

    def __init__(self, parent = None):
        # El texto inicial del botón
        super().__init__("Pulsado 0 veces", parent)

        # Atributo privado → guarda cuántas veces se ha pulsado el botón
        self.__contador = 0

        # Cada vez que se pulse el botón (clicked), llamará al método __incrementar()
        self.clicked.connect(self.__incrementar)


    def __incrementar(self):
        """Método privado que incrementa el contador y emite la señal."""

        # Aumenta el contador interno
        self.__contador = self.__contador + 1

        # Actualiza el texto del botón
        # (Se concatena sin espacios para conservar el código original)
        nuevo_texto = "Pulsado" + str(self.__contador) + "veces"
        self.setText(nuevo_texto)

        # Se emite la señal personalizada, enviando el valor del contador
        self.contador_actualizado.emit(self.__contador)


    def contador(self):
        """Devuelve el valor del contador (getter)."""
        return self.__contador
   


# ============================================================
# CLASE VentanaPrincipal → Interfaz principal
# ============================================================
class VentanaPrincipal(QMainWindow):
     def __init__(self):
        super().__init__()

        self.setWindowTitle("Prueba de botón de contador con señal personalizada")

        # Widget contenedor para el layout
        contenedor = QWidget()
        layout = QVBoxLayout()

        # Creamos el botón personalizado
        self.boton = BotonContador()

        # Etiqueta que mostrará el mensaje
        self.etiqueta = QLabel("Aún no has pulsado el botón")

        # Conectamos la señal personalizada del botón
        # con el método actualizar_etiqueta()
        self.boton.contador_actualizado.connect(self.actualizar_etiqueta)

        # Añadimos widgets al layout
        layout.addWidget(self.boton)
        layout.addWidget(self.etiqueta)

        # Establecemos el layout en el contenedor
        contenedor.setLayout(layout)

        # Y el contenedor se convierte en el "central widget" del QMainWindow
        self.setCentralWidget(contenedor)


     def actualizar_etiqueta(self, valor):
        """Slot que recibe la señal y actualiza el texto de la etiqueta."""
        self.etiqueta.setText("La señal avisó: contador = " + str(valor))



# ============================================================
# EJECUCIÓN DE LA APLICACIÓN
# ============================================================
app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()

