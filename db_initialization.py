import sqlite3

conn = sqlite3.connect("./database/calendar.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS calendar (Day DATE, Type VARCHAR(255), Subject VARCHAR(255), Description TEXT)"
            )
conn.commit()

cur.close()
conn.close()