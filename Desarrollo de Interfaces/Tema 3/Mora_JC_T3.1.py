import sys
from PySide6.QtWidgets import (QApplication,QMainWindow, QWidget, QVBoxLayout, 
                             QCheckBox, QPushButton, QLineEdit, 
                             QRadioButton, QComboBox, QLabel)

class VentanaWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setWindowTitle('5 Widgets Básicos')
        self.setGeometry(100, 100, 300, 250)
        
        layout = QVBoxLayout()
        
        self.checkbox = QCheckBox('Acepto los términos')
        layout.addWidget(self.checkbox)
        
        
        self.boton = QPushButton('Pulsar aquí')
        self.boton.clicked.connect(self.on_click)
        layout.addWidget(self.boton)
        
        
        self.linea_texto = QLineEdit()
        self.linea_texto.setPlaceholderText('Escribe algo...')
        layout.addWidget(self.linea_texto)
        
        
        self.radio = QRadioButton('Opción A')
        layout.addWidget(self.radio)
        
  
        self.combo = QComboBox()
        self.combo.addItems(['Opción 1', 'Opción 2', 'Opción 3'])
        layout.addWidget(self.combo)
        
      
        self.etiqueta = QLabel('')
        layout.addWidget(self.etiqueta)
        
        self.setLayout(layout)
    
    def on_click(self):
        self.etiqueta.setText('¡Botón pulsado!')

app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()