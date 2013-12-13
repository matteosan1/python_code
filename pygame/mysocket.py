import socket
import sys

class mysocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
            
    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        size = self.sock.send(str(sys.getsizeof(msg)))
        while totalsent < int(size):
            sent = self.sock.send(str(msg[totalsent:]))
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        msg = ''
        size = self.sock.recv(sys.getsizeof(int()))
        print size
        while len(msg) < int(size):
            chunk = self.sock.recv(int(size)-len(msg))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            msg = msg + chunk
        return msg
