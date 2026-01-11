import sqlite3
conn = sqlite3.connect('casino.db')
c = conn.cursor()


def point_table():
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS point
                 (id INTEGER PRIMARY KEY, point INTEGER default 0)''')

    conn.commit()

def data_history():
    c.execute("""
        CREATE TABLE IF NOT EXISTS data_history (
            id INTEGER PRIMARY KEY,
            die1 INTEGER,
            die2 INTEGER,
            score INTEGER,
            point INTEGER
        )
    """)
    conn.commit()


def Bank():
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS bank
                 (id INTEGER DEFAULT 1, 
                 balance INTEGER)''')
    conn.commit()

point_table()
data_history()
Bank()