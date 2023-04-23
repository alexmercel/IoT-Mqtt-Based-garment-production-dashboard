import sqlite3
import os
def createnew():
    deletedb()
    # Create a new database connection
    conn = sqlite3.connect('mydatabasenew.db')

    # Create a cursor object
    c = conn.cursor()

    c.execute('CREATE TABLE inventory (rfid TEXT PRIMARY KEY,name TEXT,line TEXT,description TEXT)')
    c.execute('CREATE TABLE worklogs (rfid TEXT,stage_status INTEGER,operator TEXT,time_stamp TEXT, PRIMARY KEY (rfid,stage_status),FOREIGN KEY (rfid) REFERENCES inventory (rfid))')

    # Create a new table in the database
    # c.execute('CREATE TABLE articles (id TEXT PRIMARY KEY,rfid TEXT, name TEXT,line TEXT,description TEXT,status INTEGER,time TEXT)')

    # Insert some data into the table
    # c.execute("INSERT INTO articles (id,rfid,name,line, description, status,time) VALUES ('83c6e02e_0','83c6e02e','Article 1','A', 'This is the description for Article 1',0,'2023-04-11T04:14:32.292261')")
    # c.execute("INSERT INTO articles (id,rfid,name,line, description, status,time) VALUES ('fcf053d3_0','fcf053d3','Article 2','A', 'This is the description for Article 2',0,'2023-04-11T04:14:32.292261')")
    # c.execute("INSERT INTO articles (id,rfid,name,line, description, status,time) VALUES ('311c722e_0','311c722e','Article 3','B', 'This is the description for Article 3',0,'2023-04-11T04:14:32.292261')")
    # c.execute("INSERT INTO articles (id,rfid,name,line, description, status,time) VALUES ('4e56d3_0','4e56d3','Article 4','B', 'This is the description for Article 3',0,'2023-04-11T04:14:32.292261')")

    c.execute("INSERT INTO inventory (rfid,name,line, description) VALUES ('83c6e02e','Article 1','A', 'This is the description for Article 1')")
    c.execute("INSERT INTO inventory (rfid,name,line, description) VALUES ('fcf053d3','Article 2','A', 'This is the description for Article 2')")
    c.execute("INSERT INTO inventory (rfid,name,line, description) VALUES ('311c722e','Article 3','A', 'This is the description for Article 3')")
    c.execute("INSERT INTO inventory (rfid,name,line, description) VALUES ('4e56d3','Article 4','A', 'This is the description for Article 4')")


    #show database
    c.execute("SELECT * from inventory")
    print(c.fetchall())

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the connection objects
    c.close()
    conn.close()

def deletedb():
    os.remove('mydatabasenew.db')
