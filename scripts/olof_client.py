#!/usr/bin/env python

import rospy
from chat_server.msg import Message
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
import sys
import design
import time

new_messages = list()


def callback(data):

    print(data.sender, data.message)


class ChatApplication(QtWidgets.QMainWindow, design.Ui_MainWindow):

    callback_signal = pyqtSignal()

    def __init__(self):

        rospy.init_node('olof_client')
        pub = rospy.Publisher('chat_in', Message, queue_size=10)
        rospy.Subscriber('chat_out', Message, callback)

        # PyQt
        super(ChatApplication, self).__init__()
        self.setupUi(self)

        # ROS
        self.btnSend.clicked.connect(lambda: self.send_message(pub))

    def send_message(self, pub):
        pub.publish("Olof", self.chatSendText.toPlainText())
        self.chatDisplayText.appendPlainText("olof: " + self.chatSendText.toPlainText())

    def print_message(self, message):
        self.chatDisplayText.appendPlainText(message)


class UpdateMessagesThread(QThread):

    update = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        time.sleep(0.1)
        self.update.em


def run_client():

    app = QtWidgets.QApplication(sys.argv)
    form = ChatApplication()
    form.show()
    app.exec_()


if __name__ == "__main__":
    try:
        run_client()
    except rospy.ROSInterruptException:
        pass

