import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QDateEdit

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Drop-down Menu Example')


dropdown = QComboBox(window)
dropdown.addItem("curiosity")
dropdown.addItem("Option 2")
dropdown.addItem("Option 3")
dropdown.move(20, 20)

window.show()
sys.exit(app.exec_())
