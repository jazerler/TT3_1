from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_mysqldb import MySQL
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="**",
    database="expenseclaimsdata"
    )


mycursor = db.cursor()
# db.commit()
# db.close()

# print('Successful connection!')

app = Flask(__name__)

# create login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        username = request.form['Uname']
        password = request.form['Pass']
    except ValueError:
        pass
    
    # Check if account exists in database
    # Extract record from database
    mycursor.execute(
        "SELECT * FROM employee WHERE (employee.EmployeeID = '" + username + "' AND employee.Password='" + password + "')")
    myresult = mycursor.fetchall()

    for x in myresult:
        loginID = x[0]
        username = x[1]
    return "Hello World"


# create dashboard route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    try:
        username = request.form['Uname']
    except ValueError:
        pass
    
    mycursor.execute(
        "SELECT claimid, projectid, status, currencyid FROM projectexpenseclaims WHERE employeeId ='" + username + "'")
    myresult = mycursor.fetchall()

    for x in myresult:
        claimid = x[0]
        projectid = x[1]      
        status = x[2]
        currencyid = x[3]

    return claimid, projectid, status, currencyid


# Main method
if __name__ == '__main__':
    app.run(debug=True)