from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit
from diagbox import widg
import textbox
from buttons import button_list, RoundedButton
from PyQt5.QtCore import Qt
from demoData import *
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from image import getImg
import threading
url_image = curv


def thred(func):
    thread = threading.Thread(target=func, args=(10,))
    thread.start()


def next():
    global image_label
    global n
    global but
    if (n+1) < len(lst):
        print(f'loading image {n}...')
        but.update()
        n += 1
        curv = lst[n]
        img_data = requests.get(curv).content
        print(f'imported image {curv}')
        image = QImage()
        image.loadFromData(img_data)
        image_label.setPixmap(QPixmap(image))
        pic = QPixmap(image).scaled(800, 800, Qt.KeepAspectRatio)
        image_label.setPixmap(pic)
        image_label.update()


def prev():
    global image_label
    global n
    global but
    if (n-1) >= 0:
        n -= 1
        print(f'loading image {n}...')
        curv = lst[n]
        img_dat = requests.get(curv).content
        image = QImage()
        image.loadFromData(img_dat)
        print(f'imported image {curv}')
        image_label.setPixmap(QPixmap(image))
        pic = QPixmap(image).scaled(800, 800, Qt.KeepAspectRatio)
        image_label.setPixmap(pic)
        image_label.update()


if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()

    # ---------------------------------------------buttons--------------------------------------------------------------
    # prev button
    previ = RoundedButton("<")
    previ.setFixedSize(50, 50)
    previ.clicked.connect(lambda: thred(prev()))
    previ.setStyleSheet("background-color: #283747; border-radius: 10px;")
    # next button
    nekst = RoundedButton(">")
    nekst.setFixedSize(50, 50)
    nekst.clicked.connect(lambda: thred(next()))
    nekst.setStyleSheet("background-color: #283747; border-radius: 10px;")
    # fetch
    but = RoundedButton('')
    but.clicked.connect(lambda: print(text.text()))
    but.setFixedHeight(25)

    # the widgets
    sidebar = QVBoxLayout()  # vertical box layout
    image = QVBoxLayout()
    fetchbar = QHBoxLayout()
    # nav = QHBoxLayout
    masterLay = QHBoxLayout()  # master layout (put other layouts in here), Horizontal box layout
    masterMasterLay = QVBoxLayout()
    # ------------------------------------------------------------------------------------------------------------------

    # image placeholder
    image_label = getImg(
        'https://imgs.search.brave.com/2mXF0TjkMLnhUVj_SKlv4p0eHrNK-wrkDjvAkkph4Mk/rs:fit:800:600:1/g:ce/aHR0cDovL2dpZmlt/YWdlLm5ldC93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxNy8wMi9M/b2FkaW5nLUdJRi1J/bWFnZS0yLmdpZg.gif'
    )
    image_label.setStyleSheet("border-radius: 10px;")

    # sidebar
    buttList = button_list(image_label)
    for i in buttList:
        sidebar.addWidget(buttList[i])

    sidebar.setAlignment(Qt.AlignTop)

    # sidebar.addWidget(text)
    diag = widg()
    sidebar.addLayout(diag.layout)

    # fetch bar
    text = textbox.NewText()
    text.setFixedSize(550, 25)
    fetchbar.addWidget(text)

    fetchbar.setAlignment(Qt.AlignLeft)
    fetchbar.addWidget(but)

    # adding image to layout
    image.addWidget(image_label)
    image.addLayout(fetchbar)  # fetchbar
    image.addStretch()
    # --------------------------------putting together the master layout------------------------------------------------
    sidebar.addLayout(fetchbar)
    sidebar.addLayout(fetchbar)
    masterLay.addLayout(sidebar)
    masterLay.addWidget(previ)  # prev button
    masterLay.addLayout(image)  # image
    masterLay.addWidget(nekst)  # next button
    masterLay.setAlignment(Qt.AlignHCenter)
    masterMasterLay.addLayout(masterLay)
    # ------------------------------------------------------------------------------------------------------------------

    palette = window.palette()
    palette.setColor(palette.Window,
                     QColor('#17202a'))  # set the titlebar color to dark blue, or at least it's supposed to
    window.setPalette(palette)

    window.setLayout(masterMasterLay)
    window.setStyleSheet("background-color: #17202a;")
    window.show()

app.exec_()
