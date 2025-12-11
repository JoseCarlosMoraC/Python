import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QLabel
)
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QRect, Qt
from PySide6.QtCore import Signal
import os



class BotonContador(QPushButton):
    contador_actualizado = Signal(int)

    def __init__(self, parent = None):
        super().__init__("Añadir incidencia: ", parent)

        self.__contador = 0
        self.clicked.connect(self.__incrementar)
 
    def __incrementar(self):
        self.__contador = self.__contador + 1

        nuevo_texto = "Añadir incidencia: " + str(self.__contador)
        self.setText(nuevo_texto)

        self.contador_actualizado.emit(self.__contador)


    def contador(self):
        return self.__contador
    

class IndicadorSimple(QWidget):
    def __init__(self):
        super().__init__()
        self._texto = "OK"
        

    def setTexto(self, texto):

        self._texto = texto
   
        self.update()
      
    
    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)
        color_principio = QColor("#F6F6F6")
        color_amarillo = QColor("#F9F906")
        color_verde_encendido = QColor("#E90000")

        painter.setBrush(color_principio)
        



        painter.setPen(QPen(Qt.black))

        lado = min(self.width(), self.height())


        recto = QRect(
            (self.width() - lado) // 2,   
            (self.height() - lado) // 2,  
            lado,                         
            lado                        
        )

    
        painter.drawEllipse(recto)

    
        painter.setPen(QPen(Qt.black))

    

        painter.drawText(recto, Qt.AlignCenter, self._texto)
        
        
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen T3")
        self.resize(500, 500)

        contenedor = QWidget(self)
        layout = QVBoxLayout(contenedor)
        
   
        self.indicador = IndicadorSimple()
        self.boton = BotonContador()

        contenedor.setLayout(layout)

        self.setCentralWidget(contenedor)
        boton_reset = QPushButton("Reset")
        self.etiqueta = QLabel("Incidencias abiertas: ")
        self.boton.contador_actualizado.connect(self.actualizar_etiqueta)

        boton_reset.clicked.connect(self.resetear)
   
        
        layout.addWidget(self.indicador)
        layout.addWidget(self.etiqueta)
        layout.addWidget(self.boton)
        layout.addWidget(boton_reset)
        
        layout.addWidget

        self.setCentralWidget(contenedor)

    def resetear(self):
        self.boton._BotonContador__contador = 0
        self.boton.setText("Añadir incidencia: 0")
        
        self.actualizar_etiqueta(0)
        self.indicador.setTexto("OK")

    def cambiar_texto(self):
        if BotonContador == 0:
            self.indicador.setTexto("OK")
        elif BotonContador <= 3:
            self.indicador.setTexto("OK")
        elif BotonContador <=7:
            self.indicador.setTexto("Aviso")
        else:
            self.indicador.setTexto("Error")

    def actualizar_etiqueta(self, valor):
        self.etiqueta.setText("Incidencias abiertas: " + str(valor))
        
def cargar_estilos(app, archivo_qss):

    ruta_script = os.path.abspath(os.path.dirname(__file__))


    ruta_qss = os.path.join(ruta_script, archivo_qss)


    with open(ruta_qss, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            app.setStyleSheet(contenido)

       


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cargar_estilos(app, "Mora_JC_estilos.qss")
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
