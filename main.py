import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from toggle_button import ToggleButton


class Mainwindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)

        self.container = QFrame(self)
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container {background-color: #222}")
        self.layout = QGridLayout()

        self.toggle = ToggleButton()
        self.layout.addWidget(self.toggle)
        self.toggle.setMinimumHeight(60)
        self.toggle.setMaximumHeight(60)
        self.toggle.setMinimumWidth(180)
        self.toggle.setMaximumWidth(180)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    sys.exit(app.exec_())
