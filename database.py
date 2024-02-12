import sqlite3

# Function to create a table in the database if it doesn't exist
def create_table():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY, name TEXT, identification_no INTEGER, time TIME)''')
    conn.commit()
    conn.close()

# Function to add a new employee to the database
def add_employee(name, identification_no, time):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''INSERT INTO employees (name, identification_no, time)
                 VALUES (?, ?, ?)''', (name, identification_no, time))
    conn.commit()
    conn.close()


# Function to fetch all employees from the database
def get_employees():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    employees = c.fetchall()
    conn.close()
    return employees

def delete_employee(employee_identification_no):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("DELETE FROM employees WHERE identification_no=?", (employee_identification_no,))
    conn.commit()
    conn.close()

def get_employee_by_identification_no(employee_identification_no):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("SELECT * FROM employees WHERE identification_no=?", (employee_identification_no,))
    employee = c.fetchone()
    conn.close()
    return employee

def update_employee(employee_identification_no, name, identification_no, time):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("UPDATE employees SET name=?, identification_no=?, time=? WHERE identification_no=?", (name, identification_no, time, employee_identification_no))
    conn.commit()
    conn.close()