import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from pyqtwindow import Ui_MainWindow

import tkinter as tk
from tkinter import ttk

class MainWindow(QMainWindow):
    print("oh main window")
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.btnStart.clicked.connect(self.buttonStartClicked)
        ui.btnNetworkTest.clicked.connect(self.buttonNetworkClicked)
        #ui.btnStop.clicked.connect(self.buttonStopClicked)

    def buttonStartClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def buttonNetworkClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())