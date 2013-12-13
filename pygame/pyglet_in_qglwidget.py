#!/usr/bin/env python

import sys, math, os 
from PyQt4 import QtGui, QtCore, QtOpenGL

if 'PYGLET' in os.environ: 
    from pyglet.gl import *
    def glmult(l): 
        return glMultMatrixf( (GLfloat * len(l))(*l) )
else: 
    from OpenGL.GL import *

def glmult(l): 
    return glMultMatrixf( l )

class GLWidget(QtOpenGL.QGLWidget): 
    def __init__(self, parent=None): 
        QtOpenGL.QGLWidget.__init__(self, parent)

    def initializeGL(self): 
        glClearColor(0.0, 0.0, 0.0, 0.0) 
        glShadeModel(GL_FLAT)

    def lookAt(self,ex,ey,ez,cx,cy,cz,ux,uy,uz): 
        F = [cx-ex, cy-ey, cz-ez] 
        Fmag = math.sqrt(sum([a*a for a in F])) 
        fnorm = [a/Fmag for a in F]

        Up = [ux,uy,uz] 
        Upmag = math.sqrt(sum([a*a for a in Up])) 
        upnorm = [a/Upmag for a in Up]

        def cross(v1,v2): 
            return [v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0]]

        s = cross( fnorm, upnorm ) 
        u = cross( s, fnorm )

        glmult([ s[0], s[1], s[2], 0, u[0], u[1], u[2], 0, -fnorm[0], -fnorm[1], -fnorm[2], 0, 0, 0, 0, 1 ]) glTranslated(-ex, -ey, -ez)

    def paintGL(self): 
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0,1.0,1.0) 
        glLoadIdentity() 
        self.lookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) 
        glScalef(1.0, 2.0, 1.0) 
        glBegin(GL_TRIANGLES) 
        glNormal3f(1,0,0) 
        glVertex3f(1,0,0) 
        glVertex3f(0,1,0) 
        glVertex3f(1,1,0) 
        glEnd() 
        glFlush()

    def resizeGL(self, height, width): 
        glViewport(0, 0, width, height) 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() 
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0) 
        glMatrixMode(GL_MODELVIEW)

    def mousePressEvent(self, event): 
        print "mousePressEvent:",event.pos()

    def mouseMoveEvent(self, event): 
        print "mouseMoveEvent:",event.pos()

class MainWindow(QtGui.QMainWindow): 
    def __init__(self): 
        QtGui.QMainWindow.__init__(self)
        self.resize(350, 400) 
        self.setWindowTitle('Main Window')

        self.gl = glwidget = GLWidget() self.setCentralWidget(glwidget)

        exit = QtGui.QAction(QtGui.QIcon(), 'Exit', self) 
        exit.setShortcut('Ctrl+Q') 
        exit.setStatusTip('Exit application') 
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        self.statusBar()

        toolbar = self.addToolBar('Exit') 
        toolbar.addAction(exit)

    def idle(self): 
        pass

# QT app 
app = QtGui.QApplication(sys.argv) 
main = MainWindow() 
main.show()
sys.exit(app.exec_()) 
