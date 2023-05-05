from flask import Flask, request, jsonify
from db import Connector
from flask_mysqldb import MySQLdb
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_pyfile("dbconfig.py")
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

connector = Connector(app)

@app.route('/retrieve', methods=['POST'])
def retrieve_userbyID():
    try:
        EmployeeID = request.form['EmployeeID']
        d = connector.retrieve(EmployeeID)
        return d, 200
    
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        return str(e), 502
    
    except Exception as e:
        return str(e), 500
    
@app.route('/login', methods=['POST'])
def retrieve_user():
    try:
        EmployeeID = request.form['EmployeeID']
        Password = request.form['Password']
        result = connector.login(EmployeeID, Password)
        if result: 
            access_token = create_access_token(identity=EmployeeID)
            return jsonify(access_token=access_token), 200 
        else:
            return "", 401
    
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        return str(e), 502
    
    except Exception as e:
        return str(e), 500

# create retrieve claim
@app.route('/retrieveClaim', methods=['POST'])
@jwt_required()
def retrieveClaim():
    try:
        current_user = get_jwt_identity()
        EmployeeID = request.form['EmployeeID']
        if current_user != EmployeeID:
            return "", 401
        else:
            result = connector.retrieveClaim(EmployeeID)
        if result:
            return result
        else:
            return "", 404
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        return str(e), 502
    
    except Exception as e:
        return str(e), 500
    
@app.route('/addClaim', methods=['POST'])
@jwt_required()
def addClaim():
    try:
        current_user = get_jwt_identity()
        claimID = request.form['claimID']
        projectid = request.form['projectid']
        EmployeeID = request.form['EmployeeID']
        currencyid = request.form['currencyid']
        expensedate = request.form['expensedate']
        amount = request.form['amount']
        purpose = request.form['purpose']
        chargetodefaultdept = request.form['chargetodefaultdept']
        alternativedeptcode = request.form['alternativedeptcode']
        status = request.form['status']
        lasteditedclaimdate = request.form['lasteditedclaimdate']
        if current_user != EmployeeID:
            return "", 401
        else:
            result = connector.addClaim(claimID,projectid,EmployeeID,currencyid,expensedate,amount,purpose,chargetodefaultdept,alternativedeptcode,status,lasteditedclaimdate)
        if result:
            return result
        else:
            return "", 404

    except (MySQLdb.Error, MySQLdb.Warning) as e:
        return str(e), 502
    
    except Exception as e:
        return str(e), 500


@app.route('/editClaim', methods=['POST'])
@jwt_required()
def editClaim():
    try:
        current_user = get_jwt_identity()
        EmployeeID = request.form['EmployeeID']
        ClaimID = request.form['ClaimID']
        ExpenseDate = request.form['ExpenseDate']
        Amount = request.form['Amount']
        Purpose = request.form['Purpose']
        ChargeToDefaultDept = request.form['ChargeToDefaultDept']
        AlternativeDeptCode = request.form['AlternativeDeptCode']
        Status = request.form['Status']
        CurrencyID = request.form['CurrencyID']
        if current_user != EmployeeID:
            return "", 401
        else:
            result = connector.editClaim(ClaimID, EmployeeID, ExpenseDate,Amount,Purpose,ChargeToDefaultDept,AlternativeDeptCode,Status, CurrencyID)

        print(result)
        if result:
            return "", 200
        else:
            return "", 404
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        return str(e), 502
    
    except Exception as e:
        return str(e), 500


    
if __name__ == "__main__":
    app.run(debug=True)
