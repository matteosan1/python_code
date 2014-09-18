import math
l = 7
a = 1.
h = 5
counter = 0
checkval = 1
outputfile = open('newtonOutput.txt', 'a') 
sep = '\t'
header = 'value for f(x)'+sep+'value for f\'(x)'+sep+'T_0_n'+sep+'T_0_n+1'+'\n' 
outputfile.write(header)
while checkval > 0.1:
    value = l/a
    fx = a+h-a*math.cosh(value)
    fprimex = 1-math.cosh(value)+value*math.sinh(value)
    a_n_1 = a - fx/fprimex
    a_1 = a
    checkval = abs(a_n_1 - a_1)
    a=a_n_1
    counter+=1
    dataline = str(fx) + sep + str(fprimex) + sep + str(a_1) + sep + str(a_n_1)+'\n' 
    outputfile.write(dataline)
print 'The value T_0/w is approximated to be : ' + str(a_n_1) +'\n'+'The difference between iterations is ' + str(checkval)+ ' ft' +'\n'+ 'After: ' +str(counter) + ' iterations'
l = a_n_1*math.sinh(l*1/a_n_1)
print 'The length of the cable is ' +str(l)+ ' ft' 
outputfile.close()
