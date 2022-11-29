import sqlite3
con = sqlite3.connect("dbtest.db")
cursor = con.cursor()

cursor.execute("create table info(Name TEXT , Age INT , Address TEXT)")
print("done")