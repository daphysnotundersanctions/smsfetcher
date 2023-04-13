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
                cursor.execute("INSERT INTO messages (value, fromWho) VALUES (?, ?)", (arg.value, arg.fromWho))
                conection.commit()
                print(arg)
                return 200
        except Exception as error:
                print(error)
                return 404


def returnData():
        cursor.execute("SELECT * FROM messages;")
        row = cursor.fetchall() 
        headers = ['id','value','fromWho']
        result = [zip(headers,i) for i in row]
        return result


cursor.execute("SELECT * FROM messages;")
print([cursor.fetchall()])