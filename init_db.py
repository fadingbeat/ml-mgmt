import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO models (m_name, m_description, m_version) VALUES (?, ?, ?)",
            ('Model 1', 'Content for the first model', 'v1.0')
            )
cur.execute("INSERT INTO models (m_name, m_description, m_version) VALUES (?, ?, ?)",
            ('Model 2', 'Content for the second model', 'v1.01')
            )

sql = "SELECT * FROM models"

# Execute the SQL statement
cur.execute(sql)

# Fetch all rows from the result set
rows = cur.fetchall()

# Print the contents of the table
for row in rows:
    print(row)

connection.commit()
connection.close()