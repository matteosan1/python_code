import random, sys, math
import socket, pickle, bisect

def rho(p1, p2):
    r = math.sqrt(math.pow(p1[0]-p2[0], 2) + math.pow(p1[1]-p2[1], 2))
    return r

class Cavallo:
    def __init__(self, n):
        self.nome = n
        self.scatto = 1
        self.vel_max = int(random.uniform(40, 60))
        self.resistenza = int(random.uniform(50,100))
        self.precisione = int(random.uniform(0,2))
        self.allenamento = 1

class Point:
    def __init__(self):
        self.coord = (0,0)
        self.angle = 0
        self.val = 0
        self.pos = 0
        self.leafs = (0,0,0)
        self.indice = -1
    
    def set_point(self, i, p):
        self.indice = i
        self.coord = (int(p[0]), int(p[1]))
        self.angle = float(p[2])
        self.val = int(p[3])
        self.pos = int(p[4])
        self.leafs = (int(p[5]), int(p[6]), int(p[7]))

class Barbero():
    def __init__(self, n, i):
        self.cavallo = Cavallo(n)
        self.pos = Point()
        self.t = 0
        self.giro = 0
        self.traiettoria = []
        self.tempo_indice = []
        self.velocita = 0
        self.riserva = self.cavallo.resistenza*self.cavallo.allenamento
        self.scosso = True
        self.indice = i

    def setPosizione(self, p):
        self.pos = p

    def accelera(self):
        self.velocita += self.cavallo.scatto 
        self.riserva -= 5 # FIXME

    def decelera(self):
        self.velocita -= self.cavallo.scatto 

def ordinaBarberiFunc(b1, b2):
    if (b1.giro < b2.giro):
        return 1
    elif (b1.giro > b2.giro):
        return -1
    else:
        if ((b1.pos.pos <= b2.pos.pos) or
            ((b1.pos.pos == b2.pos.pos) and (b1.pos.val > b2.pos.val))):
            return 1
        return -1

def ordinaPathsFunc(p1, p2):
    if (p1[0] == p2[0]):
        return (abs(p1[1]) < abs(p2[1]))
    else:
        return (p1[0] < p2[0])

class Engine():
    def __init__(self, n):
        self.barberi = [Barbero(n[i], i) for i in xrange(len(n))]    
        self.piazza = []
        self.ordine = []
        self.corsaFinita = False        
        self.timerInterno = 0.0

        self.serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.serversocket.bind(('localhost', 1974))
        self.serversocket.listen(1)
        self.client_sockets = []
        (clientsocket, address) = self.serversocket.accept()
        self.client_sockets.append(clientsocket)

    def loadMap(self):
        file = open("mappa_piazza2.csv")
        lines = file.readlines()
        for i, line in enumerate(lines):
            numbers = (line.split("\n")[0]).split(",")
            p = Point()
            p.set_point(i, numbers)
            self.piazza.append(p)
        
    def mossa(self):
        temp = []
        for i, b in enumerate(self.barberi):
            b.setPosizione(self.piazza[217+i])
            temp.append([i, [0.0, b.pos.coord, b.pos.angle]])
            b.accelera()
        return temp
        
    def getPositions(self):
        posList = []
        for b in self.barberi:
            posList.append([b.indice, b.pos_int.coord, b.pos.coord, b.velocita])
        
        return posList
  
    def dist(self, p, b2):
        return (((p.pos-b2.pos), abs(p.val)-abs(b2.val)))

    def ordinaBarberi(self):
        self.barberi = sorted(self.barberi, cmp=ordinaBarberiFunc)

    def handicap(self, leaf, t, precisione):
        if (leaf != -1):
            h = abs(self.piazza[leaf].val + precisione)

            for y in xrange(len(self.barberi)):
                dx=9999.
                dy=9999.
                
                #for p in self.barberi[y].tempo_indice:
                #    if ((abs(p[0])-t) < (1./self.barberi[y].velocita)):
                #        dx = self.dist(self.piazza[leaf], self.piazza[p[1]])[0]
                #        dy = self.dist(self.piazza[leaf], self.piazza[p[1]])[1]
                #        break
                    
                #print dx, dy

                if ((dy > 2) or (dx > 0) or (dx < -2)):
                    h = h + 0
                elif (dy < 1):
                    h = h + 2
                elif (dy == 0 and dx == -2):
                    h = h + 4
                elif (dy == 0 and dx == -1):
                    h = h + 8
                elif (dy == 0 and dx == 0):
                    h = h + 9999
                else:
                    h = h + 2
            #print h
            return h

    def isVicoloCieco(self, leaf, v, direzione):
        for i in xrange(v):
            new_leaf = self.piazza[leaf].leafs[1]
            if (new_leaf == -1):
                if (self.piazza[leaf].leafs[direzione] == -1):
                    return v-i
                else:
                    new_leaf = self.piazza[leaf].leafs[direzione]
    
        return 0
    
    def fineCorsa(self):
        print "ARRIVO:"
        for b in engine.barberi:
            print "%s\t\t %d %d %d %d"%(b.cavallo.nome, b.pos.pos, b.pos.val, b.velocita, b.giro)

    def move(self):
        self.timerInterno += 1.0
        for z,b  in enumerate(self.barberi):
            turns = [-1, 0, 1]
            paths = [[self.handicap(l, self.timerInterno, b.cavallo.precisione), turns[j], l] for j,l in enumerate(b.pos.leafs) if (l != -1)]

            iterations = b.velocita        
            for iteration in xrange(iterations):
                t = iteration/iterations+self.timerInterno
                temp_paths = []
                #print len(paths)
                for path in paths:
                    current_val = self.piazza[path[-1]].val
                    #print path[-1]
                    #print self.piazza[path[-1]].leafs
                    #print self.piazza[path[-1]].coord
                    for leaf in self.piazza[path[-1]].leafs:
                        if (leaf != -1):
                            handy = self.handicap(leaf, t, b.cavallo.precisione)
                            if (handy >= 9999):
                                continue

                            deltaX = self.piazza[leaf].val - current_val
                            if (deltaX * path[1] < 0):
                                continue

                            if (deltaX != 0):
                                path[1] = deltaX
                                handy += self.isVicoloCieco(leaf, (iterations-iteration), path[1]+1)
                            #print [path[0]+handy] + [path[1]] + path[2:]+[leaf]
                            temp_paths.append([path[0]+handy] + [path[1]] + path[2:]+[leaf])

                # cleaning
                temp_paths = sorted(temp_paths, cmp=ordinaPathsFunc)
                if (len(temp_paths) != 0):
                    #print "temp_paths", temp_paths
                    paths = temp_paths[0:3]
                else:
                    if (iteration < b.velocita):
                        b.velocita = iteration-1
                        # INFORUNIO CAVALLO !!!
                        break

            if (len(paths) > 0):
                dist = b.t
                indice = 2
                for i in xrange(int(b.velocita)):
                    step = max(0,self.piazza[paths[0][indice]].val)
                    if (step > 6):
                        step = 6
                    dist += (1 - step*.15)                    
                    indice = int(dist) + 2
                    b.t = dist%1.0

                b.tempo_indice = []
                b.traiettoria = [b.indice]
                if (indice > 2):
                    b.pos = self.piazza[paths[0][indice-1]]

                if (len(paths[0][2:indice]) > 0):
                    punto_di_arrivo = self.piazza[paths[0][indice-1]].coord
                    old_ang = 0.0
                    for n, i in enumerate(paths[0][2:indice]):
                        punto_corrente = self.piazza[i].coord
                        ang = math.atan2(punto_di_arrivo[1]-punto_corrente[1], punto_di_arrivo[0]-punto_corrente[0])
                        if (n == indice - 3):
                            ang = old_ang
                        old_ang = ang
                        b.traiettoria.append([float(n)/b.velocita+self.timerInterno, punto_corrente, ang])
                        b.tempo_indice.append((float(n)/b.velocita+self.timerInterno, self.piazza[i].indice))
                        
                    npath = len(paths[0][2:indice])
                    if ((bisect.bisect_left(paths[0][2:indice], 217) > 0) and
                        (bisect.bisect_right(paths[0][2:indice], 228) < npath)):
                        b.giro = b.giro + 1
                        if (b.giro > 2):
                            self.corsaFinita = True

                else:
                    b.traiettoria.append([self.timerInterno, b.pos.pos, b.pos.angle])
                    b.tempo_indice.append((self.timerInterno, b.pos.indice))

            # velocita
            if (b.scosso):
                if ((b.pos.pos > 150 and b.pos.pos < 178) or
                    (b.pos.pos > 280 and b.pos.pos < 302)):
                    velocita_limite = 8
                    if (b.velocita > velocita_limite):
                        b.decelera()
                else:
                    if (b.velocita < b.cavallo.vel_max*.5): # lo scosso va al massimo alla meta`
                        b.accelera()
            else: # Non e` scosso
                # sceglie il fantino
                if ((b.pos.pos > 150 and b.pos.pos < 178) or
                    (b.pos.pos > 280 and b.pos.pos < 302)):
                    velocita_limite = 8
                    if (b.velocita > velocita_limite):
                        b.decelera()
                else:
                    if (b.velocita < b.cavallo.vel_max*.5): # lo scosso va al massimo alla meta`
                        b.accelera()
            
            # stanchezza
            if (b.velocita > b.cavallo.vel_max*0.9):
                b.riserva -= 2
            else:
                b.riserva  -= 1

if __name__ == "__main__":
    nomi = ("Panezio", "Benito", "Zuccher", "Rimini", "Uberto", "Danubio", "Zodiach", "Pytheos", "Gallegg", "Figaro")

    engine = Engine(nomi)
    #for e in engine.barberi:
    #    print e.cavallo.nome, e.cavallo.vel_max
    
    engine.loadMap()
    traiettorie_tot = []
    traiettorie_tot.append(engine.mossa())
    #while 1:
    for i in range(3):
        engine.move()
        engine.ordinaBarberi()
        traiettorie = []
        #print "--------------"
        for b in engine.barberi:
            #print "%s\t\t %d %d %d"%(b.cavallo.nome, b.pos.pos, b.pos.val, b.velocita), b.giro
            traiettorie.append(b.traiettoria)
        traiettorie_tot.append(traiettorie)
        #print traiettorie_tot
        #sys.exit(0)

        pickledTraiettorie = pickle.dumps(traiettorie_tot)
        for s in engine.client_sockets:
            s.send("DATI")
            s.send(pickledTraiettorie)
        traiettorie_tot = []

        if (engine.corsaFinita):
            engine.fineCorsa()
            for s in engine.client_sockets:
                s.send("DATI")
            engine.client_sockets[0].shutdown(socket.SHUT_RDWR)
            engine.client_sockets[0].close()
            sys.exit(1)

