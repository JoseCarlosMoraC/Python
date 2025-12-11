from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QLabel, QPushButton
from PySide6.QtCore import Signal
from PySide6.QtGui import QPalette, QColor

# -----------------------------
# CLASE QUE PERSONALIZA UN QTextEdit
# -----------------------------
class EscribirTexto(QTextEdit):

    # Señales personalizadas:
    # - longitudCambiada(int): avisa cada vez que cambia el número de caracteres
    # - limiteSuperado(bool): avisa si el texto supera o no el límite permitido
    longitudCambiada = Signal(int)
    limiteSuperado = Signal(bool)

    # Límite máximo de caracteres permitidos
    maxCaracteres = 200

    def __init__(self, parent=None):
        super().__init__(parent)

        # Texto que aparece cuando el widget está vacío
        self.setPlaceholderText("Escribe aquí, por favor")

        # Cuando el contenido cambia, se ejecuta verificarTexto()
        # Esta señal existe en QTextEdit por defecto
        self.textChanged.connect(self.verificarTexto)

        # Colores iniciales del área de texto
        self.inicializarColor()

    # Configura colores iniciales del QTextEdit
    def inicializarColor(self):
        paleta = self.palette()
        # Fondo blanco
        paleta.setColor(QPalette.Base, QColor(255, 255, 255))
        # Texto negro
        paleta.setColor(QPalette.Text, QColor(0, 0, 0))
        self.setPalette(paleta)

    # Función que verifica el texto cada vez que cambia
    def verificarTexto(self):
        texto = self.toPlainText()   # Obtener texto plano
        longitud = len(texto)        # Contar caracteres escritos

        # Emitimos señal informando la longitud actual
        self.longitudCambiada.emit(longitud)

        # Emitimos señal indicando si se ha superado el límite de 200 caracteres
        self.limiteSuperado.emit(longitud > self.maxCaracteres)

        # Actualizamos el color del fondo según la longitud
        self.actualizarColor(longitud)

    # Cambia el color del fondo dinámicamente según el número de caracteres
    def actualizarColor(self, longitud):
        if longitud > self.maxCaracteres:
            # Si se supera el límite → fondo rojo
            color = QColor(255, 0, 0)
        else:
            # Si no se supera → el color se vuelve más rojizo a medida que te acercas al límite
            porcentaje = float(longitud) / self.maxCaracteres
            rojo = 255
            verde = int(255 * (1 - porcentaje))  # Disminuye según lo que escribes
            azul = int(255 * (1 - porcentaje))
            color = QColor(rojo, verde, azul)

        # Aplicamos el color al widget
        paleta = self.palette()
        paleta.setColor(QPalette.Base, color)
        paleta.setColor(QPalette.Text, QColor(0, 0, 0))
        self.setPalette(paleta)

    # Permite obtener el límite máximo desde fuera de la clase
    def obtener_max_caracteres(self):
        return self.maxCaracteres



# -----------------------------
# CLASE PARA EL CONTADOR DE CARACTERES
# -----------------------------
class EtiquetaContador(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Texto inicial del contador
        self.setText("Caracteres: 0 / 200")

        # Color inicial del texto (blanco → rojo)
        self.actualizarColor(0, 200)

    # Actualiza el texto de la etiqueta y su color
    def actualizar(self, longitud, maximo):
        texto = "Caracteres: " + str(longitud) + " / " + str(maximo)
        self.setText(texto)
        self.actualizarColor(longitud, maximo)

    # Cambia el color del texto según los caracteres escritos
    def actualizarColor(self, longitud, maximo):
        if longitud > maximo:
            # Si te pasas → texto rojo
            paleta = self.palette()
            paleta.setColor(QPalette.WindowText, QColor(255, 0, 0))
        else:
            # Si aún estás dentro del límite → gradiente blanco → rojo
            porcentaje = float(longitud) / maximo if maximo > 0 else 0
            rojo = 255
            verde = int(255 * (1 - porcentaje))
            azul = int(255 * (1 - porcentaje))

            paleta = self.palette()
            paleta.setColor(QPalette.WindowText, QColor(rojo, verde, azul))
       
        self.setPalette(paleta)



# -----------------------------
# BOTÓN PERSONALIZADO PARA LIMPIAR EL TEXTO
# -----------------------------
class BotonLimpiar(QPushButton):

    # Señal personalizada que se emite cuando el botón limpia el texto
    textoLimpiado = Signal()

    def __init__(self, areaTexto, parent=None):
        super().__init__("Limpiar texto", parent)

        # Guardamos la referencia al QTextEdit para poder limpiarlo
        self.areaTexto = areaTexto

        # Cuando se hace clic → ejecuta self.limpiar()
        self.clicked.connect(self.limpiar)

        # Estilo inicial del botón
        self.setColorNormal()

    def limpiar(self):
        # Vacía el texto del QTextEdit
        self.areaTexto.clear()

        # Emitimos la señal para notificar a la ventana principal
        self.textoLimpiado.emit()

        # Cambiamos el aspecto del botón para indicar que la acción se realizó
        self.setColorFinal()

    # Color por defecto
    def setColorNormal(self):
        paleta = self.palette()
        paleta.setColor(QPalette.Button, QColor(200, 200, 200))  # gris claro
        paleta.setColor(QPalette.ButtonText, QColor(0, 0, 0))    # texto negro
        self.setPalette(paleta)
        self.setAutoFillBackground(True)

    # Color cuando se ha limpiado el texto (verde)
    def setColorFinal(self):
        paleta = self.palette()
        paleta.setColor(QPalette.Button, QColor(200, 255, 200))  # verde suave
        paleta.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        self.setPalette(paleta)
        self.setAutoFillBackground(True)



# -----------------------------
# VENTANA PRINCIPAL QUE UNE TODO
# -----------------------------
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Título y tamaño de la ventana
        self.setWindowTitle("Editor de notas con avisos")
        self.setMinimumSize(500, 400)

        # Contenedor principal y layout vertical
        contenedor = QWidget()
        layout = QVBoxLayout()

        # Widgets principales
        self.contador = EtiquetaContador()  # contador dinámico
        self.area_texto = EscribirTexto()   # área de texto personalizada
        self.boton_limpiar = BotonLimpiar(self.area_texto)
        self.etiqueta_informativa = QLabel("Bienvenido al editor de notas")

        # -----------------------------
        # CONEXIÓN DE SEÑALES
        # -----------------------------

        # Actualiza el contador cada vez que cambia la longitud
        self.area_texto.longitudCambiada.connect(self.actualizarContador)

        # Cambia el texto informativo si se supera el límite
        self.area_texto.limiteSuperado.connect(self.manejarLimiteSuperado)

        # Muestra un mensaje cuando se limpia el texto
        self.boton_limpiar.textoLimpiado.connect(self.mostrarMensajeLimpieza)

        # Añadir widgets al layout
        layout.addWidget(self.contador)
        layout.addWidget(self.area_texto)
        layout.addWidget(self.boton_limpiar)
        layout.addWidget(self.etiqueta_informativa)

        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    # Actualiza el contador del texto
    def actualizarContador(self, longitud):
        maximo = self.area_texto.obtener_max_caracteres()
        self.contador.actualizar(longitud, maximo)

    # Muestra un mensaje si se supera o no el límite
    def manejarLimiteSuperado(self, superado):
        if superado:
            self.etiqueta_informativa.setText("Te has pasado de caracteres")
        else:
            self.etiqueta_informativa.setText("Bienvenido al editor de notas")

    # Mensaje cuando se pulsa limpiar
    def mostrarMensajeLimpieza(self):
        self.etiqueta_informativa.setText("El texto ha sido limpiado correctamente")


# -----------------------------
# INICIO DE LA APLICACIÓN
# -----------------------------
app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()