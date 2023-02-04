from PyQt5.QtWidgets import QPushButton


class RoundedButton(QPushButton):
    def __init__(self, *args):
        super().__init__(*args)
        self.setFixedSize(245, 50)
        self.setStyleSheet("background-color: orange; border-radius: 10px;")


def button_list():
    button = RoundedButton("previous image")  # Qpushbutton is already a Qwidget,no need to redefine as Qwidget
    button1 = RoundedButton("next image")
    button2 = RoundedButton("send image")
    button3 = RoundedButton("send all images")

    spacer = RoundedButton()
    spacer.setFixedSize(250, 50)
    spacer.setStyleSheet("border-radius: 10px;background-color: #17202a;")

    lst = [button, button1, button2, spacer, button3]
    return lst
