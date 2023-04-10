import sqlite3

conection = sqlite3.connect("data.db")

cursor = conection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS messages 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         value SMALLINT,
         fromWho TEXT
        );
    """)

def insert(arg):
        try:
                cursor.executemany("INSERT INTO messages (value, fromWho) VALUES (?, ?)", arg)
                conection.commit()
                print(arg)
                return 200
        except Exception as error:
                print(error)
                return 404


cursor.execute("SELECT * FROM messages;")
print(cursor.fetchall())