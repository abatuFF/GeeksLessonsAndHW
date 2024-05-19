import sqlite3



def create_connetion(db_name):
    connetion = None
    try:
        connetion = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(error)
    return connetion

def create_talbe(connetion, sql):
    try:
        cursor = connetion.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

sql_to_create_employees_table = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY, AUTOINCREMENT,
    full_name VARCHAR(200 NOT NULL,
    salary FLOAT(8, 2) DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_date DATE NOT NULL,
    is_married BOOLEAN DEFAULT False
)
'''

my_connetion = create_connetion('test.db')
if my_connetion:
    print('Connected successfully!')
    (my_connetion, sql_to_create_employees_table)
    my_connetion.close()

