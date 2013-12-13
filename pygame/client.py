import socket
import pickle
import sys
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', 1974))

buf = []
pseudo_buf = []
tot_data = ""
while 1:
    data = s.recv(20000)
    tot_data = tot_data + data
    dati = tot_data.split("DATI")[0:-1]
    tot_data = tot_data.split("DATI")[-1]
    buf = buf + [pickle.loads(i)[0] for i in dati if i != ""]
    #pseudo_buf = pseudo_buf + [pickle.loads(i)[1] for i in dati if i != ""]

    # Controlla se il server e` morto
    if (data == ""):
        r, w, e = select.select([s],[],[s], 0)
        if (r):
            s.close()
        break

print buf
