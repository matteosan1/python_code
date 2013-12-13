#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import MySQLdb
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from palio_mainwindow import PalioMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #text = QInputDialog.getText(QDialog(), "Connessione a Palio DB",
    #                            "Password:", QLineEdit.Password);

    #if (text[1]):
        #db = MySQLdb.connect(host="localhost", user="sani",
        #                     passwd='%s' % text[0],
        #                     db="palio")
    db = MySQLdb.connect(host="localhost", user="sani",
    	                         passwd='mattesca96',
        	                     db="palio")

    main_window = PalioMainWindow(db)
    main_window.show()
    sys.exit(app.exec_())
