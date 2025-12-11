# Importamos las bibliotecas necesarias de PySide6
from PySide6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor


# Clase Lienzo, un QWidget personalizado para dibujar un rectángulo con un color variable
class Lienzo(QWidget):
    def __init__(self):
        super().__init__()
        self.color = QColor(255, 0, 0)  # Color inicial (Rojo)

    # Método para actualizar el color del lienzo
    def setColor(self, r, g, b):
        self.color = QColor(r, g, b)  # Creamos un nuevo color con los valores RGB
        self.update()  # Actualizamos el lienzo para que se repinte con el nuevo color

    # Evento de pintura (para dibujar sobre el widget)
    def paintEvent(self, event):
        p = QPainter(self)  # Creamos un objeto QPainter para dibujar
        p.setRenderHint(QPainter.Antialiasing)  # Activamos la suavización de bordes para mejor calidad
        p.setBrush(self.color)  # Establecemos el color con el que vamos a dibujar
        p.drawRect(50, 50, self.width() - 100, self.height() - 100)  # Dibujamos un rectángulo con los márgenes definidos


# Clase Ventana, la ventana principal de la aplicación
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Controlar color con sliders")  # Establecemos el título de la ventana

        self.lienzo = Lienzo()  # Creamos un objeto Lienzo donde se dibujará el rectángulo

        # Creamos tres sliders (deslizadores) para controlar los colores RGB
        self.sr = QSlider(Qt.Horizontal)  # Slider para el color Rojo
        self.sg = QSlider(Qt.Horizontal)  # Slider para el color Verde
        self.sb = QSlider(Qt.Horizontal)  # Slider para el color Azul

        # Configuramos los sliders
        for s in (self.sr, self.sg, self.sb):
            s.setRange(0, 255)  # El rango de valores es de 0 a 255
            s.setValue(100)  # El valor inicial es 100 (un valor intermedio)
            s.valueChanged.connect(self.actualizar_color)  # Conectamos el cambio de valor del slider a un método

        # Layout para organizar los widgets verticalmente
        layout = QVBoxLayout()
        layout.addWidget(self.lienzo)  # Añadimos el lienzo en la parte superior
        layout.addWidget(QLabel("Rojo"))  # Etiqueta para el slider de Rojo
        layout.addWidget(self.sr)  # Slider para el color Rojo
        layout.addWidget(QLabel("Verde"))  # Etiqueta para el slider de Verde
        layout.addWidget(self.sg)  # Slider para el color Verde
        layout.addWidget(QLabel("Azul"))  # Etiqueta para el slider de Azul
        layout.addWidget(self.sb)  # Slider para el color Azul

        self.setLayout(layout)  # Establecemos el layout en la ventana

    # Método que se ejecuta cuando cambia el valor de cualquier slider
    def actualizar_color(self):
        # Actualizamos el color del lienzo con los valores actuales de los sliders
        self.lienzo.setColor(self.sr.value(), self.sg.value(), self.sb.value())


# Creamos la aplicación y la ventana principal
app = QApplication([])  # Creamos una instancia de la aplicación
v = Ventana()  # Creamos la ventana principal
v.show()  # Mostramos la ventana
app.exec()  # Ejecutamos el ciclo de eventos de la aplicación
