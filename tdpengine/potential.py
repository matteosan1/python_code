def u1(type, d):
    if (type == 0):
        return 0

    potential = 0
    if (d == 1):
        potential = 2
    if (d == 2):
        potential = 4
    if (d > 2):
        potential = 8

    return potential
        
        

def u2(vl, d, dt):
    if (vl*dt > d):
        return 0
    
    return d*d
    
def u3():
    # limitare la possibilita` di curvare in un dt
    # accelera e/o decelera
    # salita al casato
    # discesa san martino
    # rallenta in curva
    # cavallo scosso
