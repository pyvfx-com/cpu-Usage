import sys
import os

from PySide2 import QtCore
from PySide2.QtWidgets import *
from datetime import datetime
from ui.usage import Ui_Form
from utils import __utils as utl

date = datetime.now()
month = date.strftime("%B")
year = date.strftime("%Y")
username = os.getlogin()


class main_usage(Ui_Form, QWidget):
    def __init__(self):
        super(main_usage, self).__init__()
        self.setupUi(self)
        self.ThreadClass = worker()
        self.ThreadClass.start()

        self.ThreadClass.progress.connect(self.update_ui)

    def update_ui(self, valC, valR, valN):
        self.progressBar_CPU.setValue(valC)
        self.progressBar_RAM.setValue(valR)
        self.progressBar_NETWORK.setValue(valN)


class worker(QtCore.QThread):
    progress = QtCore.Signal(int, int, int)

    def run(self):
        """ Long-running Task Please do carefully.
        """
        while True:
            valCPU = int(utl.getCPU())
            valRAM = int(utl.getRAM())
            valNet = int(utl.getNET())

            self.progress.emit(valCPU, valRAM, valNet)


# For widgets
if __name__ == '__main__':
    app = QApplication()
    widgets = main_usage()
    widgets.show()
    sys.exit(app.exec_())
