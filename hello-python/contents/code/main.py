#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
#from PyKDE4.plasma import Plasma
#from PyKDE4 import plasmascript
# 
#class HelloPython(plasmascript.Applet):
#    def __init__(self,parent,args=None):
#        plasmascript.Applet.__init__(self,parent)
# 
#    def init(self):
#        self.setHasConfigurationInterface(False)
#        self.resize(125, 125)
#        self.setAspectRatioMode(Plasma.Square)
# 
#    def paintInterface(self, painter, option, rect):
#        painter.save()
#        painter.setPen(Qt.white)
#        painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, "Hello Python!")
#        painter.restore()
# 
#def CreateApplet(parent):
#    return HelloPython(parent)

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
 
class HelloWorldApplet(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
 
    def init(self):
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.Square)
 
        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)
 
        self.layout = QGraphicsLinearLayout(Qt.Horizontal, self.applet)
        label = Plasma.Label(self.applet)
        label.setText("Hello world!")
        self.layout.addItem(label)
        self.applet.setLayout(self.layout)
        self.resize(125,125)
 
def CreateApplet(parent):
    return HelloWorldApplet(parent)
