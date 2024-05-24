import sqlite3

conn = sqlite3.connect('store_database.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS categories (
    code TEXT PRIMARY KEY,
    title TEXT
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    category_code TEXT,
    unit_price REAL,
    stock_quantity INTEGER,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories (code),
    FOREIGN KEY (store_id) REFERENCES store (store_id)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS store (
    store_id INTEGER PRIMARY KEY,
    title TEXT
)
''')

cur.execute("INSERT INTO categories (code, title) VALUES ('FD', 'Food products')")
cur.execute("INSERT INTO store (store_id, title) VALUES (1, 'Asia')")
cur.execute("INSERT INTO store (store_id, title) VALUES (2, 'Globus')")
cur.execute("INSERT INTO store (store_id, title) VALUES (3, 'Spar')")
cur.execute("INSERT INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (1, 'Chocolate', 'FD', 10.5, 129, 1)")

conn.commit()
cur.close()
conn.close()
