import subprocess,os, re

def checkSize():
    r = re.compile("Length: (\d+)")
    A = "/Users/sani/python/4giorniDiPalio/palio_new.db"

    statinfo1 = subprocess.check_output("wget --spider http://sani.web.cern.ch/sani/palio_new.db", stderr=subprocess.STDOUT, shell=True)
    statinfo2 = subprocess.check_output("ls -l %s"%A, shell=True)

    lenLocal = 0
    lenRemote = 0
    s = r.search(statinfo1)
    if (s):
        lenRemote = int(s.group(1))
        lenLocal = int(statinfo2.split()[4])

    return (lenLocal == lenRemote)

def getUpdatedDB():
    # controlla eventuali errori di connessione
    subprocess.call("mv palio_new.db palio_new.db_old", shell=True)
    subprocess.call("wget http://sani.web.cern.ch/sani/palio_new.db", shell=True)
