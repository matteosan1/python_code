import kivy
kivy.require('1.7.2')
 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivy.graphics import Rectangle, Color, Canvas
from functools import partial
from random import *

from kivy.config import Config
Config.set('graphics','resizable',0) #don't make the app re-sizeable

#Graphics fix ?????????
Window.clearcolor = (0,0,0,1.)

class MyButton(Button):
    #class used to get uniform button styles
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.font_size = Window.width*0.018

class SmartMenu(Widget):
    #the instance created by this class will appear when the game is started for the first time
    buttonList = []
 
    def __init__(self, **kwargs):
        #create custom events first
        self.register_event_type('on_button_release') 
 
        super(SmartMenu, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
 
    def on_button_release(self, *args):
        #print 'The on_button_release event was just dispatched', args
        #don't need to do anything here. needed for dispatch
        pass
 
    def callback(self,instance):
        #print('The button %s is being pressed' % instance.text)
        self.buttonText = instance.text
        self.dispatch('on_button_release') #dispatching the callback event 'on_button_release' to tell teh parent instance to read the button text
 
    def addButtons(self):
        for k in self.buttonList:
            tmpBtn = MyButton(text = k)
            tmpBtn.background_color = [.4, .4, .4, .4]
            tmpBtn.bind(on_release = self.callback) #when the button is released the callback function is called
            self.layout.add_widget(tmpBtn)
 
    def buildUp(self):
        #self.colorWindow()
        self.addButtons()

class SmartStartMenu(SmartMenu):
    #setup the menu button names
    buttonList = ['start', 'about']
 
    def __init__(self, **kwargs):
        super(SmartStartMenu, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical')
        self.layout.width = Window.width/2
        self.layout.height = Window.height/2
        self.layout.x = Window.width/2 - self.layout.width/2
        self.layout.y = Window.height/2 - self.layout.height/2
        self.add_widget(self.layout)
 
        self.msg = Label(text = 'Flappy Ship')
        self.msg.font_size = Window.width*0.07
        self.msg.pos = (Window.width*0.45,Window.height*0.75)
        self.add_widget(self.msg)
        self.img = Image(source = 'lens2.png')
        self.img.size = (Window.width*1.5,Window.height*1.5)
        self.img.pos = (-Window.width*0.2,-Window.height*0.2)
        self.img.opacity = 0.35
        self.add_widget(self.img)

class WidgetDrawer(Widget):
    #This widget is used to draw all of the objects on the screen
    #it handles the following:
    # widget movement, size, positioning
    #whever a WidgetDrawer object is created, an image string needs to be specified
    #example:    wid - WidgetDrawer('./image.png')
 
    def __init__(self, imageStr, **kwargs): 
        super(WidgetDrawer, self).__init__(**kwargs) 
        with self.canvas: 
            self.size = (Window.width*.002*25,Window.width*.002*25) 
            self.rect_bg=Rectangle(source=imageStr,pos=self.pos,size = self.size) 

            self.bind(pos=self.update_graphics_pos) 
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x,self.y) 
            self.rect_bg.pos = self.pos 
 
    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value  

    def setSize(self,width, height): 
        self.size = (width, height)

    def setPos(xpos,ypos):
        self.x = xpos
        self.y = ypos 

class ScoreWidget(Widget):
    def __init__(self, **kwargs):
        super(ScoreWidget, self).__init__(**kwargs)
        self.asteroidScore = 0
        self.currentScore = 0
        with self.canvas:
            tmpPos = (Window.width*0.25,Window.height*0.25)
            tmpSize = (Window.width*0.5,Window.height*0.5)
            Color(0.1,.1,.1)
            self.scoreRect = Rectangle(pos= tmpPos,size = tmpSize )
 
    def prepare(self):
        #calculate the score
        try:
 
            self.finalScore = self.asteroidScore*100
 
        except:
            print 'problems getting score'
        self.animateScore()
 
    def animateScore(self):
        #display score at 0 and every time interval add 100 until
        #we reach the final score
        #draw a score widget and schedule updates
        scoreText = 'Score: 0'# + str(self.finalScore)
        self.scoreLabel = Label(text=scoreText,font_size = '20sp')
        self.scoreLabel.x = Window.width*0.3
        self.scoreLabel.y = Window.height*0.3
        self.add_widget(self.scoreLabel)
        Clock.schedule_once(self.updateScore, .1)
        self.drawStars()
 
    def updateScore(self,dt):
        self.currentScore = self.currentScore +100
        self.scoreLabel.text = 'Score: ' + str(self.currentScore)
        if self.currentScore < self.finalScore:
            Clock.schedule_once(self.updateScore, 0.1)
 
    def drawStars(self):
        #0-10 asteroids 0 stars
        #11-50 asteroids 1 star
        #51-200 asteroids 2 stars
        #201-500 asteroids 3 stars
        #501-1000 asteroids 4 stars
        #1001+ asteroids 5 stars
        starNumber = 0
        if self.asteroidScore > 10:
            starNumber = 1
        if self.asteroidScore > 50:
            starNumber = 2
        if self.asteroidScore > 200:
            starNumber = 3
        if self.asteroidScore > 500:
            starNumber = 4
        if self.asteroidScore > 1000:
            starNumber = 5
 
        with self.canvas:
        #draw stars
        #rect one
            starPos = Window.width*0.27, Window.height*0.42
            starSize = Window.width*0.06,Window.width*0.06
            starString = 'gold_star.png'
        if starNumber < 1:
            starString = 'gray_star.png'
        starRectOne = Rectangle(source=starString,pos=starPos, size = starSize)
        #rect two
        starPos = Window.width*0.37, Window.height*0.42
        if starNumber < 2:
            starString = 'gray_star.png'
        starRectTwo = Rectangle(source=starString,pos=starPos, size = starSize)
        #rect three
        starPos = Window.width*0.47, Window.height*0.42
        if starNumber < 3:
            starString = 'gray_star.png'
        starRectThree = Rectangle(source=starString,pos=starPos, size = starSize)
        #rect four
        starPos = Window.width*0.57, Window.height*0.42
        if starNumber < 4:
            starString = 'gray_star.png'
        starRectFour = Rectangle(source=starString,pos=starPos, size = starSize)
        #rect five
        starPos = Window.width*0.67, Window.height*0.42
        if starNumber < 5:
            starString = 'gray_star.png'
            starRectFive = Rectangle(source=starString,pos=starPos, size = starSize)
 

class Asteroid(WidgetDrawer):
    #Asteroid class. The flappy ship will dodge these
    imageStr = './sandstone_1.png'
    rect_bg = Rectangle(source=imageStr)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0) 

    def move(self):                    
        self.x = self.x + self.velocity_x 
        self.y = self.y + self.velocity_y 
    def update(self): 
        self.move() 
        
class Ship(WidgetDrawer):
    #Ship class. This is for the main ship object. 
    #velocity of ship on x/y axis
 
    impulse = 3
    grav = -0.1
 
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    flameSize = (Window.width*.03, Window.width*.03)
 
    def move(self):                    
        self.x = self.x + self.velocity_x 
        self.y = self.y + self.velocity_y 
 
        if self.y <= Window.height*0.05:
            self.impulse = 1
            self.grav = -0.1
        if self.y >= Window.height*0.95:
            self.impulse = -3
            
    def checkBulletNPCCollision(self,j):
        if self.k.collide_widget(j):
            j.health = j.health - self.k.bulletDamage
            j.attackFlag = 'True'
            self.k.age = self.k.lifespan+10
 
    def checkBulletStageCollision(self,q):
        if self.k.collide_widget(q):
            try:
                if q.type == 'asteroid':
                    q.health = q.health - self.k.bulletDamage
                    self.k.age = self.k.lifespan+10
            except:
                print 'couldnt hit asteroid'

    def determineVelocity(self):
        #move the ship up and down
        #we need to take into account our acceleration
        #also want to look at gravity
        self.grav = self.grav*1.05  #the gravitational velocity should increase
        #set a grav limit
        if self.grav <= -4:
            self.grav = -4
        #the ship has a propety called self.impulse which is updated
        #whenever the player touches, pushing the ship up
        #use this impulse to determine the ship velocity
        #also decrease the magnitude of the impulse each time its used
 
        self.velocity_y = self.impulse + self.grav
        self.impulse = 0.95*self.impulse

    def drawArrow(self, *largs):
    #draw the arrows directly onto the canvas
        with self.canvas:
            flamePos = (self.pos[0]-Window.width*.02,self.pos[1]+Window.width*.01)
     
            flameRect = Rectangle(source='./flame.png',pos=flamePos, size = self.flameSize)
    #schedule removal
 
    def removeArrows(arrow, *largs):
        self.canvas.remove(arrow)
        Clock.schedule_once(partial(removeArrows, flameRect), .5)
        Clock.schedule_once(partial(self.updateArrows, flameRect), 0.1)
 
    def updateArrows(self,arrow,dt):
        with self.canvas:
            arrow.pos = (arrow.pos[0]-10,arrow.pos[1])
            Clock.schedule_once(partial(self.updateArrows, arrow), 0.1)
        return
 
    def explode(self):
        #create explosion 1
        tmpSize = Window.width*0.25,Window.width*0.2
        tmpPos = (self.x-Window.width*0.095, self.y-Window.width*0.08)
        with self.canvas: #create an explosion image, 
            self.explosionRect = Rectangle(source ='./explosion1.png',pos=tmpPos,size=tmpSize)
        
        def changeExplosion(rect, newSource, *largs):
            rect.source = newSource
 
        #schedule explosion two
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, './explosion2.png'),0.2)
        #schedule explosion three
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, './explosion3.png'),0.4)
        #schedule explosoin four
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, './explosion4.png'),0.6)
        Clock.schedule_once(partial(changeExplosion, self.explosionRect, './explosion5.png'),0.8)
        def removeExplosion(rect, *largs):
            self.canvas.remove(rect) #remove the explosion drawing
        Clock.schedule_once(partial(removeExplosion, self.explosionRect),1)
 
    def update(self):
        self.determineVelocity() #first figure out the new velocity
        self.move()              #now move the ship

class GUI(Widget):
    #this is the main widget that contains the game. 
    asteroidList =[] #use this to keep track of asteroids
    asteroidScore = NumericProperty(0)
    minProb = 1700 #this variable used in spawning asteroids
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)
        
        #setup label for the score
        self.score = Label(text = '0')
        self.score.y = Window.height*0.8
        self.score.x = Window.width*0.2
 
        def check_score(self,obj):
            #update credits
            self.score.text = str(self.asteroidScore)
        self.bind(asteroidScore = check_score)
        self.add_widget(self.score)
 
        #now we create a ship object
        self.ship = Ship(imageStr = './ship.png')
        self.ship.x = Window.width/4
        self.ship.y = Window.height/2
        self.add_widget(self.ship)
        #self.ship.drawArrow()#start the flames
        Clock.schedule_interval((self.ship.drawArrow), 0.1)
        
        ##l = Label(text='Flappy Ship') #give the game a title
        ##l.x = Window.width/2 - l.width/2
        ##l.y = Window.height*0.8
        ##self.add_widget(l) #add the label to the screen
 
        #now we create a ship object
         #notice how we specify the ship image
        self.ship = Ship(imageStr = './ship.png')
        self.ship.x = Window.width/4
        self.ship.y = Window.height/2
        self.add_widget(self.ship)
 
    def addAsteroid(self):
        #add an asteroid to the screen 
        #self.asteroid 
        imageNumber = randint(1,4)
        imageStr = './sandstone_'+str(imageNumber)+'.png'     
        tmpAsteroid = Asteroid(imageStr)
        tmpAsteroid.x = Window.width*0.99
 
        #randomize y position
        ypos = randint(1, 16)
        ypos = ypos*Window.height*.0625
        tmpAsteroid.y = ypos
        tmpAsteroid.velocity_y = 0
        vel = randint(10, 25)
        tmpAsteroid.velocity_x = -0.1*vel
        self.asteroidList.append(tmpAsteroid)
        self.add_widget(tmpAsteroid)
 
    def drawTouchResponse(self,x,y):
        #draw the arrows directly onto the canvas
        with self.canvas:
            tmpSize = Window.width*0.07, Window.width*0.07
            tmpPos = (x-self.width/4,y-self.height/4)
            self.arrowRect = Rectangle(source='./flame1.png',pos=tmpPos, size = tmpSize)
        #schedule removal
        def removeArrows(arrow, *largs):
            self.canvas.remove(arrow)
        def changeExplosion(rect, newSource, *largs):
            rect.source = newSource
        #schedule explosion two
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, './flame2.png'),0.15)
        #schedule explosion three
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, './flame3.png'),0.3)
        #schedule explosoin four
        Clock.schedule_once(partial(changeExplosion, self.arrowRect, './flame4.png'),0.45)
        Clock.schedule_once(partial(removeArrows, self.arrowRect),0.6)
 
#handle input events
    def on_touch_down(self, touch):
        self.ship.impulse = 3
        self.ship.grav = -0.1
        self.drawTouchResponse(touch.x,touch.y)
    def showScore(self):
        #this function will draw the score keeping widget, tabulate the score
        #and rank with stars
        self.scoreWidget = ScoreWidget()
        self.scoreWidget.asteroidScore = self.asteroidScore #pass on score
        self.scoreWidget.prepare()
        self.add_widget(self.scoreWidget)
    def removeScore(self):
        self.remove_widget(self.scoreWidget)
 
    def gameOver(self):
        #add a restart button
        restartButton = MyButton(text='Try Again')
        #restartButton.background_color = (.5,.5,1,.2)
        def restart_button(obj):
            #reset game
            self.removeScore()
 
            for k in self.asteroidList:
                self.remove_widget(k)
                self.ship.xpos = Window.width*0.25
                self.ship.ypos = Window.height*0.5
                self.minProb = 1780
                self.asteroidScore = 0
                self.asteroidList = []
 
            self.parent.remove_widget(restartButton)
            Clock.unschedule(self.update)
            Clock.schedule_interval(self.update, 1.0/60.0)
            restartButton.size = (Window.width*.3,Window.width*.1)
            restartButton.pos = Window.width*0.5-restartButton.width/2, Window.height*0.53
            restartButton.bind(on_release=restart_button)
            #we will want to bind the parent to listen for things from certain bubbles
 
        #*** It's important that the parent get the button so you can click on it
        #otherwise you can't click through the main game's canvas
            self.parent.add_widget(restartButton)
 
        #now draw the score widget
            self.showScore()
 
    def update(self,dt):
#This update function is the main update function for the game
#All of the game logic has its origin here
#events are setup here as well
 
        #update game objects
        #update ship
        self.ship.update()
        #update asteroids
        #randomly add an asteroid
        tmpCount = randint(1,1800)
        if tmpCount > self.minProb:
            self.addAsteroid()
            if self.minProb < 1300:
                self.minProb = 1300
            self.minProb = self.minProb -1
 
        for k in self.asteroidList:
            #check for collision with ship
            if k.collide_widget(self.ship):
                #game over routine
                self.gameOver()
                Clock.unschedule(self.update)
                #add reset button
                self.ship.explode()
                k.update()
        #check to see if asteroid is off of screen
            if k.x <  -100:
        #since it's off the screen, remove the asteroid
                self.remove_widget(k)
                self.asteroidScore = self.asteroidScore + 1
 
        #remove asteroids off screen
        tmpAsteroidList = self.asteroidList
        tmpAsteroidList[:] = [x for x in tmpAsteroidList if ((x.x > - 100))]
        self.asteroidList = tmpAsteroidList

class ClientApp(App):
 
    def build(self):
        #this is where the root widget goes
        #should be a canvas
        self.parent = Widget() #this is an empty holder for buttons, etc
 
        self.app = GUI()        
        self.sm = SmartStartMenu()
        self.sm.buildUp()
        def check_button(obj):
        #check to see which button was pressed
            if self.sm.buttonText == 'start':
                #remove menu
                self.parent.remove_widget(self.sm)
                #start the game
                print ' we should start the game now'
                Clock.unschedule(self.app.update)
                Clock.schedule_interval(self.app.update, 1.0/60.0)
                try:
                    self.parent.remove_widget(self.aboutText)
                except:
                    pass
            if self.sm.buttonText == 'about':
                self.aboutText = Label(text = 'Flappy Ship is made by Molecular Flow Games \n Check out: http://kivyspacegame.wordpress.com')
                self.aboutText.pos = (Window.width*0.45,Window.height*0.35)
                self.parent.add_widget(self.aboutText)
        #bind a callback function that repsonds to event 'on_button_release' by calling function check_button
        self.sm.bind(on_button_release = check_button)
        #setup listeners for smartstartmenu
        self.parent.add_widget(self.sm)
        self.parent.add_widget(self.app) #use this hierarchy to make it easy to deal w/buttons
        return self.parent

if __name__ == '__main__' :
    ClientApp().run()
