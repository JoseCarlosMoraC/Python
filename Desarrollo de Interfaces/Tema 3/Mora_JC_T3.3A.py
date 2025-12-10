#José Carlos Mora 2ºDAM
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QTimer


class VentanaPrincipal(QWidget):
   
    def __init__(self):
        super().__init__()
        
        self.__estado_actual = "rojo"
        
        self.temporizador = QTimer(self)
        self.temporizador.setInterval(1500)  
        
        self.temporizador.timeout.connect(self.cambiar_estado)
        
     
        self.automatico_activo = False
        
     
        self.setWindowTitle("Semáforo")
        self.setGeometry(100, 100, 280, 450)
        
   
        self._crear_interfaz()
    
    def _crear_interfaz(self):
    
        self.boton_cambiar = QPushButton("Cambiar", self)
        self.boton_cambiar.setFixedHeight(40)
        self.boton_cambiar.clicked.connect(self.cambiar_estado)
        self.boton_auto = QPushButton("Iniciar", self)
        self.boton_auto.setFixedHeight(40)
        self.boton_auto.clicked.connect(self.alternar_automatico)
        
        
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.boton_cambiar)
        layout_botones.addWidget(self.boton_auto)
        
       
        layout = QVBoxLayout(self)
        layout.addStretch()  
        layout.addLayout(layout_botones)  

        
        self.setLayout(layout)
    

    
    def estado(self):
        return self.__estado_actual
    
    def reiniciar(self):
        self.__estado_actual = "rojo"
        
        if self.automatico_activo:
            self.temporizador.stop()
            self.automatico_activo = False
            self.boton_auto.setText("Iniciar")
        
        self.update()
    
    
    def cambiar_estado(self):

        
        if self.__estado_actual == "rojo":
            self.__estado_actual = "amarillo"
            
        elif self.__estado_actual == "amarillo":
            self.__estado_actual = "verde"
            
        else:  
            self.__estado_actual = "rojo"
         
        
        self.update()
    
    def alternar_automatico(self):
     
        
        if self.automatico_activo:
            self.temporizador.stop()
            self.automatico_activo = False
            self.boton_auto.setText("Iniciar")
            
        else:
          
            self.temporizador.start()
            self.automatico_activo = True
            self.boton_auto.setText("Pausar Automático")

    
    def paintEvent(self, event):
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        

        rojo_encendido = QColor(255, 0, 0)
        amarillo_encendido = QColor(255, 255, 0)
        verde_encendido = QColor(0, 200, 0)
        apagado = QColor(60, 60, 60)
        
    
        x = 90
        y_roja = 50
        y_amarilla = 160
        y_verde = 270
        tamaño = 80
        
  
        painter.setBrush(QColor(30, 30, 30))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(70, 30, 120, 340, 15, 15)
        

        color = rojo_encendido if self.__estado_actual == "rojo" else apagado
        painter.setBrush(color)
        painter.drawEllipse(x, y_roja, tamaño, tamaño)
   
        color = amarillo_encendido if self.__estado_actual == "amarillo" else apagado
        painter.setBrush(color)
        painter.drawEllipse(x, y_amarilla, tamaño, tamaño)
        
     
        color = verde_encendido if self.__estado_actual == "verde" else apagado
        painter.setBrush(color)
        painter.drawEllipse(x, y_verde, tamaño, tamaño)
        
        painter.setBrush(Qt.NoBrush)
        painter.setPen(QColor(200, 200, 200))
        painter.drawEllipse(x, y_roja, tamaño, tamaño)
        painter.drawEllipse(x, y_amarilla, tamaño, tamaño)
        painter.drawEllipse(x, y_verde, tamaño, tamaño)



app =QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()