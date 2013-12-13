import math

mu =0.6
R = 20.
alpha = 0.0
v = math.sqrt(R*9.81)*math.sqrt((alpha+mu)/(1-mu*alpha))
print v
