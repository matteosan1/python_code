from PyQt4 import QtGui, Qt
import time

def splash(mainwindow):
    #app = QtGui.QApplication([])
    pixmap = QtGui.QPixmap("/home/sani/python/tdpy/tdpyclient/splash/splash.jpg")
    s = QtGui.QSplashScreen(pixmap)#, Qt.WindowStaysOnTopHint)
    s.show()
    #app.processEvents()
    #mainwindow  = QtGui.QMainWindow()
    #mainwindow.setWindowOpacity(0.5);
    time.sleep(5)
    s.finish(mainwindow)

