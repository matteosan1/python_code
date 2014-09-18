#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import sqlite3
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from palio_mainwindow import PalioMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    db = sqlite3.connect('/Users/sani/databases/palio_new.db')
    main_window = PalioMainWindow(db)
    main_window.show()
    sys.exit(app.exec_())
