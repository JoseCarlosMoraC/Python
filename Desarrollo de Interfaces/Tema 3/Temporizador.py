# Importamos las bibliotecas necesarias de PySide6
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow
from PySide6.QtCore import QTimer, Signal


# Clase CronometroLabel, que hereda de QLabel para mostrar el cronómetro
class CronometroLabel(QLabel):
    # Definimos una señal que se emite cuando el segundo cambia
    segundo_actualizado = Signal(int)

    def __init__(self):
        super().__init__("0")  # Inicializamos la etiqueta con "0"
        self.__segundo = 0  # Inicializamos el contador de segundos

        # Creamos un temporizador que se activará cada segundo
        self.timer = QTimer()
        self.timer.setInterval(1000)  # El temporizador se activará cada 1000 ms (1 segundo)
        self.timer.timeout.connect(self.tic)  # Conectamos el temporizador al método tic

    def tic(self):
        """Este método se ejecuta cada vez que el temporizador se dispara (cada segundo)"""
        self.__segundo += 1  # Incrementamos el contador de segundos
        self.setText(str(self.__segundo))  # Actualizamos el texto del cronómetro en la etiqueta
        self.segundo_actualizado.emit(self.__segundo)  # Emitimos la señal con el número de segundos

    def iniciar(self):
        """Inicia el cronómetro"""
        self.timer.start()  # Comienza el temporizador

    def pausar(self):
        """Pausa el cronómetro"""
        self.timer.stop()  # Detiene el temporizador

    def reiniciar(self):
        """Reinicia el cronómetro"""
        self.timer.stop()  # Detiene el temporizador
        self.__segundo = 0  # Reinicia el contador de segundos
        self.setText("0")  # Reinicia el texto del cronómetro a "0"
        self.segundo_actualizado.emit(self.__segundo)  # Emite la señal con el valor 0


# Clase Ventana, que hereda de QMainWindow para crear la ventana principal
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cronómetro simple")  # Establecemos el título de la ventana

        cont = QWidget()  # Creamos un widget para contener los elementos
        layout = QVBoxLayout()  # Creamos un layout vertical para organizar los widgets

        self.crono = CronometroLabel()  # Creamos una instancia del cronómetro

        # Creamos los botones para controlar el cronómetro
        btn_ini = QPushButton("Iniciar")  # Botón para iniciar el cronómetro
        btn_pau = QPushButton("Pausar")  # Botón para pausar el cronómetro
        btn_rei = QPushButton("Reiniciar")  # Botón para reiniciar el cronómetro

        # Conectamos los botones a los métodos correspondientes
        btn_ini.clicked.connect(self.crono.iniciar)  # Al hacer clic, se inicia el cronómetro
        btn_pau.clicked.connect(self.crono.pausar)  # Al hacer clic, se pausa el cronómetro
        btn_rei.clicked.connect(self.crono.reiniciar)  # Al hacer clic, se reinicia el cronómetro

        # Añadimos los widgets al layout
        layout.addWidget(self.crono)  # Añadimos el cronómetro a la ventana
        layout.addWidget(btn_ini)  # Añadimos el botón "Iniciar"
        layout.addWidget(btn_pau)  # Añadimos el botón "Pausar"
        layout.addWidget(btn_rei)  # Añadimos el botón "Reiniciar"

        cont.setLayout(layout)  # Establecemos el layout en el widget contenedor
        self.setCentralWidget(cont)  # Establecemos el widget como central en la ventana

# Creamos la aplicación y la ventana principal
app = QApplication([])  # Creamos una instancia de la aplicación
v = Ventana()  # Creamos la ventana principal
v.show()  # Mostramos la ventana
app.exec()  # Ejecutamos el ciclo de eventos de la aplicación
