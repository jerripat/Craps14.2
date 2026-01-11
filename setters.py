import sqlite3

conn = sqlite3.connect('casino.db')
c = conn.cursor()

def update_bank_balance(id, balance):
    c.execute('UPDATE bank SET balance =? WHERE id =?', (balance, id))
    conn.commit()

def update_point(id, point):
    c.execute('UPDATE point SET point =? WHERE id =?', (point, id))
    conn.commit()

def update_data_history(die1, die2, score, point):
    c.execute('INSERT INTO data_history (die1, die2, score, point) VALUES (?,?,?,?)', (die1, die2, score, point))
    conn.commit()
