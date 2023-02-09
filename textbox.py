from PyQt5.QtWidgets import QLineEdit


def NewText(x=''):
    text = QLineEdit(x)
    text.setStyleSheet("border-radius: 10px;background-color: #d5d8dc;")
    # text.setFixedSize(245, 115)
    print('generated textbox')
    return text
