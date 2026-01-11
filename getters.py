import sqlite3

conn = sqlite3.connect('casino.db')
c = conn.cursor()

def get_bank_balance():
    c.execute('SELECT balance FROM bank WHERE id = 1')
    return c.fetchone()

def get_point():
    c.execute('SELECT point FROM point WHERE id = 1')
    return c.fetchone()
