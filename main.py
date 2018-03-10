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
IP = "192.168.1.255"
PORT = 12688


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnStart.clicked.connect(self.buttonStartClicked)
        self.ui.btnNetworkTest.clicked.connect(self.buttonNetworkClicked)
        self.ui.btnStop.clicked.connect(self.buttonStopClicked)
        ip_status = 'IP: '
        self.ui.labelIPAddress.setText(ip_status + getIpAddress())

        self.send_play_count = 0
        self.isReady = False

    # This is for READY button
    def buttonStopClicked(self):

        if self.isReady == True:
            self.isReady = False
            self.ui.btnStop.setEnabled(False);
        else:
            self.isReady = True
            self.ui.btnStop.setEnabled(True);


            # send out READY command as a bundle
            msg1 = oscbuildparse.OSCMessage("/pc1/cmd/control/showison", None, [6666])
            msg2 = oscbuildparse.OSCMessage("/pc2/cmd/control/showison", None, [6666])
            msg3 = oscbuildparse.OSCMessage("/pc3/cmd/control/showison", None, [6666])
            msg4 = oscbuildparse.OSCMessage("/pc4/cmd/control/showison", None, [6666])
            msg5 = oscbuildparse.OSCMessage("/pc5/cmd/control/showison", None, [6666])
            msg6 = oscbuildparse.OSCMessage("/pc6/cmd/control/showison", None, [6666])

            bun = oscbuildparse.OSCBundle(
                oscbuildparse.OSC_IMMEDIATELY,
                [msg1, msg2, msg3, msg4, msg5, msg6])

            osc_send(bun, "oscclient")
            osc_process()


            pe = QtGui.QPalette()
            pe.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0, 200))
            self.ui.labelStatus.setAutoFillBackground(True)
            pe.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 0, 255, 180))
            # pe.setColor(QPalette.Background,Qt.blue)
            self.ui.labelStatus.setPalette(pe)
            self.ui.labelStatus.setFont(QtGui.QFont("", 22, QtGui.QFont.Bold))


            self.ui.labelStatus.setText(" The show is READY !!! ")
            self.ui.btnStart.setText("ALL START")
            self.send_play_count = 0
            self.statusBar().showMessage("Play signals sending " + str(self.send_play_count) + " times")

            self.isReady = True
            self.ui.btnStop.setEnabled(False);


    def buttonStartClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' pressed')

        if self.isReady == False:
            pe = QtGui.QPalette()
            pe.setColor(QtGui.QPalette.WindowText, QtGui.QColor(255, 0, 0, 200))
            self.ui.labelStatus.setAutoFillBackground(True)
            pe.setColor(QtGui.QPalette.Window, QtGui.QColor(0, 0, 255, 180))
            # pe.setColor(QPalette.Background,Qt.blue)
            self.ui.labelStatus.setPalette(pe)
            self.ui.labelStatus.setFont(QtGui.QFont("", 22, QtGui.QFont.Bold))
            self.ui.labelStatus.setText(" Hit READY before start !!! ")
            return



        # send out START command as a bundle
        msg1 = oscbuildparse.OSCMessage("/pc1/cmd/control/showison", None, [1111])
        msg2 = oscbuildparse.OSCMessage("/pc2/cmd/control/showison", None, [1111])
        msg3 = oscbuildparse.OSCMessage("/pc3/cmd/control/showison", None, [1111])
        msg4 = oscbuildparse.OSCMessage("/pc4/cmd/control/showison", None, [1111])
        msg5 = oscbuildparse.OSCMessage("/pc5/cmd/control/showison", None, [1111])
        msg6 = oscbuildparse.OSCMessage("/pc6/cmd/control/showison", None, [1111])

        bun = oscbuildparse.OSCBundle(
            oscbuildparse.OSC_IMMEDIATELY,
            [msg1, msg2, msg3, msg4, msg5, msg6])

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

        # jus in case
        osc_send(bun, "oscclient")
        osc_process()

    def buttonNetworkClicked(self):
        def handlerfunction(x):
            print("get cmd: " + x)

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' pressed')

        #
        # send out START command as a bundle
        msg1 = oscbuildparse.OSCMessage("/pc1/cmd/control/ruthere", None, ["1111"])
        msg2 = oscbuildparse.OSCMessage("/pc2/cmd/control/ruthere", None, ["1111"])
        msg3 = oscbuildparse.OSCMessage("/pc3/cmd/control/ruthere", None, ["1111"])
        msg4 = oscbuildparse.OSCMessage("/pc4/cmd/control/ruthere", None, ["1111"])

        bun = oscbuildparse.OSCBundle(
            oscbuildparse.OSC_IMMEDIATELY,
            [msg1, msg2, msg3, msg4])

        osc_send(bun, "oscclient")

        # receive echo back
        osc_process()

        osc_method("/pc1/cmd/control/ruthere", handlerfunction)

        osc_process()


def oscInit():

    # def handlerfunction(x):
    #     print("get cmd: " + x)

    # Start the system.
    osc_startup()
    # Make client channels to send packets.
    osc_udp_client(IP, PORT, "oscclient")

    # Associate Python functions with message address patterns, using default
    # argument scheme OSCARG_DATAUNPACK.
    # osc_method("/pc1/cmd/control/ruthere", handlerfunction)

    # finished = False
    # while not finished:
    #     # …
    #     osc_process()
    #     # …
    # #
    # # # Properly close the system.
    # # osc_terminate()


def getIpAddress():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def handlerFunction(s):
    print("got echo back i'm alive: "+s)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    oscInit()
    sys.exit(app.exec_())