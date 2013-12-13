# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui_sceltapalio import Ui_SceltaPalio
  
class SceltaPalio(QtGui.QDialog):
  def __init__(self, db):
    QtGui.QDialog.__init__(self)
    self.ui = Ui_SceltaPalio()
    self.ui.setupUi(self)
    self.db = db
    self.r = ()
    QtCore.QObject.connect(self.ui.lineEdit, QtCore.SIGNAL('editingFinished()'), self.queryPalio)
 
  def queryPalio(self):
    cursor = self.db.cursor()
    cursor.execute("select data, indice from vittorie where year(data)=%s",(self.ui.lineEdit.text()))
    self.r = cursor.fetchall()
    self.ui.comboBox.clear()
    for i in self.r:
      self.ui.comboBox.addItem(str(i[0]))
    