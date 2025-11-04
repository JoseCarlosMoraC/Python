from PySide6.QtWidgets import QApplication, QWidget

# Solo es necesario si quieres acceder a los argumentos de la línea de comandos
import sys

# Necesitas una (y solo una) instancia de QApplication por aplicación.
# Pasa sys.argv para permitir argumentos desde la línea de comandos.
# Si sabes que no vas a usar argumentos, QApplication([]) también funciona.
app = QApplication(sys.argv)

# Crea un widget de Qt, que será nuestra ventana.
window = QWidget()
window.show()  # IMPORTANTE: las ventanas están ocultas por defecto.

# Inicia el bucle de eventos.
app.exec()

# La ejecución no continuará hasta que salgas y el bucle de eventos termine.