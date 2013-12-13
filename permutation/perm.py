>>> for p in all_perms(['a','b','c']):
	print p


def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]



 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62

	

#!/usr/bin/env python

__version__ = "1.0"

"""xpermutations.py
Generators for calculating a) the permutations of a sequence and
b) the combinations and selections of a number of elements from a
sequence. Uses Python 2.2 generators.

Similar solutions found also in comp.lang.python

Keywords: generator, combination, permutation, selection

See also: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/105962
See also: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/66463
See also: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/66465
"""

from __future__ import generators

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
            
def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))

if __name__=="__main__":
    print "Permutations of 'love'"
    for p in xpermutations(['l','o','v','e']): print ''.join(p)

    print
    print "Combinations of 2 letters from 'love'"
    for c in xcombinations(['l','o','v','e'],2): print ''.join(c)

    print
    print "Unique Combinations of 2 letters from 'love'"
    for uc in xuniqueCombinations(['l','o','v','e'],2): print ''.join(uc)

    print
    print "Selections of 2 letters from 'love'"
    for s in xselections(['l','o','v','e'],2): print ''.join(s)

    print
    print map(''.join, list(xpermutations('done')))
