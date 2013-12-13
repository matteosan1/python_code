#! /usr/bin/env python

import sys
import MySQLdb
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from main import MainDialog

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    #window = QMainWindow()
    main_window = MainDialog()
    #main_window.setup()
    
    text = QInputDialog.getText(main_window, "QInputDialog::getText()",
                                "User name:");
    
    if (text[1]):
        db = MySQLdb.connect(host="localhost", user="sani", 
                             passwd='%s' % text[0],
                             db="force_10")

        main_window.init_combo(db)
        main_window.show()
        sys.exit(app.exec_())
