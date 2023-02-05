from PyQt5.QtCore import Qt
from demoData import *
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QImage, QPixmap


def getImg(url_image=curv):
    # app = QApplication([])
    image = QImage()
    image.loadFromData(requests.get(url_image).content)

    image_label = QLabel()
    image_label.setPixmap(QPixmap(image).scaled(800, 800, Qt.KeepAspectRatio))
    image_label.resize(60, 15)
    #image_label.show()

    #app.exec_()
    return image_label
