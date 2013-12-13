from PyQt4 import QtGui, QtCore 
from force_10_main import Ui_MainWindow
from insert_product import InsertProduct
from insert_object import InsertObject
from show_problem import ShowProblems
from insert_problem import InsertProblem

class MainDialog(QtGui.QMainWindow):
    def __init__(self, db):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ind_product = []
        self.ui.setupUi(self)
        self.cursor = db.cursor()
        self.init_combo()
        self.init_table()
        self.populate_table(0)
        self.ui.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows);
        self.ui.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers);

        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.populate_table)
        QtCore.QObject.connect(self.ui.actionInsert_Product, QtCore.SIGNAL('triggered()'), self.insert_product)
        QtCore.QObject.connect(self.ui.actionInsert_Object, QtCore.SIGNAL('triggered()'), self.insert_object)
        QtCore.QObject.connect(self.ui.actionInsert_Problem, QtCore.SIGNAL('triggered()'), self.insert_problem)
        QtCore.QObject.connect(self.ui.tableWidget, QtCore.SIGNAL("cellDoubleClicked(int, int)"), self.see_problem)

    def see_problem(self, row, column):
        self.type = self.ind_product[self.ui.comboBox.currentIndex()][0]
        self.cursor.execute("select ind from objects where type = " + str(self.type) + 
                            " order by serial_number limit "+ str(row) + ", 1")
        self.result = self.cursor.fetchall()
        self.cursor.execute("select problem_date, problem, objects.serial_number from objects, problems where object_ref = " + str(self.result[0][0]) + " and mother_ref = objects.ind order by problem_date;") 
        self.d = ShowProblems()
        self.d.populate_table(self.cursor.fetchall())
        self.d.exec_()
        
    def insert_problem(self):
        self.cursor.execute("select ind, serial_number from objects order by ind")
        self.r1 = self.cursor.fetchall()
        self.cursor.execute("select ind, serial_number from objects where type =5 or type = 10 or type = 9 order by type, ind")
        self.r2 = self.cursor.fetchall()
        self.d = InsertProblem(self.r1, self.r2)
        self.ok = self.d.exec_()
        if (self.ok):
            self.text = self.d.text()
            self.index1 = self.r1[self.text[0]][0]
            self.index2 = self.r2[self.text[1]][0]

            self.cursor.execute("insert into problems (problem, problem_date, mother_ref, object_ref) VALUES ('" + str(self.text[3]) + "', '" + str(self.text[2]) + "', '" + str(self.index2) + "', '" + str(self.index1) + "');")
            
    def insert_object(self):
        self.d = InsertObject(self.ind_product)

        self.ok = self.d.exec_()
        if (self.ok):
            self.text = self.d.text()
            self.cursor.execute("insert into objects (revision, serial_number, shipment, type) VALUES ('" + str(self.text[3]) + "', '" + str(self.text[2]) + "', '" + str(self.text[1]) + "', '" + str(self.ind_product[self.text[0]][0]) + "');")

# scrivere tipo sprintf            
#self.init_combo()

    def insert_product(self):
        self.d = InsertProduct()
        self.ok = self.d.exec_()
        if (self.ok):
            self.text = self.d.text()
            self.cursor.execute("insert into products (product, description) VALUES ('" + 
                                str(self.text[0]) + "', '" +
                                str(self.text[1]) + "');")
            self.init_combo()

    def init_combo(self):
        self.ind_product = []
        self.ui.comboBox.clear()
        self.cursor.execute("select ind, product from products")
        self.result = self.cursor.fetchall()
    
        for self.r in self.result:
            self.ui.comboBox.addItem(str(self.r[1]))
            self.ind_product.append((self.r[0], str(self.r[1])))
   
    def init_table(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(3)
        headerLabels = ("Revision", "Serial Number", "Shipment")
        self.ui.tableWidget.setHorizontalHeaderLabels(headerLabels);
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.show()

    def populate_table(self, index):
        self.cursor.execute("select object_ref from problems;")
        self.pro = []
        for self.a in self.cursor.fetchall():
            self.pro.append(self.a[0])
        
        self.cursor.execute("select description from products where ind = " + 
                            str(self.ind_product[index][0]))
        self.result = self.cursor.fetchall()
        self.ui.lineEdit.setText(self.result[0][0])

        self.cursor.execute("select revision, serial_number, shipment, ind from objects where type = " + str(self.ind_product[index][0]) + " order by serial_number")
        self.result = self.cursor.fetchall()
        self.a = len(self.result)
        self.ui.tableWidget.setRowCount(self.a)
        self.i = 0
        for self.r in self.result:
            self.item0 = QtGui.QTableWidgetItem(self.r[0])
            self.item1 = QtGui.QTableWidgetItem(self.r[1])
            self.item2 = QtGui.QTableWidgetItem(str(self.r[2]))
            if (self.r[3] in self.pro):
                self.item0.setBackground(QtGui.QBrush(QtGui.QColor(255,0,0)))
                self.item1.setBackground(QtGui.QBrush(QtGui.QColor(255,0,0)))
                self.item2.setBackground(QtGui.QBrush(QtGui.QColor(255,0,0)))

            self.ui.tableWidget.setItem(self.i, 0, self.item0);
            self.ui.tableWidget.setItem(self.i, 1, self.item1);
            self.ui.tableWidget.setItem(self.i, 2, self.item2);
            self.i += 1

        self.ui.tableWidget.resizeColumnsToContents()
