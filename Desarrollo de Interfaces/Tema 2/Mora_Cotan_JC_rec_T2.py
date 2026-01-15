# José Carlos Mora 2º DAM
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QTabWidget, QWidget, QFormLayout, QCheckBox, QTextEdit, QToolBar)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    #He creado una ventana principal con un minimo de tamaño
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bloc de incidencias")
        self.setMinimumSize(800, 600)
    
    #He agregado las funciones de crear
        self.crear_central()
        self.crear_acciones()
        self.crear_menus()
        self.crear_toolbar()
        self.crear_statusbar()
    
    #Aqui he creado 2 pestañas porque me estaba dando error de otra manera, por lo que he preferido hacerlo asi
    #Funciona tanto una pestaña como otra, en el caso de la primera, si creas campos y le das a generar incidencia, te lo crea
    #En el caso del historial, te lo crea con los datos necesarios

    def crear_central(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        tab1 = QWidget()
        layout_tab1 = QFormLayout()
        tab1.setLayout(layout_tab1)
        
        self.line_grupo = QLineEdit()
        self.line_grupo.setPlaceholderText("Entrada de grupo")
        
        self.line_alumno = QLineEdit()
        self.line_alumno.setPlaceholderText("Entrada de alumno/a")

        self.line_tipo = QLineEdit()
        self.line_tipo.setPlaceholderText("Tipo de incidencia")

        self.line_descripcion = QLineEdit()
        self.line_descripcion.setPlaceholderText("Descripción de la incidencia")

        self.check_verificar = QCheckBox("Verificación")

         
        layout_tab1.addRow("Entrada de grupo:", self.line_grupo)
        layout_tab1.addRow("Entrada de alumno/a:", self.line_alumno)
        layout_tab1.addRow("Tipo de incidencia:", self.line_tipo)
        layout_tab1.addRow("Descripción de la incidencia:", self.line_descripcion)
        layout_tab1.addRow("Incidencia resuelta", self.check_verificar)

        self.tabs.addTab(tab1, "Incidencia")
    
    #Tal como he dicho antes, el historial me estaba causando problemas por lo que he tenido que hacerlo así
        tab2 = QWidget()
        layout_tab2 = QVBoxLayout()
        tab2.setLayout(layout_tab2)
        
        self.label_resumen = QLabel("Completa la incidencia para ver el historial")
        self.label_resumen.setAlignment(Qt.AlignCenter)
        fuente = self.label_resumen.font()
        fuente.setPointSize(12)
        self.label_resumen.setFont(fuente)
        
        layout_tab2.addWidget(self.label_resumen)
        
        boton_ver_historial = QPushButton("Generar historial")
        boton_ver_historial.clicked.connect(self.slot_ver_historial)
        layout_tab2.addWidget(boton_ver_historial)
        layout_tab2.addStretch()
        
        self.tabs.addTab(tab2, "Historial de incidencias")
    
    #He creado las accions con un atajo
    def crear_acciones(self):
        self.accion_nueva = QAction("Nueva incidencia", self)
        self.accion_nueva.setShortcut("Ctrl+N")
        self.accion_nueva.triggered.connect(self.slot_nueva_encuesta)
        
        self.accion_historial = QAction("Generar incidencia", self)
        self.accion_historial.setShortcut("Ctrl+R")
        self.accion_historial.triggered.connect(self.slot_ver_historial)
        
        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut("Ctrl+Q")
        self.accion_salir.triggered.connect(self.slot_salir)
        
        self.accion_acerca = QAction("Acerca de", self)
        self.accion_acerca.triggered.connect(self.slot_acerca_de)

        self.accion_limpiar = QAction("Limpiar", self)
        self.accion_limpiar.triggered.connect(self.slot_limpiar)

    #Aqui he creado el menú, por una parte archivo con nueva encuesta, historial y salir
    #Por otro lado, el ayuda con un acerca de, donde he puesto un mensaje cualquiera
    def crear_menus(self):
        barra_menu = self.menuBar()
        
        menu_archivo = barra_menu.addMenu("&Archivo")
        menu_archivo.addSeparator()
        menu_archivo.addAction(self.accion_nueva)
        menu_archivo.addAction(self.accion_historial)
        menu_archivo.addSeparator()
        menu_archivo.addAction(self.accion_salir)
    
        menu_ayuda = barra_menu.addMenu("&Ayuda")
        menu_ayuda.addAction(self.accion_acerca)

    #Tambien he creado una barra de herramientas para añadir cosas que no me dejaba en la ventana principal
    def crear_toolbar(self):
        toolbar = QToolBar("Incidencia")
        toolbar.addAction(self.accion_nueva)
        toolbar.addAction(self.accion_historial)
        toolbar.addSeparator()
        toolbar.addAction(self.accion_limpiar)
        self.addToolBar(toolbar)

    def crear_statusbar(self):
        self.barra_estado = self.statusBar()
        self.barra_estado.showMessage("Bienvenido", 5000)

    #Aqui simplemente he creado un mensaje para preguntar si quiere iniciar, en el caso de que si, borra todo lo que estaba escrito
    def slot_nueva_encuesta(self):
        respuesta = QMessageBox.question(
            self,
            "Nueva incidencia",
            "¿Estás seguro de que quieres iniciar una nueva incidencia?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            self.line_grupo.clear()
            self.line_alumno.clear()
            self.line_tipo.clear()
            self.line_descripcion.clear()
            self.check_verificar.setChecked(False)
            
            self.tabs.setCurrentIndex(0)
            
            self.barra_estado.showMessage("Nueva encuesta iniciada", 3000)

    #Practicamente he hecho lo mismo que antes, porque quería que también hubiese un mensaje de confirmación
    def slot_limpiar(self):
        respuesta = QMessageBox.question(
            self,
            "Limpiar",
            "¿Estás seguro de que quieres limpiar?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            self.line_grupo.clear()
            self.line_alumno.clear()
            self.line_tipo.clear()
            self.line_descripcion.clear()
            self.check_verificar.setChecked(False)
            
            self.tabs.setCurrentIndex(0)
            
            self.barra_estado.showMessage("Nueva encuesta iniciada", 3000)

    #Aqui he creado el historial
    def slot_ver_historial(self):
        grupo = self.line_grupo.text() 
        alumno = self.line_alumno.text() 
        tipo = self.line_tipo.text()
        descripcion = self.line_descripcion.text()
        verificada = "Sí" if self.check_verificar.isChecked() else "No"
       
        
        historial = f"""
        
        Grupo: {grupo}
        Alumno/a: {alumno}
        Tipo: {tipo}
        Descripción: {descripcion}
        Recomendaría: {verificada}
        """
        self.label_resumen.setText(historial)
        self.tabs.setCurrentIndex(1) 
        QMessageBox.information(
            self,
            "Incidencia generada",
            "La incidencia se ha generado correctamente"
        )
        
        self.barra_estado.showMessage("Historial generado correctamente", 3000)

    #Salir con un mensaje de confirmación
    def slot_salir(self):
        respuesta = QMessageBox.question(
            self,
            "Salir",
            "¿Estás seguro de que quieres salir de la aplicación?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            self.close()

    #Acerca de con un mensaje simple
    def slot_acerca_de(self):
        QMessageBox.information(
            self,
            "Esto\n",
            "Es\n"
            "Un\n"
            "Mensaje\n"
            "De\n"
            "Ayuda\n"
        )

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()