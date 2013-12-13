#import sqlite3
import android.database.sqlite

#conn = sqlite3.connect("dumpfile.db")

c = conn.cursor()

rows = c.execute("select * from fantini where fantino=\"Aceto\"")

for r in rows:
    print r
