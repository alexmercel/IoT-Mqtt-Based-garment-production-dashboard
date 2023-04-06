import sqlite3

# Create a new database connection
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
c = conn.cursor()

# Create a new table in the database
c.execute('CREATE TABLE articles (id INTEGER PRIMARY KEY, name TEXT, description TEXT,status INTEGER)')

# Insert some data into the table
c.execute("INSERT INTO articles (name, description, status) VALUES ('Article 1', 'This is the description for Article 1',0)")
c.execute("INSERT INTO articles (name, description, status) VALUES ('Article 2', 'This is the description for Article 2',0)")
c.execute("INSERT INTO articles (name, description, status) VALUES ('Article 3', 'This is the description for Article 3',0)")

#show database
c.execute("SELECT * from articles")
print(c.fetchall())

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection objects
c.close()
conn.close()
