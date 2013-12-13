#!/usr/bin/env python

"""
A simple echo client
"""
import pickle
import socket
import sys

host = 'localhost'
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', 1974))
a = [i for i in xrange(100)]
pickledList = pickle.dumps(a)
size = "%08d"%(sys.getsizeof(pickledList))
s.send(size)
s.send(pickledList)

data = s.recv(48)
print data
data = s.recv(int(data))
s.close()
print 'Received:', pickle.loads(data)

