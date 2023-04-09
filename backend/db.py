import sqlite3

conection = sqlite3.connect("data.db")

cursor = conection.cursor()

cursor.execute("""CREATE TABLE messages
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         value TEXT)
    """)