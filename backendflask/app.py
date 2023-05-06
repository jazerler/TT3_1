from flask import Flask, request, jsonify
from db import Connector
from flask_mysqldb import MySQLdb
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
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

# create dashboard route
@app.route('/retrieveClaim', methods=['POST'])
def retrieveClaim():
    try:
        EmployeeID = request.form['EmployeeID']
        result = connector.retrieveClaim(EmployeeID)
        if result:
            return result
        else:
            return "", 404
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        return str(e), 502
    
    except Exception as e:
        return str(e), 500