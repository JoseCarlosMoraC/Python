from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QLabel, QPushButton
from PySide6.QtCore import Signal
from PySide6.QtGui import QPalette, QColor

class EscribirTexto(QTextEdit):
   
    longitudCambiada = Signal(int)
    limiteSuperado = Signal(bool)

    maxCaracteres = 200

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlaceholderText("Escribe aquí, por favor")
        self.textChanged.connect(self.verificarTexto)
        self.inicializarColor()

    def inicializarColor(self):
        paleta = self.palette()
        paleta.setColor(QPalette.Base, QColor(255, 255, 255))
        paleta.setColor(QPalette.Text, QColor(0, 0, 0))
        self.setPalette(paleta)

    def verificarTexto(self):
        texto = self.toPlainText()
        longitud = len(texto)
        

        self.longitudCambiada.emit(longitud)
        self.limiteSuperado.emit(longitud > self.maxCaracteres)
        
        self.actualizarColor(longitud)

    def actualizarColor(self, longitud):
        if longitud > self.maxCaracteres:
            color = QColor(255, 0, 0)
        else:
            porcentaje = float(longitud) / self.maxCaracteres
            rojo = 255
            verde = int(255 * (1 - porcentaje))
            azul = int(255 * (1 - porcentaje))
            color = QColor(rojo, verde, azul)

        paleta = self.palette()
        paleta.setColor(QPalette.Base, color)
        paleta.setColor(QPalette.Text, QColor(0, 0, 0))
        self.setPalette(paleta)

    def obtener_max_caracteres(self):
        return self.maxCaracteres


class EtiquetaContador(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Caracteres: 0 / 200")
        self.actualizarColor(0, 200)

    def actualizar(self, longitud, maximo):
        texto = "Caracteres: " + str(longitud) + " / " + str(maximo)
        self.setText(texto)
        self.actualizarColor(longitud, maximo)

    def actualizarColor(self, longitud, maximo):
        if longitud > maximo:
            paleta = self.palette()
            paleta.setColor(QPalette.WindowText, QColor(255, 0, 0))
        else:
            porcentaje = float(longitud) / maximo if maximo > 0 else 0
            rojo = 255
            verde = int(255 * (1 - porcentaje))
            azul = int(255 * (1 - porcentaje))
            
            paleta = self.palette()
            paleta.setColor(QPalette.WindowText, QColor(rojo, verde, azul))
        
        self.setPalette(paleta)


class BotonLimpiar(QPushButton):
    textoLimpiado = Signal()

    def __init__(self, areaTexto, parent=None):
        super().__init__("Limpiar texto", parent)
        self.areaTexto = areaTexto
        self.clicked.connect(self.limpiar)
        self.setColorNormal()

    def limpiar(self):
        self.areaTexto.clear()
        self.textoLimpiado.emit()
        self.setColorFinal()

    def setColorNormal(self):
        paleta = self.palette()
        paleta.setColor(QPalette.Button, QColor(200, 200, 200))
        paleta.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        self.setPalette(paleta)
        self.setAutoFillBackground(True)

    def setColorFinal(self):
        paleta = self.palette()
        paleta.setColor(QPalette.Button, QColor(200, 255, 200))
        paleta.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        self.setPalette(paleta)
        self.setAutoFillBackground(True)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de notas con avisos")
        self.setMinimumSize(500, 400)


        contenedor = QWidget()
        layout = QVBoxLayout()

        self.contador = EtiquetaContador()
        self.area_texto = EscribirTexto()
        self.boton_limpiar = BotonLimpiar(self.area_texto)
        self.etiqueta_informativa = QLabel("Bienvenido al editor de notas")

        self.area_texto.longitudCambiada.connect(self.actualizarContador)
        self.area_texto.limiteSuperado.connect(self.manejarLimiteSuperado)
        self.boton_limpiar.textoLimpiado.connect(self.mostrarMensajeLimpieza)

        layout.addWidget(self.contador)
        layout.addWidget(self.area_texto)
        layout.addWidget(self.boton_limpiar)
        layout.addWidget(self.etiqueta_informativa)

        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def actualizarContador(self, longitud):
        maximo = self.area_texto.obtener_max_caracteres()
        self.contador.actualizar(longitud, maximo)

    def manejarLimiteSuperado(self, superado):
        if superado:
            self.etiqueta_informativa.setText("Te has pasado de caracteres")
        else:
            self.etiqueta_informativa.setText("Bienvenido al editor de notas")

    def mostrarMensajeLimpieza(self):
        self.etiqueta_informativa.setText("El texto ha sido limpiado correctamente")

app =QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()