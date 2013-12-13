from random import randint
from time import sleep
import datetime
import subprocess

def checkTime(start):
    while(1):
        now = datetime.datetime.now()
        if (now > start):
            print "CI SIAMO!"
            break
        sleep(60)


def playOhOh(s):
    subprocess.call(["mplayer", "-msglevel all=-1:statusline=-1:cplayer=-1", s])
 
s = [] 
s.append("campanelli_slitta_e_hohoho.mp3")
s.append("campanelli_slitta.mp3")
s.append("hohoho.mp3")
s.append("hohoho_2.mp3")

start = datetime.datetime(2013, 12, 12, 18, 00, 00)
end = datetime.datetime(2013, 12, 12, 21, 00, 00)
checkTime(start)

while(1):
    attesa = randint(2, 10)
    print "Attesa: ", attesa
    sleep(attesa*60)
    suono = randint(0, 3)
    print "Suono: ", s[suono]
    playOhOh(s[suono])
    now = datetime.datetime.now()
    if (now > end):
        break
