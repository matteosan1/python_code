import android
import sqlite3
import os

app = android.Android()

os.popen("ls").readlines()

#name = app.dialogGetInput("Enter your name: ", "Please enter your name: ").result
#app.dialogDismiss()

#app.dialogCreateAlert("CIAO !!!", "Ciao %s, come va ?" %name)
#app.dialogSetPositiveButtonText("OK")
#app.dialogShow()
#app.dialogGetResponse().result
#app.dialogDismiss()

#app.vibrate()

#conn = sqlite3.connect("/mnt/sdcard/sl4a/scripts/dumpfile.db")
#c = conn.cursor()

#rows = c.execute("select * from fantini where fantino=\"Aceto\"")
#app.dialogCreateAlert("Fantino")
#for r in rows:
#    app.dialogSetItems(r)
#app.dialogShow()
#response = app.dialogGetResponse().result

#result = app.ttsSpeak('Grande MatteoSoftuer')
