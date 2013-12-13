import sqlite3, re

def createDB(name):
    conn = sqlite3.connect(name)
    c = conn.cursor()
    c.execute("CREATE TABLE CMSCollaboration (name text, institution text, id int, mail text, status int)")
    conn.commit()
    conn.close()

def openDB(name):
    conn = sqlite3.connect(name)
    return conn

def insertInDB(conn, c):   
    r0 = re.compile("\d+\">(.*?)</a>")
    r1 = re.compile("InstNameCell\">(.*?)</td>")
    r2 = re.compile("sid=(\d+)\"")
    
    file = open("view-source.html")
    lines = file.readlines()
    file.close()
    
    it = -1
    collaborators = []
    for l in lines:
        if ("user_photo" in l):
            m = r0.search(l)
            if (m):
                it = 0
                collaborators.append([m.group(1), "", 0])
                
        if ("add_recommendation" in l):
            m = r2.search(l)
            if (m):
                it = 2
                collaborators[-1][2] = m.group(1)
                it = -1
                        
        if ("InstName" in l):
            m = r1.search(l)
            if (m):
                it = 1
                collaborators[-1][1] = m.group(1)
        
    for i in collaborators:
        i = i + ["@cern.ch", 0]
        print i
        c.execute("INSERT INTO CMSCollaboration VALUES(?,?,?,?,?)", i)
    conn.commit()
    conn.close()

def selectFromDB(c, name, inst, mail, status):
    c.execute('SELECT * FROM CMSCollaboration WHERE name like \'%'+name+'%\' OR institution like \'%'+inst+'%\' OR mail like \'%'+mail+'%\' OR status='+str(status))
    return c.fetchall()


#createDB("cms.db")
#insertInDB(conn, c)

#conn = openDB("cms.db")
#c = conn.cursor()
#it = selectFromDB(c, "Matteo", "-1" ,"-1" , -1)
#for i in it:
#    print i
