#! /usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore


#a = QtGui.QApplication(sys.argv)

#def sayHello():
#    print "Ciao, merdacce"

#helloButton = QtGui.QPushButton("Say 'Ciao merine'", None)

#a.connect(helloButton, QtCore.SIGNAL("clicked()"), sayHello)


#hello = QtGui.QLabel("Hello", None)

# to understand
#a.setMainWidget(hello)

#helloButton.show()

#a.exec_()



class HelloApplication(QtGui.QApplication):
    
    def __init__(self, args):
        """In the constructor we're doing everything to get our application 
           started, which is basically constructing a basic QApplication by
           its __init__ method, then adding our widgets and finally starting
           the exec_."""
        QtGui.QApplication.__init__(self, args)
        self.addWidgets()
        self.exec_()

    def addWidgets(self):
        self.hellobutton = QtGui.QPushButton("Say 'Hello world'", None)
        self.connect(self.hellobutton, QtCore.SIGNAL("clicked()"), self.slotSayHello)
        #self.setMainWidget(self.hellobutton)
        self.hellobutton.show()

    def slotSayHello(self):
        print "Hello, world"

if __name__ == "__main__":
    app = HelloApplication(sys.argv)
