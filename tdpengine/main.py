import sys
import random
import math

from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QGraphicsItem
from PyQt4.QtGui import QGraphicsScene
from PyQt4.QtGui import QGraphicsView
from PyQt4.QtGui import QPainter, QSlider
from PyQt4.QtGui import QPushButton, QColor
from PyQt4.QtGui import QPainterPath
from PyQt4.QtGui import QPolygonF
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QBrush
from PyQt4.QtCore import *
#from PyQt4.QtCore import QRectF

SCENESIZEX = 1146
SCENESIZEY = 956
INTERVAL = 100

nodes = []

class node():
    x = float()
    y = float()
    angle = float()
    type = int()
    d = int()

class MainForm(QDialog):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.Running = False
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, SCENESIZEX, SCENESIZEY)
        self.view = QGraphicsView()
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setScene(self.scene)
        self.view.setFocusPolicy(Qt.NoFocus)
        #self.zoomSlider = QSlider(Qt.Horizontal)
        #self.zoomSlider.setRange(5, 200)
        #self.zoomSlider.setValue(100)
        self.pauseButton = QPushButton("Pa&use")
        self.quitButton = QPushButton("&Quit")

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        #layout.addWidget(self.zoomSlider)
        layout.addWidget(self.pauseButton)
        layout.addWidget(self.quitButton)
        self.setLayout(layout)

        #self.connect(self.zoomSlider, SIGNAL("valueChanged(int))"),
        #             self.zoom)
        self.connect(self.pauseButton, SIGNAL("clicked()"),
                     self.pauseOrResume)
        self.connect(self.quitButton, SIGNAL("clicked()"), self.accept)
        
        self.readNodes()
        self.zoom(1.0)
        self.populate()
        #self.startTimer(INTERVAL)
        self.setWindowTitle("TdPaleo")
        
    def pauseOrResume(self):
        self.Running = not self.Running
        self.pauseButton.setText("Pa&use" if self.Running else "Res&ume")
        items = self.scene.items()
        for item in items:
            item.setRunning()
    
    def zoom(self, value):
        factor =1/ 1.5
        matrix = self.view.matrix()
        matrix.reset()
        matrix.scale(factor, factor)
        self.view.setMatrix(matrix)
    
    def readNodes(self):
        file = open("tdp_geometry.dat")
        file.readline()
        while True:
            line = file.readline()
            if not line:
                break
            param = line.split(" ")
            if (line != "\n"):
                n = node()
                n.x = float(param[0])
                n.y = 956 - float(param[1])
                n.angle = float(param[2])
                n.d = int(param[3])
                n.type = int(param[4])
                nodes.append(n)

    def populate(self):
        color = QColor(0, 150, 0)
        head = TdPCavallo(color, nodes[0].angle, QPointF(nodes[0].x, nodes[0].y))
        #FIXME AGGIUNGERE POI IL FANTINO AL CAVALLO
        #segment = Segment(color, offset, head)
        self.scene.addItem(head)
        #Running = False
        
    def timerEvent(self, event):
        if not self.Running:
            return

class TdPCavallo(QGraphicsItem):
    Rect = QRectF(-8, -2, 8, 2)
    
    def __init__(self, color, angle, position):
        super(TdPCavallo, self).__init__()
        self.color = color
        self.angle = angle
        self.setPos(position)
        self.timer = QTimer()
        QObject.connect(self.timer, SIGNAL("timeout()"), self.timeout)
        self.timer.start(INTERVAL)
        self.row = 0
        self.column = 1
        self.rotate(-math.degrees(angle))
        self.Running = False

    def setRunning(self):
        self.Running = not self.Running
        
    def boundingRect(self):
        return TdPCavallo.Rect

    def shape(self):
        path = QPainterPath()
        path.addEllipse(TdPCavallo.Rect)
        return path

    def paint(self, painter, option, widget=None):
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(self.color))
        painter.drawEllipse(TdPCavallo.Rect)
        #if option.levelOfDetail > 0.5:
        #    painter.setBrush(QBrush(Qt.yellow))
        #    painter.drawEllipse(-12, -19, 8, 8)  
        #    painter.drawEllipse(-12, 11, 8, 8)
        #    if option.levelOfDetail > 0.9:
        #        painter.setBrush(QBrush(Qt.darkBlue))
        #        painter.drawEllipse(-12, -19, 4, 4)  
        #        painter.drawEllipse(-12, 11, 4, 4)
        #        if option.levelOfDetail > 0.5:
        #            painter.setBrush(QBrush(Qt.white))
        #            painter.drawEllipse(-27, -5, 2, 2)  
        #            painter.drawEllipse(-27, 3, 2, 2)

    def timeout(self):
        if not self.Running:
            return
        self.row += 1

        if (self.row == len(nodes)):
            self.row = 0

        self.rotate(-math.degrees(nodes[self.row].angle - self.angle))
        self.angle = nodes[self.row].angle
        self.setPos(QPointF(nodes[self.row].x, nodes[self.row].y))
        #angle = self.angle
        #while True:
        #    angle += random.randint(-9,9)
        #    offset = random.randint(3, 15)
        #    x = self.x() + (offset * math.sin(math.radians(angle)))
        #    y = self.y() + (offset * math.cos(math.radians(angle)))
        #    if 0 <= x <= SCENESIZE and 0 <= y <= SCENESIZE:
        #        break
        #self.angle = angle
        #self.rotate(random.randint(-5,5))
        #self.setPos(QPointF(x,y))
        #for item in self.scene().collidingItems(self):
        #    if isinstance(item, Head):
        #        self.color.setRed(min(255, self.color.red() +1))
        #    else:
        #        item.color.setBlue(min(255, item.color.blue() +1))
                
#class Segment(QGraphicsItem):
#    def __init__(self, color, offset, parent):
#        super(Segment, self).__init__(parent)
#        self.color = color
#        self.rect = QRectF(offset, -20, 30, 40)
#        self.path = QPainterPath()
#        self.path.addEllipse(self.rect)
#        x = offset + 15
#        y = -20
#        self.path.addPolygon(QPolygonF([QPointF(x,y),
#                                        QPointF(x-5, y-12), 
#                                        QPointF(x-5, y)]))
#        self.path.closeSubpath()
#        y = 20
#        self.path.addPolygon(QPolygonF([QPointF(x,y),
#                                        QPointF(x-5, y+12), 
#                                        QPointF(x-5, y)]))
#        self.path.closeSubpath()
#        self.change = 1
#        self.angle=0
#        self.timer = QTimer()
#        QObject.connect(self.timer, SIGNAL("timeout()"), self.timeout)
#        self.timer.start(INTERVAL)
#
#    def boundingRect(self):
#        return self.path.boundingRect()
#
#    def shape(self):
#        return self.path
#
#    def paint(self, painter, option, widget=None):
#        painter.setPen(Qt.NoPen)
#        painter.setBrush(QBrush(self.color))
#        if option.levelOfDetail < 0.9:
#            painter.drawEllipse(self.rect)
#        else:
#            painter.drawPath(self.path)
#
#    def timeout(self):
#        if not Running:
#            return
#        matrix = self.matrix()
#        matrix.reset()
#        self.setMatrix(matrix)
#        self.angle += self.change
#        if self.angle > 5:
#            self.change = -1
#            self.angle -= 1
#        elif self.angle < -5:
#            self.change = 1
#            self.angle += 1
#        self.rotate(self.angle)
            

app = QApplication(sys.argv)

#     qsrand(QTime(0,0,0).secsTo(QTime::currentTime()));

topLevel = MainForm()
#topLevel.setWindowTitle("Ported Asteroids Game");
topLevel.show();

app.setQuitOnLastWindowClosed(True);

sys.exit(app.exec_())



