#! /usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="fisica",
                     db="palio")

cursor = db.cursor()
cursor.execute("select * from mosse")

result = cursor.fetchall()

for record in result:
    print record[0], " --> ", record[1]

