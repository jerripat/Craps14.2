import sqlite3
conn=sqlite3.connect('casino.db')
c=conn.cursor()

def init_bank(balance):
    c.execute("INSERT INTO bank (balance) VALUES (?)", (balance,))
    conn.commit()
init_bank(1000)

def init_point_table():
    c.execute('INSERT INTO point (point) VALUES (0)')
    conn.commit()

def init_data_history():
    c.execute('''INSERT INTO data_history (die1, die2, score, point) VALUES (0, 0, 0, 0)''')
    conn.commit()
