# José Carlos Mora 2º DAM

# He creado un QProgressBar como widget central y un QTimer que pregunta al usuario
# cada 2 segundos si quiere aumentar, disminuir o salir
# El progreso se incrementa o decrementa en pasos de 20 y el titulo de la ventana
# se actualiza según el valor actual. También muestro el progreso en la consola

from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar
from PySide6.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.progreso_actual = 0

      
        self.barra = QProgressBar()
        self.barra.setRange(0, 100)
        self.barra.setValue(self.progreso_actual)

        
        self.setCentralWidget(self.barra)
        self.setWindowTitle("Progreso: 0%")

       
        self.timer = QTimer()
        self.timer.timeout.connect(self.preguntar_usuario)
        self.timer.start(2000)  

  
        self.titulos = ["Progreso: 0%", "Progreso: 20%", "Progreso: 40%", "Progreso: 60%", "Progreso: 80%", "Completado"]

    def preguntar_usuario(self):
       
        print("\n=== Control de progreso ===")
        print("1 → Aumentar progreso")
        print("2 → Retroceder progreso")
        print("0 → Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            self.cambiar_progreso("aumentar")
        elif opcion == "2":
            self.cambiar_progreso("disminuir")
        elif opcion == "0":
            print("Adios")
            self.timer.stop()
            self.close()
        else:
            print("Opción no válida.")

    def cambiar_progreso(self, modo):
        if modo == "aumentar":
            self.progreso_actual += 20
            if self.progreso_actual > 100:
                self.progreso_actual = 100
        elif modo == "disminuir":
            self.progreso_actual -= 20
            if self.progreso_actual < 0:
                self.progreso_actual = 0

     
        self.barra.setValue(self.progreso_actual)


        if self.progreso_actual == 100:
            self.setWindowTitle(self.titulos[5])
        else:
           
            indice = self.progreso_actual // 20
            self.setWindowTitle(self.titulos[indice])


        print("Progreso actual:", self.progreso_actual, "%")



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
