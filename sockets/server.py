import socket

host    = ''
port    = 1974
backlog = 5
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(48)
    #print data

    client.send(data)

    data = client.recv(int(data))

    if data:
        client.send(data)
    client.close()
