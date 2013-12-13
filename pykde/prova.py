import sys
from PyKDE4.kdecore import ki18n, KAboutData, KCmdLineArgs
from PyKDE4.kdeui import KApplication, KMainWindow
from PyQt4.QtGui import QLabel

class MainWindow (KMainWindow):
    def __init__ (self):
        KMainWindow.__init__ (self)
        
        self.resize (640, 480)
        label = QLabel ("This is a simple PyKDE4 program", self)
        label.setGeometry (10, 10, 200, 20)


#--------------- main ------------------
if __name__ == '__main__':

    appName     = "KApplication"
    catalog     = ""
    programName = ki18n ("KApplication")
    version     = "1.0"
    description = ki18n ("KApplication/KMainWindow/KAboutData example")
    license     = KAboutData.License_GPL
    copyright   = ki18n ("(c) 2007 Jim Bublitz")
    text        = ki18n ("none")
    homePage    = "www.riverbankcomputing.com"
    bugEmail    = "jbublitz@nwinternet.com"
    
    aboutData   = KAboutData (appName, catalog, programName, version, description,
                              license, copyright, text, homePage, bugEmail)
    
    KCmdLineArgs.init (sys.argv, aboutData)
    
    app = KApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
