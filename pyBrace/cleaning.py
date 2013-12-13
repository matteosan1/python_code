#! /usr/bin/python
import sys

def compare_min(a, b):
    s1 = min(a[1])
    s2 = min(b[1])
    if (s1 >= s2):
        return 1
    else:
        return -1
    
def compare(a, b):
    s1 = a[0] - sum(a[1])
    s2 = b[0] - sum(b[1])
    if (s1 > s2):
        return -1
    elif (s1 < s2):
        return 1
    else:
        if (len(a[1]) > len(b[1])):
            return 1
        else:
            return -1

d = [[56, [23, 14, 11, 7]], [56, [22, 9, 9, 11, 4]], [56, [11, 17, 4, 5, 4, 4, 7, 4]], [56, [11, 17, 16, 4, 6]], [56, [20, 20, 13, 2]], [56, [19, 19, 15, 2]], [56, [15, 14, 8, 11, 8]], [56, [20, 18, 3, 6, 6, 2]], [56, [11, 15, 13, 14]], [56, [20, 9, 9, 17]], [56, [20, 16, 14, 5]], [56, [23, 23, 9]], [56, [20, 24, 7, 4]], [56, [8, 4, 4, 3, 2, 11, 7, 15]], [28, [9, 19]], [28, [23, 4]], [28, [22, 5]], [28, [15, 6, 6]], [28, [24, 3]], [28, [6, 6, 15]], [28, [19, 8]], [28, [8, 20]], [28, [22, 6]], [28, [22, 5]], [21, [6, 8, 6]], [21, [9, 11]], [21, [20]], [14, [7, 7]], [7, [6]]] 

resto = [4, 6, 9] 

d.sort(lambda x, y: compare(x, y))
for n,t in enumerate(d):
    ratio = float(sum(t[1]))/float(t[0])
    if (ratio <= 0.5):
        temp = t[1]
        for i in temp:
            for j in d[n+1:]:
                posti_liberi = j[0] - sum(j[1])
                if (posti_liberi >= i):
                    j[1].append(i)
                    t[1].remove(i)

temp = []
for i in d:
    if (i[0] != sum(i[1])):
        temp.append(i)

#print resto
#for i in temp:
#    print i, i[0]-sum(i[1])

#print "-------"
while(1):
    fatto = False
    target = temp[0][0] - sum(temp[0][1])
    for i in temp[1:-1]:
        for j in i[1]:
            if (j == target and not fatto):
                temp.pop(0)
                i[1].remove(j)
                fatto = True

    temp.sort(lambda x, y: compare(x, y))
                
    for r in resto:
        for i in temp:
            if (i[0] - sum(i[1]) == r):
                resto.remove(r)
                temp.remove(i)

    temp.sort(lambda x, y: compare(x, y))

    if (len(resto) == 0):
        break

    if (not fatto):
        break

print resto
for i in temp:
    print i, i[0]-sum(i[1])

# fixing tavolo con 1
#for r in resto:
#    n_min = -1
#    m_min = 999999
#    for n,i in enumerate(temp):
#        m = min(i[1])
#        if (m+1 == r):
#            i[1].append(r)
#            i[1].remove(m)
#            break


for n,i in enumerate(temp[0:6]):
    print "ADESSO: ", i
    if (i[0] - sum(i[1]) == 0):
        continue
    m = min(i[1]) + i[0] - sum(i[1])
    resto.append(m)
    i[1].remove(min(i[1]))
    fixed = False
    for j in temp[n+1:]:
        if (i == j):
            continue
        for y in j[1]:
            if (y == m):
                j[1].remove(y)
                i[1].append(y)
                fixed = True
                break
        
        if (fixed):
            break
    temp.sort(lambda x, y: compare_min(x, y))
    
            
print resto
for i in temp:
    print i, i[0]-sum(i[1])

# aggiungi tavolino per finire resto
