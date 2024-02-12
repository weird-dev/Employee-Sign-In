from flask import Flask, render_template, request, redirect
from database import create_table, add_employee, get_employees, delete_employee, get_employee_by_identification_no, update_employee

app = Flask(__name__)

# I created a function for the code to create a table in the database if it doesn't exist
create_table()

# Route for the homepage
@app.route('/')
def index():
    employees = get_employees()
    return render_template('index.html', employees=employees)

#route to adding a new employee to the database
@app.route('/add_employee', methods=['POST'])
def add():
    name = request.form['name']
    identification_no = request.form['identification_no']
    time = request.form['time']
    add_employee(name, identification_no, time)
    return redirect('/')

@app.route('/delete_employee/<int:employee_identification_no>')
def delete(employee_identification_no):
    delete_employee(employee_identification_no)
    # Redirect to the homepage after deleting the employee
    return redirect('/')

#code to update the database
@app.route('/edit_employee/<int:employee_identification_no>', methods=['GET', 'POST'])
def edit(employee_identification_no):
    if request.method == 'GET':
        employee = get_employee_by_identification_no(employee_identification_no)
        return render_template('edit_employee.html', employee=employee)
    elif request.method == 'POST':
        name = request.form['name']
        identification_no = request.form['identification_no']
        time = request.form['time']
        update_employee(employee_identification_no, name, identification_no, time)
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)

