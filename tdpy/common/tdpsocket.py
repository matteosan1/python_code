from PyQt4.QtNetwork import *

class Socket(QTcpSocket):
  def __init__(self, t=-1, parent=None):
    super(Socket, self).__init__(parent)
    #self.connect(self, SIGNAL("disconnected()"), self.deleteLater)
    self.tipo = t
    self.stato = "Not Ready"
    self.userName = "AI"
