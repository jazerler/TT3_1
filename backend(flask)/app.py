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

# create transactions route, createclaim
@app.route('/transactions/createclaim', methods=['GET', 'POST'])
def transactions():
    try:
        projectid = request.form['projectid']
        employeeid = request.form['employeeid']
        currencyid = request.form['currencyid']
        expensedate = request.form['expensedate']
        amount = request.form['amount']
        purpose = request.form['purpose']
        chargetodefaultdept = request.form['chargetodefaultdept']
        alternativedeptcode = request.form['alternativedeptcode']
        status = request.form['status']
        lasteditedclaimdate = request.form['lasteditedclaimdate']

    except ValueError:
        pass
    
    # create a new claim
    mycursor.execute("INSERT INTO projectexpenseclaims (projectid, employeeid, currencyid, expensedate, amount, purpose, chargetodefaultdept, alternativedeptcode, status, lasteditedclaimdate) VALUES ('" + projectid, employeeid, currencyid, expensedate, amount, purpose, chargetodefaultdept, alternativedeptcode, status, lasteditedclaimdate + "')")

    return


# create transactions route, createclaim
@app.route('/transactions/deleteclaim', methods=['GET', 'POST'])
def transactions():
    try:
        claimID = request.form['claimid']

    except ValueError:
        pass
    
    # delete claim
    mycursor.execute("DELETE FROM projectexpenseclaims WHERE claimID = '" + claimID + "')")
    
    return

# Main method
if __name__ == '__main__':
    app.run(debug=True)