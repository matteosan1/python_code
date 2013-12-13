# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aggiornaVoti.ui'
#
# Created: Sat Feb 11 18:34:12 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AggiornaVoti(object):
    def setupUi(self, AggiornaVoti):
        AggiornaVoti.setObjectName(_fromUtf8("AggiornaVoti"))
        AggiornaVoti.resize(400, 300)
        AggiornaVoti.setWindowTitle(QtGui.QApplication.translate("AggiornaVoti", "Aggiorna Voto", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(AggiornaVoti)
        self.label.setGeometry(QtCore.QRect(30, 30, 70, 17))
        self.label.setText(QtGui.QApplication.translate("AggiornaVoti", "Giornata", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.labelGiornata = QtGui.QLabel(AggiornaVoti)
        self.labelGiornata.setGeometry(QtCore.QRect(120, 30, 70, 17))
        self.labelGiornata.setText(QtGui.QApplication.translate("AggiornaVoti", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelGiornata.setObjectName(_fromUtf8("labelGiornata"))
        self.label_3 = QtGui.QLabel(AggiornaVoti)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 70, 17))
        self.label_3.setText(QtGui.QApplication.translate("AggiornaVoti", "Giocatore", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.labelGiocatore = QtGui.QLabel(AggiornaVoti)
        self.labelGiocatore.setGeometry(QtCore.QRect(120, 60, 211, 17))
        self.labelGiocatore.setText(QtGui.QApplication.translate("AggiornaVoti", "Giocatore", None, QtGui.QApplication.UnicodeUTF8))
        self.labelGiocatore.setObjectName(_fromUtf8("labelGiocatore"))
        self.doubleSpinBoxVoto = QtGui.QDoubleSpinBox(AggiornaVoti)
        self.doubleSpinBoxVoto.setGeometry(QtCore.QRect(110, 94, 56, 25))
        self.doubleSpinBoxVoto.setDecimals(1)
        self.doubleSpinBoxVoto.setSingleStep(0.5)
        self.doubleSpinBoxVoto.setObjectName(_fromUtf8("doubleSpinBoxVoto"))
        self.label_5 = QtGui.QLabel(AggiornaVoti)
        self.label_5.setGeometry(QtCore.QRect(30, 100, 70, 17))
        self.label_5.setText(QtGui.QApplication.translate("AggiornaVoti", "Voto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox = QtGui.QGroupBox(AggiornaVoti)
        self.groupBox.setGeometry(QtCore.QRect(30, 140, 141, 111))
        self.groupBox.setTitle(QtGui.QApplication.translate("AggiornaVoti", "Cartellini", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.radioButton.setText(QtGui.QApplication.translate("AggiornaVoti", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 111, 21))
        self.radioButton_2.setText(QtGui.QApplication.translate("AggiornaVoti", "Ammonito", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.radioButton_3.setText(QtGui.QApplication.translate("AggiornaVoti", "Espulso", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.spinBoxGoal = QtGui.QSpinBox(AggiornaVoti)
        self.spinBoxGoal.setGeometry(QtCore.QRect(320, 114, 56, 25))
        self.spinBoxGoal.setObjectName(_fromUtf8("spinBoxGoal"))
        self.label_6 = QtGui.QLabel(AggiornaVoti)
        self.label_6.setGeometry(QtCore.QRect(210, 120, 70, 17))
        self.label_6.setText(QtGui.QApplication.translate("AggiornaVoti", "Goal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.spinBoxRigoriSe = QtGui.QSpinBox(AggiornaVoti)
        self.spinBoxRigoriSe.setGeometry(QtCore.QRect(320, 140, 56, 25))
        self.spinBoxRigoriSe.setObjectName(_fromUtf8("spinBoxRigoriSe"))
        self.label_7 = QtGui.QLabel(AggiornaVoti)
        self.label_7.setGeometry(QtCore.QRect(210, 146, 101, 16))
        self.label_7.setText(QtGui.QApplication.translate("AggiornaVoti", "Rigori Segnati", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.spinBoxRigoriSb = QtGui.QSpinBox(AggiornaVoti)
        self.spinBoxRigoriSb.setGeometry(QtCore.QRect(320, 164, 56, 25))
        self.spinBoxRigoriSb.setObjectName(_fromUtf8("spinBoxRigoriSb"))
        self.label_8 = QtGui.QLabel(AggiornaVoti)
        self.label_8.setGeometry(QtCore.QRect(210, 170, 101, 17))
        self.label_8.setText(QtGui.QApplication.translate("AggiornaVoti", "Rigori Sbagliati", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(AggiornaVoti)
        self.label_9.setGeometry(QtCore.QRect(210, 196, 81, 17))
        self.label_9.setText(QtGui.QApplication.translate("AggiornaVoti", "Autogoal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.spinBoxAutogoal = QtGui.QSpinBox(AggiornaVoti)
        self.spinBoxAutogoal.setGeometry(QtCore.QRect(320, 190, 56, 25))
        self.spinBoxAutogoal.setObjectName(_fromUtf8("spinBoxAutogoal"))
        self.buttonBox = QtGui.QDialogButtonBox(AggiornaVoti)
        self.buttonBox.setGeometry(QtCore.QRect(200, 250, 170, 26))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(AggiornaVoti)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AggiornaVoti.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AggiornaVoti.reject)
        QtCore.QMetaObject.connectSlotsByName(AggiornaVoti)

    def retranslateUi(self, AggiornaVoti):
        pass

