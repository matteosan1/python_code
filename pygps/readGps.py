#!/usr/bin/python
from xml.sax import make_parser, handler
import gpshandler

parser = make_parser()
handler = gpshandler.GpsHandler()
parser.setContentHandler(handler)
parser.parse("/home/sani/gps/tracks/06_06_2010_lac_darbon.gpx")

tracks = handler.tracks

#for i in handler.track.points:
#    print i

for track in tracks:
    print track.number,  track.name
    print track.highestSpeed()
    print track.lowestSpeed()
    print track.highestHeight()
    print track.lowestHeight()

