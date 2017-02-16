# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.chatDisplayText = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.chatDisplayText.setGeometry(QtCore.QRect(10, 10, 581, 381))
        self.chatDisplayText.setObjectName("chatDisplayText")
        self.chatSendText = QtWidgets.QTextEdit(self.centralWidget)
        self.chatSendText.setGeometry(QtCore.QRect(10, 400, 511, 31))
        self.chatSendText.setObjectName("chatSendText")
        self.btnSend = QtWidgets.QPushButton(self.centralWidget)
        self.btnSend.setGeometry(QtCore.QRect(530, 400, 61, 31))
        self.btnSend.setObjectName("btnSend")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuOlof_Chat_Client = QtWidgets.QMenu(self.menuBar)
        self.menuOlof_Chat_Client.setObjectName("menuOlof_Chat_Client")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuOlof_Chat_Client.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSend.setText(_translate("MainWindow", "Send"))
        self.menuOlof_Chat_Client.setTitle(_translate("MainWindow", "Olof Chat Client"))

