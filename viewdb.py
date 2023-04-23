import sqlite3
from datetime import datetime

# Create a new database connection
conn = sqlite3.connect('mydatabasenew.db')

# Create a cursor object
c = conn.cursor()
#show database
ts= datetime.now().isoformat()
# c.execute("INSERT INTO worklogs (rfid,stage_status,operator,time_stamp) VALUES  ('ef34tr',1,'Mohan',?)",(ts,))
# c.execute("SELECT * from worklogs")
c.execute('SELECT w.time_stamp, w.rfid, i.name, i.description, w.stage_status FROM inventory i, worklogs w WHERE w.rfid = i.rfid ORDER BY w.time_stamp DESC')
print(c.fetchall())
# conn.commit()
c.close()
conn.close()