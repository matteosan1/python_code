# -*- coding: utf-8 -*-
# AZzERA LE COMBO DELLA MOSSA

from PyQt4 import QtGui, QtCore
from ui_mainwindow import Ui_MainWindow
#from sceltapalio import SceltaPalio

contrade = ("Aquila", "Bruco", "Chiocciola", "Civetta", "Drago",
"Giraffa", "Istrice", "Leocorno", "Lupa", "Nicchio", "Oca", "Onda",
"Pantera", "Selva", "Tartuca", "Torre", "Montone", "---------")

class PalioMainWindow(QtGui.QMainWindow):
  
  def __init__(self, db):
    QtGui.QMainWindow.__init__(self)
    self.ui = Ui_MainWindow()
    self.ind_product = []
    self.ui.setupUi(self)
    self.db = db
    self.cur = db.cursor()
    self.r = []
    self.indice = int()
    self.vittoria = ()
    self.comparsa = ()
    self.mossa = ()
    self.queryPalio()
    self.graphicScene = QtGui.QGraphicsScene()
    self.graphicsView = QtGui.QGraphicsView(self.graphicScene, self.ui.tabPalio)
    self.graphicsView.setGeometry(QtCore.QRect(710, 10, 120, 380))
    self.graphicsView.setObjectName("graphicsView")    
    self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    #QtCore.QObject.connect(self.ui.actionModifica, QtCore.SIGNAL('triggered()'), self.sceltaPalio)
    QtCore.QObject.connect(self.ui.tableWidget, QtCore.SIGNAL('cellChanged(int, int)'), self.newTableLine)
    #QtCore.QObject.connect(self.ui.lineEdit_12, QtCore.SIGNAL('editingFinished()'), self.queryPalio)
    QtCore.QObject.connect(self.ui.comboBox_5, QtCore.SIGNAL('currentIndexChanged(int)'), self.sceltaPalio)
    QtCore.QObject.connect(self.ui.buttonAggiorna, QtCore.SIGNAL('pressed()'), self.aggiorna)
    QtCore.QObject.connect(self.ui.buttonNuovo, QtCore.SIGNAL('pressed()'), self.nuovoPalio)
    QtCore.QObject.connect(self.ui.aggiungiMonturato, QtCore.SIGNAL('pressed()'), self.nuovoMonturato)
    QtCore.QObject.connect(self.ui.eliminaMonturato, QtCore.SIGNAL('pressed()'), self.togliMonturato)
    
  def nuovoPalio(self):
    self.cur.execute("select indice from vittorie order by indice desc limit 1")
    last_index = (self.cur.fetchall())[0][0] + 1
    self.cur.execute("insert into vittorie set indice = %s",(last_index))
    for i in range(1,11):
      self.cur.execute("insert into mosse set indice = %s, estrazione=%s, contrada=17",(last_index, str(i)))
      
    self.db.commit()
    msgBox = QtGui.QMessageBox.information(self.ui.tab, "Aggiornamento DB.", "Un nuovo Palio e` stato inserito.")
    self.queryPalio()
    i = [o[1] for o in self.r].index(last_index)
    self.sceltaPalio(i)
    
  def nuovoMonturato(self):
    self.ui.listWidget.addItem("")
    rows = self.ui.listWidget.count()
    item = self.ui.listWidget.item(rows-1)
    item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
    
  def togliMonturato(self):  
    items = self.ui.listWidget.selectedItems()
    for i in items:
      self.ui.listWidget.takeItem(self.ui.listWidget.row(i))
    
  def aggiorna(self):
    # aggiorna Palio
    query = "update vittorie set data=%s, primo=%s, secondo=%s, tempo=%s, pittore=%s, dedica=%s, note=%s, numero_unico=%s, mossiere=%s, libreria=%s where indice=%s"
    self.cur.execute(query, (str(self.ui.dateEdit.date().toString(QtCore.Qt.ISODate)),
    self.ui.comboBox.currentIndex(),
    self.ui.comboBox_2.currentIndex(),
    self.ui.lineEdit_11.text(),
    self.ui.lineEdit.text(),
    self.ui.lineEdit_2.text(),
    self.ui.textEdit.toPlainText(),
    self.ui.lineEdit_4.text(),
    self.ui.lineEdit_3.text(), 
    self.ui.checkBox.checkState(),
    self.r[self.indice][1]))
    
    # aggiorna comparsa
    self.cur.execute("delete from comparse where indice=%s",(self.r[self.indice][1]))
    for i in range(0, self.ui.listWidget.count()):
      item = self.ui.listWidget.item(i)
      line = item.text().split(": ")
      self.cur.execute("insert into comparse set ruolo=%s, nome=%s, indice=%s", (line[0], line[1], self.r[self.indice][1]))
      
    # aggiorna mossa
    for j in range(0,10):
      i = j
      query = "update mosse set orecchio=%s, assegnazione=%s, contrada=%s, cavallo=%s, fantino=%s, mossa=%s, capitano=%s, note=%s, caduta=%s, chi_estrae=%s where indice=%s and estrazione=%s"
      self.cur.execute(query, (self.ui.spinBox_2[j].value(),
      self.ui.spinBox[j].value(),
      self.ui.comboBox_3[j].currentIndex(),
      self.ui.lineEdit_6[j].text(),
      self.ui.lineEdit_7[j].text(),
      self.ui.lineEdit_10[j].text(),
      self.ui.lineEdit_5[j].text(),
      self.ui.lineEdit_9[j].text(),
      self.ui.lineEdit_8[j].text(),
      self.ui.comboBox_4[j].currentIndex(),
      self.r[self.indice][1], str(i+1)))
          
    self.db.commit()
    msgBox = QtGui.QMessageBox.information(self.ui.tab, "Aggiornamento DB.", "Il DB e` stato aggiornato.")
    
  def queryPalio(self):
    cursor = self.db.cursor()
    cursor.execute("select data, indice from vittorie")
    self.r = cursor.fetchall()
    self.ui.comboBox_5.clear()
    for i in self.r:
      self.ui.comboBox_5.addItem(str(i[0]))
	
  def sceltaPalio(self, i):
    self.indice = i
    ind = self.r[i][1]
    self.populate_palio(ind)
    self.populate_comparsa(ind)
    self.populate_mossa(ind)
    self.drappellone(self.r[i][0])
    
  def drappellone(self, data):
    self.cur.execute("select primo from vittorie where data=%s",(data))
    result = self.cur.fetchall()
    if (len(result) > 1):
      print "PROBLEMINO"
      return
    
    self.graphicScene.clear()
    contrada_vincente = contrade[result[0][0]].lower()
    nuova_data = str(data.day)+"."+str(data.month)+"."+str(data.year)[1:4]
    nomefile = "/home/sani/Documents/Palio/fotografie/drappelloni/"+contrada_vincente+"/d"+contrada_vincente[0:3]+nuova_data+".gif"
    if (not QtCore.QFile.exists(nomefile)):
      nomefile = "/home/sani/Documents/Palio/fotografie/drappelloni/palio_non_disponibile.gif"
    pixMap = QtGui.QPixmap(nomefile)
    self.graphicScene.addPixmap(pixMap)
    self.ui.graphicsView.show()
    
  def populate_palio(self, indice):
    self.cur.execute("select * from vittorie where indice = %s", (indice))
    self.vittoria = self.cur.fetchall()
    result = self.vittoria
    if (len(result) > 1):
      print "PROBLEMINO"
    else:  
      self.ui.dateEdit.setDate(result[0][0]) #data
      self.ui.comboBox.addItems(contrade)
      if (result[0][2] is not None):
	self.ui.comboBox.setCurrentIndex(result[0][2]) #primo
      else:
	self.ui.comboBox_2.setCurrentIndex(17) #secondo
	  
      self.ui.comboBox_2.addItems(contrade)
      if (result[0][3] is not None):
	self.ui.comboBox_2.setCurrentIndex(result[0][3]) #secondo
      else:
	self.ui.comboBox_2.setCurrentIndex(17) #secondo
	
      if (result[0][5] is not None):
	self.ui.lineEdit.setText(result[0][5]) #pittore
      else:
	self.ui.lineEdit.setText("") #dedica
	  
      if (result[0][6] is not None):
	self.ui.lineEdit_2.setText(result[0][6]) #dedica
      else:
	self.ui.lineEdit_2.setText("") #dedica
	
      if (result[0][4] is not None):
	self.ui.lineEdit_11.setText(result[0][4]) #tempo
      else:
	self.ui.lineEdit_11.setText("0:00.00") #tempo
      
      if (result[0][8] is not None):
        self.ui.lineEdit_4.setText(str(result[0][8])) #numero unico
      else:
	self.ui.lineEdit_4.setText("")

      if (result[0][9] is not None):
	self.ui.lineEdit_3.setText(str(result[0][9])) #mossiere 
      else:
	self.ui.lineEdit_3.setText("")
	
      if (result[0][7] is not None):
	self.ui.textEdit.setText(result[0][7]) # note
      else:
	self.ui.textEdit.setText("")
	
      if (result[0][10] is not None):	
	self.ui.checkBox.setCheckState(int(result[0][10])) # libreria
      else:
	self.ui.checkBox.setCheckState(QtCore.Qt.Unchecked)
  
  def populate_mossa(self, indice):
    self.cur.execute("select * from mosse where indice = %s order by estrazione", (indice))
    result = self.cur.fetchall()
    if (len(result) > 10):
      print "PROBLEMINO"
      return
    for j,i in enumerate(result):  
      self.ui.spinBox[j].setValue(i[2]) # assegnazione
      self.ui.spinBox_2[j].setValue(i[4]) # orecchio
      self.ui.lineEdit_10[j].setText(i[8]) # mossa
      self.ui.comboBox_3[j].addItems(contrade)
      self.ui.comboBox_3[j].setCurrentIndex(i[5]) # contrada
      self.ui.lineEdit_6[j].setText(i[6]) # cavallo
      self.ui.lineEdit_7[j].setText(i[7]) # fantino
      self.ui.lineEdit_8[j].setText(str(i[10])) # cadute
      self.ui.comboBox_4[j].addItems(contrade)
      if (i[12] is not None):
	self.ui.comboBox_4[j].setCurrentIndex(i[12]) # estratta da
      else:
	self.ui.comboBox_4[j].setCurrentIndex(17)
      
      if (i[9] is not None):
	self.ui.lineEdit_5[j].setText(i[9]) # capitano
      else:
	self.ui.lineEdit_5[j].setText("")
	
      if (i[11] is not None):
	self.ui.lineEdit_9[j].setText(str(i[11])) # note
      else:
	self.ui.lineEdit_9[j].setText("")
    
  def populate_comparsa(self, indice):
    self.ui.listWidget.clear()
    self.cur.execute("select * from comparse where indice = %s order by nome", (indice))
    result = self.cur.fetchall()
    if (len(result) < 1):
      return
    ordine_comparsa = ("Tamburino", "Alfiere", "Duce", "Uomo d'Arme", "Figurin Maggiore",
    "Paggio Porta Insegna", "Palafreniere", "Soprallasso", "Barbaresco",
    "Vessillifero", "Popolo")
    j=0
    while j < len(ordine_comparsa):
      for i in result:
	if (i[0] == ordine_comparsa[j]):
	  self.ui.listWidget.addItem(i[0]+": " + i[1])
	  rows = self.ui.listWidget.count()
	  item = self.ui.listWidget.item(rows-1)
	  item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)	  
      j = j+1
     
  def newTableLine(self, row, col):
    if (col != 0):
      return
    item = QtGui.QTableWidgetItem(self.ui.tableWidget.currentItem())
    text = item.text() # modificare per ricerca piu` generica
    if (text == ""):
      return
    self.cur.execute("select vittorie.primo=mosse.contrada, data,contrada from mosse,vittorie where cavallo=%s and mosse.indice = vittorie.indice",(text))
    result = self.cur.fetchall()
    if (len(result) is not 0):
      self.ui.tableWidget.item(row, 1).setText(str(len(result)))
    else:
      self.ui.tableWidget.item(row, 1).setText("0")
      self.ui.tableWidget.item(row, 2).setText("0")
            
    if (row == self.ui.tableWidget.rowCount()-1):
      self.ui.tableWidget.setRowCount(row+2)
      for i in range(0,4):
	new_item = QtGui.QTableWidgetItem()
	self.ui.tableWidget.setItem(row, i, new_item)
