from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QPushButton, QLineEdit
import sys


class ListaTareas(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista de tareas")

        self.lista = QListWidget()
        self.lista.setStyleSheet("background-color: #fff5d6;")

        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText("Nueva tarea...")

        self.btn_agregar = QPushButton("Agregar")
        self.btn_borrar = QPushButton("Eliminar seleccionada")

        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_borrar.clicked.connect(self.eliminar)

        l = QVBoxLayout()
        l.addWidget(self.entrada)
        l.addWidget(self.btn_agregar)
        l.addWidget(self.lista)
        l.addWidget(self.btn_borrar)

        self.setLayout(l)

    def agregar(self):
        texto = self.entrada.text()
        if texto != "":
            self.lista.addItem(texto)
            self.entrada.clear()

    def eliminar(self):
        item = self.lista.currentItem()
        if item:
            self.lista.takeItem(self.lista.row(item))


app = QApplication(sys.argv)
v = ListaTareas()
v.show()
app.exec()
