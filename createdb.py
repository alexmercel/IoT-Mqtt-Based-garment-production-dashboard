import sqlite3

# Create a new database connection
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
c = conn.cursor()

# Create a new table in the database
c.execute('CREATE TABLE articles (id INTEGER PRIMARY KEY, name TEXT,line TEXT,description TEXT,status INTEGER,time TEXT)')

# Insert some data into the table
c.execute("INSERT INTO articles (name,line, description, status,time) VALUES ('Article 1','A', 'This is the description for Article 1',0,'2023-04-11T04:14:32.292261')")
c.execute("INSERT INTO articles (name,line, description, status,time) VALUES ('Article 2','A', 'This is the description for Article 2',0,'2023-04-11T04:14:32.292261')")
c.execute("INSERT INTO articles (name,line, description, status,time) VALUES ('Article 3','B', 'This is the description for Article 3',0,'2023-04-11T04:14:32.292261')")

#show database
c.execute("SELECT * from articles")
print(c.fetchall())

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection objects
c.close()
conn.close()
