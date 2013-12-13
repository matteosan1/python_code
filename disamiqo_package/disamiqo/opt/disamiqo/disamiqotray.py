import random
import sys
import os
import pexpect

from PyQt4 import Qt

class DisamiqoTray(Qt.QDialog):
    def __init__(self):
        Qt.QDialog.__init__(self)
        self.iconLabel = Qt.QLabel()
        self.setWindowIcon(Qt.QIcon(":/images/disamiqoicon.png"))
        
        self.disamici = ["Matteo", "Stefano", "PJ", "Simone", "Andrea", "Chiara",
                         "Broccolo", "Riccardo", "Raffa", "Florentina", "Ciccio", "CC", "Antonio",
                         "Schlenk", "Vitaliano", "Nicoletta", "Elisabetta", "Alessandro"]
        self.disamici.sort()
        self.disamici = ["Casuale"] + self.disamici

        self.currentDisamico = 0

        self.createMessageGroupBox();
        self.iconLabel.setMinimumWidth(self.durationLabel.sizeHint().width());
        self.createActions();
        self.createTrayIcon();

        self.trayIcon.show()
        self.setWindowTitle("DisamiQo Settings")
        self.resize(400, 300)
        self.timer = Qt.QTimer(self)
        self.iconTimer = Qt.QTimer(self)
        self.decc = Qt.QTime().currentTime()
        Qt.QObject.connect(self.timer, Qt.SIGNAL("timeout()"), self.showMessage)
        Qt.QObject.connect(self.iconTimer, Qt.SIGNAL("timeout()"), self.resetIcon)
        self.timer.start(900000);
        self.rand = random.Random()
        self.rand.seed()

    def enableOK(self):
        self.okButton.button(Qt.QDialogButtonBox.Ok).setEnabled(True)
        
    def acceptedPressed(self):
        self.timer.setInterval(self.durationSpinBox.value() * 60000)
        if (self.typeComboBox.currentIndex() != 0):
            self.currentDisamico = self.typeComboBox.currentIndex()
        self.close()

    def rejectedPressed(self):
        self.close()
        
    def closeEvent(self, event):
        if (self.trayIcon.isVisible()):
            self.hide()
            event.ignore()
    
    def openSettings(self):
        self.okButton.button(Qt.QDialogButtonBox.Ok).setEnabled(False)
        self.show()

    def iconActivated(self, reason):
        if (reason == Qt.QSystemTrayIcon.DoubleClick):
            self.showMessage()
         
    def showMessage(self):
        #mybell = Qt.QSound('puppa')
        #mybell.play()

        if (self.currentDisamico == 0):
            d = self.rand.randint(1, len(self.disamici)-1)
        else:
            d = self.currentDisamico
	
	if (self.disamici[d] == "CC"):
            self.trayIcon.setIcon(Qt.QIcon(Qt.QPixmap(":/images/"+self.disamici[d]+".png")))
            decc1 = Qt.QTime().currentTime()
            secs = self.decc.secsTo(decc1)
            fraseCC = "Lo vuoi riprogrammare te disamiQo, se lo vuoi riprogrammare te lo dici...\n\n (Applicazione deCCzata per %.2dh %.2dm %.2ds)"%((secs/3600), ((secs%3600)/60), ((secs%3600)%60))
            if (Qt.QMessageBox.critical(self, "Disamiqo", 
                                        fraseCC)):
		sys.exit(-1)
                
        file = open("/opt/disamiqo/frasi/"+self.disamici[d]+".txt")
        lines = file.readlines()
        file.close()

        self.currentLine = self.rand.choice(lines)
    
        self.trayIcon.setIcon(Qt.QIcon(Qt.QPixmap(":/images/"+self.disamici[d]+".png")))
        self.trayIcon.showMessage("Ciao " +self.disamici[d]+" !",
                                  self.currentLine, 
                                  Qt.QSystemTrayIcon.NoIcon)
        self.iconTimer.start(10000)

    def resetIcon(self):
        self.iconTimer.stop()
        self.trayIcon.setIcon(Qt.QIcon(Qt.QPixmap(":/images/disamiqoicon.png")))

    def about(self):
        Qt.QMessageBox.about(self, "About",
                             "\nDisamiQo v1.3\n\nMatteoSoftware (C)2009\n") 

    def saveChanges(self):
        file = open("/opt/disamiqo/frasi/"+self.disamici[self.tempDisamico]+".txt", "w")
        for i in range(self.bodyEdit.count()):
            line = self.bodyEdit.item(i)
            if (line.text() != ""):
                file.write(line.text()+"\n")
        file.close()

    def addMessage(self):
        self.enableOK()
        item = Qt.QListWidgetItem()
        item.setFlags(Qt.Qt.ItemIsEnabled|Qt.Qt.ItemIsSelectable|Qt.Qt.ItemIsEditable)
        self.bodyEdit.insertItem(self.bodyEdit.count(), item) 
        self.bodyEdit.editItem(item)
     
    def messageClicked(self):
        self.message = Qt.QMessageBox(1,
                                      "DisamiQo",
                                      self.currentLine)
        icon = self.trayIcon.icon()
        self.message.setIconPixmap(icon.pixmap(100))
        self.message.setFont(Qt.QFont("Times", 12, Qt.QFont.Bold))
        # FIXME fix the size of the window
        self.message.setWindowIcon(Qt.QIcon(":/images/disamiqoicon.png"))
        self.message.resize(500,500)
        self.message.show()


    def populateList(self, index):
        self.enableOK()
        self.tempDisamico = index
        self.bodyEdit.clear()
        self.showMessageButton.setEnabled(False)
        if (index > 0 and self.disamici[index] != "CC"):
            self.showMessageButton.setEnabled(True)
            file = open("/opt/disamiqo/frasi/"+self.disamici[index]+".txt")
            lines = file.readlines()
            file.close()            
            for i in lines:
                item = Qt.QListWidgetItem(i.split("\n")[0], self.bodyEdit)
                item.setFlags(Qt.Qt.ItemIsEnabled|Qt.Qt.ItemIsSelectable|Qt.Qt.ItemIsEditable)
                
    def loginDialog(self):
        self.login = Qt.QDialog(self)
        self.userLabel = Qt.QLabel("User Name: ")
        self.pwdLabel = Qt.QLabel("Password: ")
        self.userEdit = Qt.QLineEdit("")
        self.pwdEdit = Qt.QLineEdit("")
        self.pwdEdit.setEchoMode(Qt.QLineEdit.Password)
        self.ok = Qt.QDialogButtonBox(Qt.QDialogButtonBox.Ok|Qt.QDialogButtonBox.Cancel)
        Qt.QObject.connect(self.ok, Qt.SIGNAL("accepted()"), self.login.accept)  
        Qt.QObject.connect(self.ok, Qt.SIGNAL("rejected()"), self.login.reject)  
        self.dialogLayout = Qt.QGridLayout(self.login)
        self.dialogLayout.addWidget(self.userLabel, 0, 0)
        self.dialogLayout.addWidget(self.pwdLabel, 1, 0)
        self.dialogLayout.addWidget(self.userEdit, 0, 1)
        self.dialogLayout.addWidget(self.pwdEdit, 1, 1)
        self.dialogLayout.addWidget(self.ok, 2, 2)
        return self.login

    def upload(self):
        #if (self.loginDialog().exec_() != Qt.QDialog.Accepted):
        #    return

        lines = os.popen("ls -1 /opt/disamiqo/frasi/*.txt").readlines()
        self.progressBar.setRange(0, len(lines))
        self.progressBar.setVisible(True)
        for n, i in enumerate(lines):
            i = i.split("\n")[0]
            try:
                #foo = pexpect.spawn("scp "+i+" "+str(self.userEdit.text())+"guest@.cern.ch:~sani/public/matteosoftware/.")
                foo = pexpect.spawn("scp "+i+" guest@pclxcms02.cern.ch:matteosoftware/.")
                foo.expect('.assword:')
                foo.sendline("guest")
                foo.interact()
            except:    
                pass
                #print "Exception was thrown"
                #print "debug information:"
                #print str(foo)
            
            self.progressBar.setValue(n)

        self.progressBar.setValue(self.progressBar.maximum())
        if (Qt.QMessageBox.information(self, "Disamiqo", 
                                    "Upload frasi completato !")):
            self.progressBar.hide()
        self.enableOK()

    def download(self):
        #if (self.loginDialog().exec_() != Qt.QDialog.Accepted):
        #    return
        lines = os.popen("ls -1 /opt/disamiqo/frasi/*.txt").readlines()
        self.progressBar.setRange(0, len(lines))
        self.progressBar.setVisible(True)
        for n, i in enumerate(lines): 
            i = i.split("\n")[0]
            i = i.split("/")[-1]
            try:
                #foo = pexpect.spawn("scp "+str(self.userEdit.text())+"@lxplus.cern.ch:~sani/public/matteosoftware/"+i+" /opt/disamiqo/frasi/"+i+"_temp")
                foo = pexpect.spawn("scp guest@pclxcms02.cern.ch:matteosoftware/"+i+" /opt/disamiqo/frasi/"+i+"_temp")
                foo.expect('.assword:')
                foo.sendline("guest")
                foo.interact()
            except:    
                pass
            self.progressBar.setValue(n)
            diff = pexpect.run("diff /opt/disamiqo/frasi/"+i+" /opt/disamiqo/frasi/"+i+"_temp")
            file_temp = open("/opt/disamiqo/frasi/"+i, "a")
            for line in diff.split("\n"):
                line = line.split("\r")[0]
                if (line.find("> ") != -1):
                    line = line[2:]
                    file_temp.write(line+"\n")
            file_temp.close()
            rm = pexpect.run("rm /opt/disamiqo/frasi/"+i+"_temp")

        self.progressBar.setValue(self.progressBar.maximum())
        

        if (Qt.QMessageBox.information(self, "Disamiqo", 
                                    "Download frasi completato !")):
            self.progressBar.hide()
        self.enableOK()

    def createMessageGroupBox(self):
        self.typeLabel = Qt.QLabel("Disamico Preferito:")
        self.typeComboBox = Qt.QComboBox()
        for i in self.disamici:
            if (i != "Casuale" and i != ""):
                self.typeComboBox.addItem(Qt.QIcon(":/images/"+i+".png"), i)
            else:
                self.typeComboBox.addItem(i)

        self.typeComboBox.setCurrentIndex(self.currentDisamico)

        self.durationLabel = Qt.QLabel("Intervallo:")
        self.durationSpinBox = Qt.QSpinBox()
        self.durationSpinBox.setRange(1, 60)
        self.durationSpinBox.setSuffix(" min.")
        self.durationSpinBox.setValue(15)

        self.progressBar = Qt.QProgressBar(self)
        self.progressBar.setVisible(False)

        self.labelWarn = Qt.QLabel("Prima di fare Upload aggiorna i messaggi !")
        self.uploadButton = Qt.QPushButton("Upload")
        self.downloadButton = Qt.QPushButton("Download")        
        self.uploadButton.setDefault(False)
        self.downloadButton.setDefault(False)
        #self.uploadButton.autoDefault(False)
        #self.downloadButton.autoDefault(False)

        self.okButton = Qt.QDialogButtonBox(Qt.QDialogButtonBox.Ok|Qt.QDialogButtonBox.Cancel)        
        self.okButton.button(Qt.QDialogButtonBox.Ok).setEnabled(False)
        self.okButton.button(Qt.QDialogButtonBox.Ok).setDefault(True)
        
        self.bodyLabel = Qt.QLabel("Frasi:")
        self.bodyEdit = Qt.QListWidget()
        self.bodyEdit.setEditTriggers(Qt.QAbstractItemView.DoubleClicked)
        
        self.showMessageButton = Qt.QPushButton("Aggiungi Frase")
        self.showMessageButton.setEnabled(False)
        #self.showMessageButton.autoEnabled(False)
        
        self.messageLayout = Qt.QGridLayout(self)
        self.messageLayout.addWidget(self.typeLabel, 0, 0)
        self.messageLayout.addWidget(self.typeComboBox, 0, 1)
        self.messageLayout.addWidget(self.durationLabel, 1, 0)
        self.messageLayout.addWidget(self.durationSpinBox, 1, 1)
        self.messageLayout.addWidget(self.bodyLabel, 3, 0)
        self.messageLayout.addWidget(self.bodyEdit, 3, 1, 8, 5)
        self.messageLayout.addWidget(self.labelWarn, 8, 0)
        self.messageLayout.addWidget(self.uploadButton, 9, 0)
        self.messageLayout.addWidget(self.downloadButton, 10, 0)
        self.messageLayout.addWidget(self.progressBar, 11, 0)
        self.messageLayout.addWidget(self.showMessageButton, 11, 1)
        self.messageLayout.addWidget(self.okButton, 12, 3)
        self.messageLayout.setColumnStretch(3, 1)
        self.messageLayout.setRowStretch(4, 2)
        
    def createActions(self):
        self.settingsAction = Qt.QAction("&Settings", self)
        Qt.QObject.connect(self.settingsAction, Qt.SIGNAL("triggered()"), self.openSettings)

        self.aboutAction = Qt.QAction("&About", self)
        Qt.QObject.connect(self.aboutAction, Qt.SIGNAL("triggered()"), self.about)
        
        self.quitAction = Qt.QAction("&Quit", self)
        Qt.QObject.connect(self.quitAction, Qt.SIGNAL("triggered()"), Qt.qApp, Qt.SLOT("quit()"))
        
#    def closeEditor(self, current, previous):
#        self.bodyEdit.closePersistentEditor(previous)

    def createTrayIcon(self):
        self.trayIconMenu = Qt.QMenu(self)
        self.trayIconMenu.addAction(self.settingsAction)
        self.trayIconMenu.addAction(self.aboutAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = Qt.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.setIcon(Qt.QIcon(Qt.QPixmap(Qt.QString(":/images/disamiqoicon.png"))))
        self.trayIcon.setToolTip("DisamiQo")

        Qt.QObject.connect(self.durationSpinBox, Qt.SIGNAL("valueChanged(int)"), self.enableOK)

        Qt.QObject.connect(self.uploadButton, Qt.SIGNAL("clicked()"), self.upload)
        Qt.QObject.connect(self.downloadButton, Qt.SIGNAL("clicked()"), self.download)

        Qt.QObject.connect(self.showMessageButton, Qt.SIGNAL("clicked()"), self.addMessage)

        #Qt.QObject.connect(self.trayIcon, Qt.SIGNAL("messageClicked()"), self.messageClicked)
        Qt.QObject.connect(self.trayIcon, Qt.SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.iconActivated)

        Qt.QObject.connect(self.okButton, Qt.SIGNAL("accepted()"), self.acceptedPressed)  
        Qt.QObject.connect(self.okButton, Qt.SIGNAL("rejected()"), self.rejectedPressed)  

        Qt.QObject.connect(self.typeComboBox, Qt.SIGNAL("currentIndexChanged(int)"), self.populateList) 

        Qt.QObject.connect(self.bodyEdit, Qt.SIGNAL("itemIsDoubleClicked(QListWidgetItem*)"), 
                           self.bodyEdit.editItem)

        Qt.QObject.connect(self.bodyEdit, Qt.SIGNAL("itemChanged(QListWidgetItem*)"), self.saveChanges)
#        Qt.QObject.connect(self.bodyEdit, Qt.SIGNAL("currentItemChanged(QListWidgetItem*, QListWidgetItem*)"),
#                           self.closeEditor)
