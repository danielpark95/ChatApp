import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
	connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users(user_id, password, first_name, last_name) VALUES (?, ?, ?, ?)",
		("danielpark95", "123", "Daniel", "Park"))

cur.execute("INSERT INTO users(user_id, password, first_name, last_name) VALUES (?, ?, ?, ?)",
		("won2001", "456", "Won", "Kim"))

connection.commit()
connection.close()
