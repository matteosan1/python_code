def move(self):
    self.timerInterno += 1.0
    for z,b  in enumerate(self.barberi):
        cambioDirezione = [-1, 0, 1]
        paths = [[self.handicap(k, self.timerInterno, b.cavallo.precisione), turns[j], k] for j,k in enumerate(b.pos.leafs) if (k != -1)]

        iterazions = b.velocita
        if (not b.scosso):
            iterations *= 2 
        
        for it in xrange(iterations):
            t = it/iterations + self.timerInterno
            temp_paths = []
            for p in paths:
                current_val = self.piazza[p[-1]].val
                for leaf in self.piazza[path[-1]].leafs:
                    if (leaf != -1):
                        # non puo` girare piu` di una volta a mossa "a parte in curva"
                        deltaX = self.piazza[leaf].val - current_val
                        if (deltaX * path[1] < 0):
                            continue

                            handy = self.handicap(leaf, t, b.cavallo.precisione)
                            if (handy >= 9999):
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
