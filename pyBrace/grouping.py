#! /usr/bin/python

gruppi = [23,17,4,6,15,5,11,9,2,8,7,6,9,9,19,4,15,11,9,11,3,24,14,7,2,19,20,11,16,4,13,17,4,14,22,6,4,22,8,6,20,4,6,20,5,23,7,8,20,15, 6, 23,17,4,6,15,5,11,9,2,8,7,6,9,9,19,4,15,11,9,11,3,24,14,7,2,19,20,11,16,4,13,17,4,14,22,6,4,22,8,6,20,4,6,20,5,23,7,8,20,15, 6]

gruppi.sort()

i = 0
while(i < len(gruppi)):
    if (gruppi[i] < 7):
        j = i + 1
        while (j < len(gruppi)):
            if (gruppi[i] + gruppi[j] == 7):
                gruppi[i] = 7
                gruppi.pop(j)
                break
            j += 1
    i += 1

temp = []
r = []
for i in gruppi:
    if (i%7 == 0):
        temp.append(i)
    else:
        r.append(i)

print temp, r
