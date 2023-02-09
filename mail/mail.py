import os

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QCalendarWidget, QLabel, QComboBox,QSizePolicy
from buttons import RoundedButton


def send_mail(recipient,subject,body):
    import ezgmail
    ezgmail.init()
    ezgmail.send(recipient, subject, body)
    print('sent mail')

class widg():
    def __init__(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignLeft)
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignBottom)
        self.mail_button = RoundedButton("c'est un button")
        self.layout.addWidget(self.mail_button)

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('mail')
    widg = widg()
    widg.mail_button.clicked.connect(lambda: send_mail('mesinodd@gmail.com','test mail pt 2','bip bop boop'))
    window.setLayout(widg.layout)
    window.show()
    app.exec_()