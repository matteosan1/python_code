import re

keys = ["Frey N.", "Frey S.", "Sani"]

cognomi = ["Frey Nicola", "Frey Simone", "Sani Matteo Andrea"]
nomi = ["Nicola", "Simone", "Matteo"]

for ind, g in enumerate(cognomi):
    matches = []
    n = g[0]
    for iteration in xrange(1, len(g)):
        matches = [string for string in keys if re.match("^"+n, string)]
        if (len(matches) < 2):
            break
        n = g[0:iteration]
        
    if (len(matches) == 1):
        print matches[0]
    else:
        print "Not found"
