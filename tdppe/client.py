








from kivy.uix.popup import Popup
import time
#from twisted.internet.protocol import ClientFactory
#from twisted.protocols.basic import LineReceiver
#from twisted.internet import reactor
#import sys
#
#class EchoClient(LineReceiver):
#    end="Bye-bye!"
#    def connectionMade(self):
#        self.sendLine("Hello, world!")
#        self.sendLine("What a fine day it is.")
#        self.sendLine(self.end)
#
#    def lineReceived(self, line):
#        print "receive:", line
#        if line==self.end:
#            self.transport.loseConnection()
#
#class EchoClientFactory(ClientFactory):
#    protocol = EchoClient
#
#    def clientConnectionFailed(self, connector, reason):
#        print 'connection failed:', reason.getErrorMessage()
#        reactor.stop()
#
#    def clientConnectionLost(self, connector, reason):
#        print 'connection lost:', reason.getErrorMessage()
#        reactor.stop()

#factory = EchoClientFactory()
#reactor.connectTCP('localhost', 8000, factory)
#reactor.run()

# If using buildozer, you would instead set the presplash.filename token in your buildozer.spec file.

import kivy
kivy.require('1.8.0') 

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.atlas import Atlas

class RootWidget(BoxLayout):
    pass


class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0, 1, 0, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class TDPpe(Widget)


class MyApp(App):
    def build(self):
        self.icon = 'myicon.png'
        self.name = ""
        self.title = ""

        #self.atlas = Atlas("./tdpatlas.atlas")
        #print (self.atlas['Chiocciola_1'])
        self.sm = ScreenManager()
        screens = [Screen(name='Title {}'.format(i)) for i in range(4)]
        self.sm.add_widget(screens[0])
        img_tufo = Image(source="pictures/tufo.png")
        screens[0].add_widget(img_tufo)
        self.sm.add_widget(screens[1])
        img_palazzo = Image(source="pictures/palazzo_comunale.png")
        screens[0].add_widget(img_palazzo)
        #root.add_widget(img)
        #img.add_widget(Image(source="pictures/Istrice_1.gif", pos=(100, 100)))
        #c = CustomLayout()
        #root.add_widget(c)
        #c.add_widget(
        #    Image(
        #        source="pictures/palazzo_comunale.png"))
        #root.add_widget(Image(source="pictures/Chiocciola_1.gif"))
        #c = CustomLayout()
        #c.add_widget(
        #        Image(source="pictures/Chiocciola_1.gif",
        #        size_hint= (1, .5),
        #        pos_hint={'center_x':.5, 'center_y':.5}))
        #root.add_widget(c)
        return self.sm
        #filename = "pictures/Chiocciola_1.gif"
        #m = Image(source=filename)
        
    def loginPopup(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text="Username", size_hint=(1., None), size=(1., 30)))
        box.add_widget(TextInput(multiline=False, size_hint=(1., None), size=(1., 30)))
        box.add_widget(Label(text="Password", size_hint=(1., None), size=(1., 30)))
        box.add_widget(TextInput(multiline=False, size_hint=(1., None), size=(1., 30), password=True))
        # manca il bottone
        popup = Popup(title='Login', content=box, size_hint=(.5, .3), )
        popup.open()
        return

    def estrazione(self, list_):
        self.sm.next()
        pass
#        posx = (140, 190, 240, 290, 340, 390, 440, 490, 550, 625, 190, 240, 290, 340, 390, 440, 490)
#        posy = (440, 440, 440, 440, 440, 440, 440, 440, 440, 440, 220, 220, 220, 220, 220, 220, 215)
#  
#        self.ui.statusbar.showMessage("Estrazione delle Contrade")
#        #self.ui.label.show()
#  
#        bandiere = [Qt.QGraphicsPixmapItem() for i in xrange(17)]
#        scene = Qt.QGraphicsScene(self.ui.frame)
#
#        palazzo = scene.addPixmap(Qt.QPixmap(Qt.QString(":/estrazione/pictures/palazzo_comunale.png")));
#        palazzo.setPos(0,0)
#
#        for i in xrange(17):
#            s = Qt.QString(":/estrazione/pictures/" + list_[i] + "_1.gif")
#            bandiere[i] = scene.addPixmap(Qt.QPixmap(s))
#            bandiere[i].setPos(posx[i], posy[i])
#
#        scene.setSceneRect(0, 0, 906, 616);
#        #self.ui.graphicsView.setRenderHint(Qt.QPainter.Antialiasing)
#        #self.ui.graphicsView.setCacheMode(Qt.QGraphicsView.CacheBackground)
#        #self.ui.graphicsView.setDragMode(Qt.QGraphicsView.ScrollHandDrag)
#        self.ui.graphicsView.setScene(scene)
#        self.ui.graphicsView.scale(float(self.ui.graphicsView.width())/906., float(self.ui.graphicsView.height())/616.)
#        self.ui.graphicsView.show()
#  
#        for i in xrange(7):
#            bandiere[i].show()
#  
#        #if (self.soundWanted):
#            #Qt.QSound.play("../tdpalioclient/sound/chiarine.wav")
#            #FIXME
#            #sleep(10)
#        for i in xrange(7,10):
#            bandiere[i].show()
#            #sleep(3)
#
#        self.aggiornaContradeTable(1, list_)
#        # FIXME attiva tasto di avanzamento


if __name__ == '__main__':
    MyApp().run()


#    from kivy.uix.textinput import TextInput
#
#    def on_enter(instance, value):
#    print('User pressed enter in', instance)
#
#    textinput = TextInput(text='Hello world', multiline=False, password=True)
#    textinput.bind(on_text_validate=on_enter)
#    
#
#    pp = Popup(title='Test popup', content=Label(text='Hello world'),
#                  size_hint=(None, None), size=(400, 400))
#    pp = popup.Popup(title='Test popup', content=Label(text='Hello world'),
#              auto_dismiss=False)
#    #
#    #popup.dismiss()
#    # create content and add to the popup
#    content = Button(text='Close me!')
#    popup = Popup(content=content, auto_dismiss=False)
#    # bind the on_press event of the button to the dismiss function
#    content.bind(on_press=popup.dismiss)
#    # open the popup
#    popup.open()
#    def my_callback(instance):
#        print('Popup', instance, 'is being dismissed but is prevented!')
#        return True
#    popup = Popup(content=Label(text='Hello world'))
#    popup.bind(on_dismiss=my_callback)
#    popup.open()



