import math

def fattore(s):
    i = 3
    while (i*int(s/i) !=s) and (i<=math.sqrt(s)):
        i = i+2
    print i, s/i
    return s/i

x = 45000001
while(x!=0):    
    x = fattore(x)
    
