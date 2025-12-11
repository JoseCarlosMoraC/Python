# José Carlos Mora 2ºDAM

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QTimer


class VentanaPrincipal(QWidget):
   
    def __init__(self):
        super().__init__()
       
        # Estado actual del semáforo. Comienza en rojo.
        # Se marca como "privado" con doble guion bajo.
        self.__estado_actual = "rojo"
       
        # -----------------------------
        # CONFIGURACIÓN DEL TEMPORIZADOR
        # -----------------------------
        # QTimer permite ejecutar una función automáticamente cada cierto tiempo
        self.temporizador = QTimer(self)

        # Intervalo de tiempo entre cambios (1500 ms = 1.5 segundos)
        self.temporizador.setInterval(1500)  

        # Cuando el temporizador termina, llama a cambiar_estado()
        self.temporizador.timeout.connect(self.cambiar_estado)
       
        # Bandera que indica si el modo automático está activado o no
        self.automatico_activo = False
       
        # -----------------------------
        # CONFIGURACIÓN DE LA VENTANA
        # -----------------------------
        self.setWindowTitle("Semáforo")
        self.setGeometry(100, 100, 280, 450)
       
        # Crear la interfaz gráfica
        self._crear_interfaz()
   
    # ============================================================
    # INTERFAZ (BOTONES Y LAYOUTS)
    # ============================================================
    def _crear_interfaz(self):
       
        # Botón que cambia el estado manualmente
        self.boton_cambiar = QPushButton("Cambiar", self)
        self.boton_cambiar.setFixedHeight(40)
        self.boton_cambiar.clicked.connect(self.cambiar_estado)

        # Botón que inicia/pausa el modo automático
        self.boton_auto = QPushButton("Iniciar", self)
        self.boton_auto.setFixedHeight(40)
        self.boton_auto.clicked.connect(self.alternar_automatico)
       
        # Layout horizontal para colocar los botones lado a lado
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.boton_cambiar)
        layout_botones.addWidget(self.boton_auto)
       
        # Layout principal (vertical)
        layout = QVBoxLayout(self)
        layout.addStretch()               # Empuja todo hacia abajo
        layout.addLayout(layout_botones)  # Añadimos los botones

        self.setLayout(layout)
   
    # ============================================================
    # GESTIÓN DEL ESTADO DEL SEMÁFORO
    # ============================================================
   
    def estado(self):
        """Devuelve el estado actual."""
        return self.__estado_actual
   
    def reiniciar(self):
        """Reinicia el semáforo al estado 'rojo' y detiene el modo automático."""
       
        self.__estado_actual = "rojo"

        # Si estaba en modo automático, lo detenemos
        if self.automatico_activo:
            self.temporizador.stop()
            self.automatico_activo = False
            self.boton_auto.setText("Iniciar")

        self.update()  # Fuerza el repintado
   
    def cambiar_estado(self):
        """
        Cambia el estado del semáforo siguiendo el orden:
        rojo → amarillo → verde → rojo
        """

        if self.__estado_actual == "rojo":
            self.__estado_actual = "amarillo"
       
        elif self.__estado_actual == "amarillo":
            self.__estado_actual = "verde"
       
        else:  # estaba en verde
            self.__estado_actual = "rojo"
       
        # update() obliga a redibujar el widget → llama paintEvent()
        self.update()
   
    # ============================================================
    # INICIAR / DETENER MODO AUTOMÁTICO
    # ============================================================
    def alternar_automatico(self):
        """
        Activa o desactiva el modo automático.
        Este modo utiliza un QTimer para cambiar de estado cada 1.5 segundos.
        """

        # Si ya está activo, lo detenemos
        if self.automatico_activo:
            self.temporizador.stop()
            self.automatico_activo = False
            self.boton_auto.setText("Iniciar")
       
        # Si no lo está, lo activamos
        else:
            self.temporizador.start()
            self.automatico_activo = True
            self.boton_auto.setText("Pausar Automático")

    # ============================================================
    # DIBUJO DEL SEMÁFORO (paintEvent)
    # ============================================================
    def paintEvent(self, event):
        """
        Este método se ejecuta automáticamente cada vez que se llama a update()
        o cuando la ventana necesita repintarse.
        Aquí dibujamos las luces del semáforo y su estructura.
        """
       
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Bordes suaves
       
        # Colores encendidos
        rojo_encendido = QColor(255, 0, 0)
        amarillo_encendido = QColor(255, 255, 0)
        verde_encendido = QColor(0, 200, 0)

        # Color para luces apagadas
        apagado = QColor(60, 60, 60)
       
        # Coordenadas y tamaño de las luces
        x = 90
        y_roja = 50
        y_amarilla = 160
        y_verde = 270
        tamaño = 80
       
        # -------------------------------
        # DIBUJAR LA CAJA DEL SEMÁFORO
        # -------------------------------
        painter.setBrush(QColor(30, 30, 30))  # Fondo gris oscuro
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(70, 30, 120, 340, 15, 15)
       
        # -------------------------------
        # LUZ ROJA
        # -------------------------------
        color = rojo_encendido if self.__estado_actual == "rojo" else apagado
        painter.setBrush(color)
        painter.drawEllipse(x, y_roja, tamaño, tamaño)
       
        # -------------------------------
        # LUZ AMARILLA
        # -------------------------------
        color = amarillo_encendido if self.__estado_actual == "amarillo" else apagado
        painter.setBrush(color)
        painter.drawEllipse(x, y_amarilla, tamaño, tamaño)
       
        # -------------------------------
        # LUZ VERDE
        # -------------------------------
        color = verde_encendido if self.__estado_actual == "verde" else apagado
        painter.setBrush(color)
        painter.drawEllipse(x, y_verde, tamaño, tamaño)
       
        # Dibujar los bordes circulares de las luces
        painter.setBrush(Qt.NoBrush)
        painter.setPen(QColor(200, 200, 200))
        painter.drawEllipse(x, y_roja, tamaño, tamaño)
        painter.drawEllipse(x, y_amarilla, tamaño, tamaño)
        painter.drawEllipse(x, y_verde, tamaño, tamaño)



# ============================================================
# EJECUCIÓN DE LA APLICACIÓN
# ============================================================
app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()