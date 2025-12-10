#José Carlos Mora 2ºDAM
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        self.__estado_actual = "rojo"
        
 
        self.setWindowTitle("Semáforo")
        self.setGeometry(100, 100, 250, 400)  
        
        self._crear_interfaz()
    
    def _crear_interfaz(self):
        

        self.boton_cambiar = QPushButton("Cambiar", self)
        self.boton_cambiar.setFixedHeight(40)  
        
        self.boton_cambiar.clicked.connect(self.cambiar_estado)
        
    
        layout = QVBoxLayout(self)
        

        layout.addStretch()
        

        layout.addWidget(self.boton_cambiar)
        
   
        self.setLayout(layout)
    

    
    def estado(self):
        return self.__estado_actual
    
    def reiniciar(self):
        self.__estado_actual = "rojo"
        self.update()  
    
    def cambiar_estado(self):
        if self.__estado_actual == "rojo":
            self.__estado_actual = "amarillo"
           
            
        elif self.__estado_actual == "amarillo":
            self.__estado_actual = "verde"
            
        else: 
            self.__estado_actual = "rojo"
        
        self.update()
    
   
    
    def paintEvent(self, event):
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  
        
        color_rojo_encendido = QColor(255, 0, 0)      
        color_amarillo_encendido = QColor(255, 255, 0) 
        color_verde_encendido = QColor(0, 200, 0)     
        color_apagado = QColor(80, 80, 80)             
        
        x_centro = 75  
        y_luz_roja = 50      
        y_luz_amarilla = 150  
        y_luz_verde = 250  
        
        tamaño_luz = 80 
        
   
        if self.__estado_actual == "rojo":
            painter.setBrush(color_rojo_encendido) 
        else:
            painter.setBrush(color_apagado) 
        
        painter.setPen(Qt.NoPen) 
        painter.drawEllipse(x_centro, y_luz_roja, tamaño_luz, tamaño_luz)
        
        if self.__estado_actual == "amarillo":
            painter.setBrush(color_amarillo_encendido)  
        else:
            painter.setBrush(color_apagado)
        
        painter.drawEllipse(x_centro, y_luz_amarilla, tamaño_luz, tamaño_luz)
        

        if self.__estado_actual == "verde":
            painter.setBrush(color_verde_encendido)
        else:
            painter.setBrush(color_apagado)  
        
        painter.drawEllipse(x_centro, y_luz_verde, tamaño_luz, tamaño_luz)
        
        painter.setBrush(Qt.NoBrush) 
        painter.setPen(QColor(0, 0, 0))  
        painter.drawRect(60, 30, 110, 310)  


app =QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()