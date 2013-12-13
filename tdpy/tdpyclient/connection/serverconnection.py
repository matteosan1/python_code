from PyQt4 import Qt
import serverconnection_widget

class serverConnection(Qt.QDialog):
    def __init__(self):
        Qt.QDialog.__init__(self)
        self.ui = serverconnection_widget.Ui_serverConnection()
        self.ui.setupUi(self)
        self.host_ = "localhost"
        self.port_ = 1974
        self.local = 0

        Qt.QObject.connect(self.ui.lineEdit, Qt.SIGNAL('textChanged(QString)'), self.host)
        Qt.QObject.connect(self.ui.lineEdit_2, Qt.SIGNAL('textChanged(QString)'), self.port)
        Qt.QObject.connect(self.ui.checkBox, Qt.SIGNAL('stateChanged(int)'), self.localConnection)
        
    def host(self, text):
        self.host_ = text
    
    def port(self, text):
        self.port = text.toInt()

    def localConnection(self, a):
        if (a == 0):
            self.ui.lineEdit.setEnabled(True)
            self.ui.lineEdit_2.setEnabled(True)
            self.local = 0
  
        if (a == 2):
            self.ui.lineEdit.setEnabled(False)
            self.ui.lineEdit_2.setEnabled(False)
            self.local = 1
            self.host_ = "localhost"
            self.port_ = 1974
