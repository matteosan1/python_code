import re

def getValue(l):
    #m = re.search(">(\w+)<", l)
    #m = re.search(">(?<=[0-9]+\s)([a-z]+\s)*[a-z]+(?!\s{2,})<", l)
    m = re.search("(?<=\w\s)([a-zA-Z]+\s)*[a-zA-Z]+<", l)
    if (m):
        return m.group(1)

def parseHTML():
    # return list with coscia, nome, monta, proprietario
    file = open("lista_cavalli.txt")
    lines = file.readlines()
    file.close()

    cavalli = list()
    for i in xrange(len(lines)):
        if ("<td align=\"center\"><font face=\"Georgia\">" in lines[i]):
            c = []
            c.append(int(getValue(lines[i])))
            i  = i + 1
            c.append(getValue(lines[i]))
            i  = i + 1
            c.append(getValue(lines[i]))
            c.append("")
            cavalli.append(c)

    print cavalli
