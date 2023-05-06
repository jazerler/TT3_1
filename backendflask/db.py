from flask_mysqldb import MySQL 
import json
import datetime

class Connector:
    def __init__(self, app):
        self.mysql = MySQL(app)
    
    def jsonData(self, cursor, d):
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        json_data=[]
        for result in d:
                json_data.append(dict(zip(row_headers,result)))
        return json_data
    
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
        json_data = self.jsonData(cursor, d)
        cursor.close()
        return json.dumps(json_data)

    def editClaim(self, ClaimID,ExpenseDate,Amount,Purpose,ChargeToDefaultDept,AlternativeDeptCode,Status, CurrencyID):
        cursor = self.mysql.connection.cursor()
        ExpenseDate = datetime.datetime.strptime(ExpenseDate, "%d/%m/%y %H:%M:%S")
        cursor.execute("UPDATE projectexpenseclaims \
            SET ExpenseDate = %s,Amount = %s,Purpose = %s,ChargeToDefaultDept = %s,AlternativeDeptCode = %s,Status = %s, LastEditedClaimDate = CURDATE(), CurrencyID = %s\
                WHERE  ClaimID = %s",\
                (ExpenseDate,Amount,Purpose,bool(ChargeToDefaultDept),AlternativeDeptCode,Status, CurrencyID, ClaimID))
        self.mysql.connection.commit()
        cursor.close()
        return ""