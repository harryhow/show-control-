import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from pyqtwindow import Ui_MainWindow
# Import needed modules from osc4py3
from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm
from osc4py3 import oscbuildparse

import tkinter as tk
from tkinter import ttk

# Parameters for a local UDP server, contacted by out own client.
IP = "127.0.0.1"
PORT = 12345



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnStart.clicked.connect(self.buttonStartClicked)
        self.ui.btnNetworkTest.clicked.connect(self.buttonNetworkClicked)
        self.ui.btnStop.clicked.connect(self.buttonStopClicked)

        self.send_play_count = 0

    def buttonStopClicked(self):

        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0, 200))
        self.ui.labelStatus.setAutoFillBackground(True)
        pe.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 0, 255, 180))
        # pe.setColor(QPalette.Background,Qt.blue)
        self.ui.labelStatus.setPalette(pe)
        self.ui.labelStatus.setFont(QtGui.QFont("", 22, QtGui.QFont.Bold))


        self.ui.labelStatus.setText(" The show is STOPPED !!! ")
        self.ui.btnStart.setText("ALL START")
        self.send_play_count = 0
        self.statusBar().showMessage("Play signals sending " + str(self.send_play_count) + " times")

    def buttonStartClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' pressed')

        # send out START command as a bundle
        msg1 = oscbuildparse.OSCMessage("/pc1/cmd/control/showison", None, ["1111"])
        msg2 = oscbuildparse.OSCMessage("/pc2/cmd/control/showison", None, ["1111"])
        msg3 = oscbuildparse.OSCMessage("/pc3/cmd/control/showison", None, ["1111"])
        msg4 = oscbuildparse.OSCMessage("/pc4/cmd/control/showison", None, ["1111"])

        bun = oscbuildparse.OSCBundle(
            oscbuildparse.OSC_IMMEDIATELY,
            [msg1, msg2, msg3, msg4])

        osc_send(bun, "oscclient")

        # Send osc to start
        # msg = oscbuildparse.OSCMessage("/pc1/cmd/control/showison", None, ["1111"])
        # osc_send(msg, "oscclient")
        osc_process()

        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, QtGui.QColor(255, 0, 0, 200))
        self.ui.labelStatus.setAutoFillBackground(True)
        pe.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 0, 255, 180))
        # pe.setColor(QPalette.Background,Qt.blue)
        self.ui.labelStatus.setPalette(pe)
        self.ui.labelStatus.setFont(QtGui.QFont("", 22, QtGui.QFont.Bold))

        self.ui.labelStatus.setText(" The show is PLAYING !!! ")
        self.ui.btnStart.setText("Send PLAY signal again ...")
        self.send_play_count =  self.send_play_count + 1
        self.statusBar().showMessage("Play signals sending " + str(self.send_play_count) + " times")

    def buttonNetworkClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' pressed')

        #
        msg = oscbuildparse.OSCMessage("/test/here", ",si", ["message", 1])
        osc_send(msg, "oscclient")
        osc_process()

def oscInit():
    # Start the system.
    osc_startup()
    # Make client channels to send packets.
    osc_udp_client(IP, PORT, "oscclient")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    oscInit()
    sys.exit(app.exec_())