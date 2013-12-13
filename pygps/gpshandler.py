import xml.sax.handler
import math 

class TkPoint():
    def __init__(self):
        self.lat = 0
        self.lon = 0
        self.ele = 0.0
        self.time = ""
        self.fix = ""
        self.hdop = 0
        self.vdop = 0
        self.pdop = 0
        self.speed = 0
        self.hdg = 0
        self.hacc = 0
        self.vacc = 0
        self.sat = []
    def __str__(self):
        a = "Lat: "+ str(self.lat)
        a = a + " Lon: " + str(self.lon)
        return a

class Track():
    def __init__(self):
        self.points = []
        self.name = ""
        self.number = -1

    #def time(self):
    #    sdfsdf

    def distance(self):
        dist = 0
        r = 6372.
        for i in xrange(len(self.points)-1):
            rsinThetaDPhi = r*math.cos(math.radians(self.points[i+1].lat))* (math.radians(self.points[i+1].lon - self.points[i].lon))
            rDPhi = r*math.radians(self.points[i+1].lat - self.points[i].lat)
            dist = dist + math.sqrt(pow(rDPhi,2) + pow(rsinThetaDPhi,2))

        return dist
    
    def latitudes(self):
        x = [i.lat for i in self.points]
        return x

    def longitudes(self):
        x = [i.lon for i in self.points]
        return x
    
    def elevations(self):
        x = [i.ele for i in self.points]
        return x

    def speeds(self):
        x = [i.speed for i in self.points]
        return x
        
    def highestSpeed(self):
        x = [i.speed for i in self.points]
        return max(x)

    def lowestSpeed(self):
        x = [i.speed for i in self.points]
        return min(x)

    def lowestHeight(self):
        x = [i.ele for i in self.points]
        return min(x)

    def highestHeight(self):
        x = [i.ele for i in self.points]
        return max(x)

        
class GpsHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.point = TkPoint()
        self.buffer = ""
        self.track = Track()
        self.tracks = []
        
    def allTracks(self):
        at = Track()
        for i in self.tracks:
            for p in i.points:
                at.points.append(p)
        at.name = "Global Track"
        at.number = -1
        return at

    def startElement(self, name, attributes):
        # put trkseg
        if name == "name":
            self.buffer = ""
        if name == "number":
            self.buffer = ""

        if name == "trkpt":
            self.point = TkPoint()
            self.point.lat = float(attributes["lat"])
            self.point.lon = float(attributes["lon"])
        elif name == "gpslog:sat":
            if (attributes["used"] == "true"):
                self.point.sat.append((int(attributes["az"]),
                                       int(attributes["ele"]),
                                       int(attributes["prn"]),
                                       int(attributes["signal"])))

        elif name == "ele":
            self.buffer = ""
            self.inEle = 1
        elif name == "time":
            self.buffer = ""
            self.inTime = 1
        elif name == "fix":
            self.buffer = ""
            self.inFix = 1
        elif name == "hdop":
            self.buffer = ""
            self.inHdop = 1
        elif name == "vdop":
            self.buffer = ""
            self.inVdop = 1
        elif name == "pdop":
            self.buffer = ""
            self.inPdop = 1
        elif ("speed" in name): # == "mtk:speed":
            self.buffer = ""
            self.inSpeed = 1
        elif name == "gpslog:hdg":
            self.buffer = ""
            self.inHdg = 1
        elif name == "gpslog:hacc":
            self.buffer = ""
            self.inHacc = 1
        elif name == "gpslog:vacc":
            self.buffer = ""
            self.inVacc = 1
 
    def characters(self, data):
        self.buffer += data
        
    def endElement(self, name):
        if name == "name":
            self.track.name = self.buffer
        if name == "number":
            self.track.number = int(self.buffer)
        if name == "trk":
            self.tracks.append(self.track)
            self.track = Track()
        if name == "trkpt":
            self.track.points.append(self.point)
        elif name == "ele":
            self.inEle = 0
            ele = ""
            if ("." in self.buffer):
                ele = ele.join(self.buffer.split(".")[0:-1])
            else:
                ele = self.buffer
            self.point.ele = int(ele)
        elif name == "time":
            self.inTime = 0
            self.point.time = self.buffer
        elif name == "fix":
            self.inFix = 0
            self.point.fix = self.buffer
        elif name == "hdop":
            self.inHdop = 0
            self.point.hdop = self.buffer
        elif name == "Vdop":
            self.inVdop = 0
            self.point.vdop = self.buffer
        elif name == "pdop":
            self.inPdop = 0
            self.point.pdop = self.buffer
        elif ("speed" in name): # == "mtk:speed":
            self.inSpeed = 0
            self.point.speed = float(self.buffer)
        elif name == "gpslog:hdg":
            self.inHdg = 0
            self.point.hdg = float(self.buffer)
        elif name == "gpslog:hacc":
            self.inHacc = 0
            self.point.hacc = float(self.buffer)
        elif name == "gpslog:vacc":
            self.inVacc = 0
            self.point.vacc = float(self.buffer)
