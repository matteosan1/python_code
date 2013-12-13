# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Nov  5 00:18:14 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtGui.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        self.menuInsert = QtGui.QMenu(self.menubar)
        self.menuInsert.setObjectName("menuInsert")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnection = QtGui.QAction(MainWindow)
        self.actionConnection.setObjectName("actionConnection")
        self.actionInsert_Product = QtGui.QAction(MainWindow)
        self.actionInsert_Product.setObjectName("actionInsert_Product")
        self.actionInsert_Object = QtGui.QAction(MainWindow)
        self.actionInsert_Object.setObjectName("actionInsert_Object")
        self.actionInsert_Problem = QtGui.QAction(MainWindow)
        self.actionInsert_Problem.setObjectName("actionInsert_Problem")
        self.menuOpen.addAction(self.actionConnection)
        self.menuInsert.addAction(self.actionInsert_Product)
        self.menuInsert.addAction(self.actionInsert_Object)
        self.menuInsert.addAction(self.actionInsert_Problem)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuInsert.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Force 10 DB", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Component:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpen.setTitle(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInsert.setTitle(QtGui.QApplication.translate("MainWindow", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnection.setText(QtGui.QApplication.translate("MainWindow", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_Product.setText(QtGui.QApplication.translate("MainWindow", "Insert Product", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_Object.setText(QtGui.QApplication.translate("MainWindow", "Insert Object", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsert_Problem.setText(QtGui.QApplication.translate("MainWindow", "Insert Problem", None, QtGui.QApplication.UnicodeUTF8))

