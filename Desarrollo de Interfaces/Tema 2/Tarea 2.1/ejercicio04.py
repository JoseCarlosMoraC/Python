# José Carlos Mora 2º DAM

from PySide6.QtWidgets import QApplication, QMainWindow, QDateTimeEdit
from PySide6.QtCore import QDateTime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.dt_edit = QDateTimeEdit()
        self.dt_edit.setDateTime(QDateTime.currentDateTime())

      
        self.dt_edit.setDisplayFormat("dddd, d 'de' MMMM 'de' yyyy hh:mm")


        self.dt_edit.dateTimeChanged.connect(self.mostrar_fecha)

   
        self.setCentralWidget(self.dt_edit)

      
        self.mostrar_fecha(self.dt_edit.dateTime())

    def mostrar_fecha(self, fecha_hora):

        self.setWindowTitle(fecha_hora.toString("dddd, d 'de' MMMM 'de' yyyy hh:mm"))
        print("Fecha elegida:", fecha_hora.toString("dddd, d 'de' MMMM 'de' yyyy hh:mm"))



app = QApplication([])
ventana = MainWindow()
ventana.show()
app.exec()
