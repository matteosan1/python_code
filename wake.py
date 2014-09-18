import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto('\xff'*6 + '\x00\x22\x19\x0e\x46\x5d'*16, ('137.138.82.72', 9))
