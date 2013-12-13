#! /usr/bin/python

import re

file = open("fanta.tex")

while 1:
    line = file.readline()
    if not line:
        break
    print line
