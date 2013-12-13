#! /usr/bin/python
import re

def parser(s, tag):
    m = re.split("<"+tag+">(.+)</"+tag+">", s)
    if (m):
        return m
    return ""

r = re.compile("<td>|</td>")
file = open("output.html")
line = file.readlines()
lines = line[0].split("<tr>")
for line in lines:
    field = parser(line, "td")
    print field
    print 
#    if (len(fields) > 5):
#        tag = []
#        trueFields = [i for i in fields if i!= ""]
#        for i in xrange(len(trueFields)-1):
#            if i>2:
#                index = 3
#            else:
#                index = i
#            print trueFields[index], f[index]
#            m = re.search(f[index], trueFields[i])
#            if (m):
#                print "pippo"
#                tag.append(m.group(1))
#            elif ( trueFields[i] == "0"):
#                tag.append(trueFields[i])
#        if (tag[1] != "ALL" and tag[1] != "td"):
#            print tag
