import sys # Módulo do sistema
from PyQt6.QtCore import * # Core do PyQt6
from PyQt6.QtWidgets import * # Componentes de GUI do PyQt6


app = QApplication(sys.argv) # Aplicação principal
msgBox = QMessageBox() # Janela de mensagem
msgBox.setText("Hello, World!")
msgBox.exec()
app.exec()