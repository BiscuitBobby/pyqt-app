from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit
import textbox
from buttons import button_list
from PyQt5.QtCore import Qt
from demoData import *
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from image import getImg
url_image = curv




app = QApplication([])
window = QWidget()

# the widgets
sidebar = QVBoxLayout()  # vertical box layout
image = QVBoxLayout()
# nav = QHBoxLayout
masterLay = QHBoxLayout()  # master layout (put other layouts in here), Horizontal box layout

image_label = getImg()
image_label.setStyleSheet("border-radius: 10px;")

# sidebar
buttList = button_list(image_label)
for i in buttList:
    sidebar.addWidget(i)
text = textbox.NewText()
# sidebar.addWidget(text)
sidebar.setAlignment(Qt.AlignTop)

# adding image to layout
image.addWidget(image_label)
image.addStretch()

# putting together the master layout
masterLay.addLayout(sidebar)
masterLay.addLayout(image)
masterLay.setAlignment(Qt.AlignHCenter)

palette = window.palette()
palette.setColor(palette.Window, QColor('#17202a'))  # set the titlebar color to dark blue, doesn't work on gnome
window.setPalette(palette)


window.setLayout(masterLay)
window.setStyleSheet("background-color: #17202a;")
window.show()

app.exec_()
