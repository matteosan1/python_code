
def PointOnCubicBezier(cp, t):
    
    cx = 3.0 * (cp[1][0] - cp[0][0])
    bx = 3.0 * (cp[2][0] - cp[1][0]) - cx
    ax = cp[3][0] - cp[0][0] - cx - bx
    
    cy = 3.0 * (cp[1][1] - cp[0][1])
    by = 3.0 * (cp[2][1] - cp[1][1]) - cy
    ay = cp[3][1] - cp[0][1] - cy - by
    
    t = t / 2

    tSquared = t * t 
    tCubed = tSquared * t
    
    result = [(ax * tCubed) + (bx * tSquared) + (cx * t) + cp[0][0],
              (ay * tCubed) + (by * tSquared) + (cy * t) + cp[0][1]]
    
    return result;


numberOfPoints = 4;    
cp = [(0, 0), (0, 1), (0, 2), (0, 3),
      (0, 4), (0, 5), (0, 6), (0, 7)]
 
dt = 2.0 / ( numberOfPoints - 1 );

for i in xrange(0,numberOfPoints):
    print PointOnCubicBezier(cp, i*dt)

    
