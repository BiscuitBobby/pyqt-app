from PyQt5.QtWidgets import QPushButton
from demoData import next, prev

class RoundedButton(QPushButton):
    def __init__(self, *args):
        super().__init__(*args)
        self.setFixedSize(245, 50)
        self.setStyleSheet("background-color: orange; border-radius: 10px;")


def button_list(img):  # img is the image widget
    button = RoundedButton("previous image")  # Qpushbutton is already a Qwidget,no need to redefine as Qwidget
    button.clicked.connect(lambda: prev(img))
    button1 = RoundedButton("next image")
    button1.clicked.connect(lambda: next(img))
    button2 = RoundedButton("send image")
    button3 = RoundedButton("send all images")
    spacer = RoundedButton()
    spacer.setFixedSize(250, 25)
    spacer.setStyleSheet("border-radius: 10px;background-color: #17202a;")

    lst = [button, button1, button2, spacer, button3]
    return lst

