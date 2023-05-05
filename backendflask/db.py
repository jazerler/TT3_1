from flask_mysqldb import MySQL 
import json

class Connector:
    def __init__(self, app):
        self.mysql = MySQL(app)
    
    def retrieve(self, EmployeeID):
        cursor = self.mysql.connection.cursor()
        cursor.execute(" SELECT * FROM employee WHERE EmployeeID = %s ",(EmployeeID,))
        d = cursor.fetchall()
        # json_data = self.jsonData(cursor, d)
        cursor.close()
        return json.dumps(d)
    
    def login(self, EmployeeID, Password):
        cursor = self.mysql.connection.cursor()
        cursor.execute(" SELECT * FROM employee WHERE EmployeeID = %s AND Password = %s",(EmployeeID,Password))
        d = cursor.fetchall()
        if not d: 
            return None
        cursor.close()
        return json.dumps(d)
    
    def retrieveClaim(self, EmployeeID):
        cursor = self.mysql.connection.cursor()
        cursor.execute(" SELECT claimID, ProjectId, status, currencyID FROM projectexpenseclaims WHERE EmployeeID= %s",(EmployeeID,))
        d = cursor.fetchall()
        if not d: 
            return None
        cursor.close()
        return json.dumps(d)