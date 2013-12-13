# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverconnection.ui'
#
# Created: Fri May 28 19:08:50 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_serverConnection(object):
    def setupUi(self, serverConnection):
        serverConnection.setObjectName("serverConnection")
        serverConnection.resize(302, 236)
        self.hboxlayout = QtGui.QHBoxLayout(serverConnection)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtGui.QLabel(serverConnection)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(serverConnection)
        self.lineEdit.setObjectName("lineEdit")
        self.gridlayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(serverConnection)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(serverConnection)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridlayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(serverConnection)
        self.checkBox.setObjectName("checkBox")
        self.gridlayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtGui.QDialogButtonBox(serverConnection)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.retranslateUi(serverConnection)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), serverConnection.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), serverConnection.reject)
        QtCore.QMetaObject.connectSlotsByName(serverConnection)

    def retranslateUi(self, serverConnection):
        serverConnection.setWindowTitle(QtGui.QApplication.translate("serverConnection", "Connessione", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("serverConnection", "Host:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("serverConnection", "localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("serverConnection", "Porta:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setInputMask(QtGui.QApplication.translate("serverConnection", "ddddd; ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("serverConnection", "1974", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("serverConnection", "Server locale", None, QtGui.QApplication.UnicodeUTF8))

