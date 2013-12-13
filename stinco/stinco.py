import re, os, sys
import pexpect
from PyQt4 import QtGui, QtCore, Qt
import sqlite 

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self) 
        self.resize(500, 700) 
        self.setWindowTitle('Stinco')
        #app.setWindowIcon(QtGui.QIcon('chalk.ico'))
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('stinco_log.png')))
        self.statusBar().showMessage('First CMS Social Network') 
        if (not os.path.exists("foto_cms")):
            os.mkdir("foto_cms")

        cWidget = QtGui.QWidget(self)
        self.label1 = QtGui.QLabel()
        self.label1.setText("Name:")
        self.lineEdit = QtGui.QLineEdit()
        self.label2 = QtGui.QLabel()
        self.label2.setText("Institute:")
        self.lineEdit2 = QtGui.QLineEdit()
        self.tableWidget = QtGui.QTableWidget()  
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.flat = QtGui.QPushButton("Search")
        #self.flat.setFlat(True)
        self.label = QtGui.QLabel()

        vBox = QtGui.QVBoxLayout()
        vBox.addWidget(self.label1)
        vBox.addWidget(self.lineEdit)
        vBox.addWidget(self.label2)
        vBox.addWidget(self.lineEdit2)
        vBox.addWidget(self.flat)
        vBox.addWidget(self.tableWidget)
        vBox.addWidget(self.label)
        
        cWidget.setLayout(vBox)
        self.setCentralWidget(cWidget)

        self.ids = []
        self.collaborators = []
        self.password = ""
        self.pattern = ""
        self.pattern2 = ""

        self.connect(self.flat, QtCore.SIGNAL('clicked()'), self.searchPeople)
        self.connect(self.tableWidget, QtCore.SIGNAL('cellClicked(int, int)'), self.showPeople)

        self.promptPassword()
        self.getCookie()
        self.db = sqlite.openDB("cms.db")
        self.cursor = self.db.cursor()
        
    def showPeople(self, x, y):
        myPixmap = QtGui.QPixmap("foto_cms/"+str(self.ids[x][2])+".jpg")
        myScaledPixmap = myPixmap.scaled(150, 300, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(myScaledPixmap)
                       
    def searchPeople(self):
        self.pattern = str(self.lineEdit.text())
        if (self.pattern == ""):
            self.pattern = "-1"
        self.pattern2 = str(self.lineEdit2.text())
        if (self.pattern2 == ""):
            self.pattern2 = "-1"
        self.ids = []
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
    
        self.ids = sqlite.selectFromDB(self.cursor, self.pattern, self.pattern2, "-1", -1)
        #print self.ids
        for i in self.ids:
            # mettere cursore di attesa...
            if (not os.path.exists("foto_cms/"+str(int(i[2]))+".jpg")):
                self.wgetPicture(int(i[2]))
        
        bar = QtGui.QProgressBar()
        bar.show()
        bar.setMinimum(0)
        bar.setMaximum(len(self.ids))
        for n, i in enumerate(self.ids):
            bar.setValue(n)
            bar.update()
            rowNum = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowNum)
            self.tableWidget.setItem(rowNum, 0, QtGui.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(rowNum, 1, QtGui.QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(rowNum, 2, QtGui.QTableWidgetItem(str(i[3])))

        bar.hide()
        self.tableWidget.setHorizontalHeaderLabels(QtCore.QStringList(["Name", "Institute", "Mail"]))
        self.tableWidget.resizeColumnsToContents()
 
    def promptPassword(self):
        text, ok = QtGui.QInputDialog.getText(self, '', 'Enter your lxplus5 password:', mode=QtGui.QLineEdit.Password)
        if ok:
            self.password = str(text)
        else:
            print "PROBLEMA !"

    def wgetPicture(self, id):
        command  = "wget --load-cookies ssocookie.txt https://cms-mgt-conferences.web.cern.ch/cms-mgt-conferences/conferences/user_photo.aspx?sid=" + str(id) + " -O " + str(id) + ".jpg"
        self.ssh(command)
        self.scp(str(id))
    
    def scp(self, command):
        ssh_newkey = 'Are you sure you want to continue connecting'
        p=pexpect.spawn('scp lxplus5.cern.ch:' + command + '.jpg foto_cms/.')

        i=p.expect([ssh_newkey, 'password:', pexpect.EOF])
        if i==0:
            p.sendline('yes')
            i=p.expect([ssh_newkey,'sani@lxplus5.cern.ch\'s password:',pexpect.EOF])
        if i==1:
            p.sendline(self.password)
            p.expect(pexpect.EOF)
        elif i==2:
            print "I either got key or connection timeout"
            pass

    def ssh(self, command):
        ssh_newkey = 'Are you sure you want to continue connecting'
        p=pexpect.spawn('ssh lxplus5.cern.ch ' + command)

        i=p.expect([ssh_newkey, 'password:', pexpect.EOF])
        if i==0:
            p.sendline('yes')
            i=p.expect([ssh_newkey,'sani@lxplus5.cern.ch\'s password:',pexpect.EOF])

        if i==1:
            p.sendline(self.password)
            p.expect(pexpect.EOF)
        elif i==2:
            print "I either got key or connection timeout"
            pass

    def getCookie(self):
        # check timeout
        command = "cern-get-sso-cookie --krb -u https://cms-mgt-conferences.web.cern.ch/cms-mgt-conferences/Default.aspx -o ssocookie.txt"
        self.ssh(command)
        self.statusBar().showMessage('Login successful')
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Qt.QApplication.setQuitOnLastWindowClosed(True)
    main = MainWindow()
    main.show()
    #app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))
    sys.exit(app.exec_())

