# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/harryhow/Documents/000__MyProject/Project_VR_MotionCapture/AGT_ShowControl/ShowRoomControl/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        print("set ui !!")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 548)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btnStart = QtWidgets.QPushButton(self.centralWidget)
        self.btnStart.setGeometry(QtCore.QRect(90, 180, 651, 141))
        self.btnStart.setObjectName("btnStart")
        self.btnNetworkTest = QtWidgets.QPushButton(self.centralWidget)
        self.btnNetworkTest.setGeometry(QtCore.QRect(610, 370, 131, 61))
        self.btnNetworkTest.setAutoDefault(False)
        self.btnNetworkTest.setDefault(False)
        self.btnNetworkTest.setFlat(False)
        self.btnNetworkTest.setObjectName("btnNetworkTest")
        self.labelPCName = QtWidgets.QLabel(self.centralWidget)
        self.labelPCName.setGeometry(QtCore.QRect(100, 50, 101, 31))
        self.labelPCName.setObjectName("labelPCName")
        self.labelIPAddress = QtWidgets.QLabel(self.centralWidget)
        self.labelIPAddress.setGeometry(QtCore.QRect(240, 50, 141, 31))
        self.labelIPAddress.setObjectName("labelIPAddress")
        self.btnStop = QtWidgets.QPushButton(self.centralWidget)
        self.btnStop.setGeometry(QtCore.QRect(610, 440, 131, 41))
        self.btnStop.setObjectName("btnStop")
        self.labelStatus = QtWidgets.QLabel(self.centralWidget)
        self.labelStatus.setGeometry(QtCore.QRect(100, 106, 300, 31))
        self.labelStatus.setObjectName("labelStatus")
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(100, 330, 87, 20))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 330, 87, 20))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_3.setGeometry(QtCore.QRect(220, 330, 87, 20))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_4.setGeometry(QtCore.QRect(280, 330, 87, 20))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show Control"))
        self.btnStart.setText(_translate("MainWindow", "ALL START"))
        self.btnNetworkTest.setText(_translate("MainWindow", "Network Test"))
        self.labelPCName.setText(_translate("MainWindow", "PC: ______________"))
        self.labelIPAddress.setText(_translate("MainWindow", "IP: ___ . ____ . ____. ___"))
        self.btnStop.setText(_translate("MainWindow", "Stop!"))
        self.labelStatus.setText(_translate("MainWindow", "STATUS: "))
        self.checkBox.setText(_translate("MainWindow", "PC1"))
        self.checkBox_2.setText(_translate("MainWindow", "PC2"))
        self.checkBox_3.setText(_translate("MainWindow", "PC3"))
        self.checkBox_4.setText(_translate("MainWindow", "PC4"))