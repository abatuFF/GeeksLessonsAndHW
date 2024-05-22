import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(error)
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)


def insert_employee(connection, employee):
    try:
        sql = '''
            INSERT INTO employees 
            (full_name, salary, hobby, birth_date, is_married)
            VALUES 
            (?, ?, ?, ?, ?)
        '''
        cursor = connection.cursor()
        cursor.execute(sql, employee)
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def update_employee(connection, employee):
    try:
        sql = '''
            UPDATE employees SET salary = ?, is_married = ?
            WHERE id = ?            
        '''
        cursor = connection.cursor()
        cursor.execute(sql, employee)
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def delete_employee(connection, id):
    try:
        sql = '''
            DELETE FROM employees WHERE id = ?            
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def select_all_employees(connection):
    try:
        sql = '''SELECT * FROM employees'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def select_employees_by_salary(connection, limit):
    try:
        sql = '''SELECT * FROM employees WHERE salary >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


sql_to_create_employees_table = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(200) NOT NULL,
    salary FLOAT(8, 2) DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_date DATE NOT NULL,
    is_married BOOLEAN DEFAULT FALSE
)
'''
my_connection = create_connection('group_42.db')
if my_connection:
    print('Connected successfully to database!')
    create_table(my_connection, sql_to_create_employees_table)
    insert_employee(my_connection,
                    ('Jim Brown', 2500.5, 'Programming', '2000-01-01', False))
    insert_employee(my_connection, ('Mark Daniels', 1500.0, 'Football', '1999-01-02', False))
    insert_employee(my_connection, ('Alex Brilliant', 2300.5, None, '1989-12-31', True))
    insert_employee(my_connection, ('Diana Julls', 1800.0, 'Programming', '2005-01-22', True))
    insert_employee(my_connection, ('Michael Corse', 1800.0, 'Football', '2001-09-17', True))
    insert_employee(my_connection, ('Jack Moris', 2100.2, 'Programming', '2001-07-12', True))
    insert_employee(my_connection, ('Viola Manilson', 1750.82, None, '1991-03-01', False))
    insert_employee(my_connection, ('Joanna Moris', 1000.0, 'Football', '2004-04-13', False))
    insert_employee(my_connection, ('Peter Parker', 2000.0, 'Programming', '2002-11-28', False))
    insert_employee(my_connection, ('Paula Parkerson', 800.09, None, '2001-11-28', True))
    insert_employee(my_connection, ('George Newel', 1320.0, 'Programming', '1981-01-24', True))
    insert_employee(my_connection, ('Miranda Alistoun', 2500.55, 'Football', '1997-12-22', False))
    insert_employee(my_connection, ('Valeria Hillton', 2000, 'Football', '1977-10-28', True))
    insert_employee(my_connection, ('Jannet Miler', 2100.9, 'Programming', '1997-02-02', True))
    insert_employee(my_connection, ('William Tokenson', 1500, None, '1999-12-12', False))
    insert_employee(my_connection, ('Shanty Morani', 1200.6, None, '1989-08-13', False))
    insert_employee(my_connection, ('Fiona Giordano', 900.12, 'Football', '1977-01-15', True))
    update_employee(my_connection, (1000, False, 18))
    delete_employee(my_connection, 2)
    select_all_employees(my_connection)
    select_employees_by_salary(my_connection, 2000)
    my_connection.close()