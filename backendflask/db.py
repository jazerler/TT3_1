from flask_mysqldb import MySQL 
import json
import datetime

class Connector:
    def __init__(self, app):
        self.mysql = MySQL(app)
    
    #Convert to json format
    def jsonData(self, cursor, d):
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        json_data=[]
        for result in d:
                json_data.append(dict(zip(row_headers,result)))
        return json_data
    
    # def retrieve(self, EmployeeID):
    #     cursor = self.mysql.connection.cursor()
    #     cursor.execute(" SELECT * FROM employee WHERE EmployeeID = %s ",(EmployeeID,))
    #     d = cursor.fetchall()
    #     # json_data = self.jsonData(cursor, d)
    #     cursor.close()
    #     return json.dumps(d)
    
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
    
    def addClaim(self, claimID,projectid,EmployeeID,currencyid,expensedate,amount,purpose,chargetodefaultdept,alternativedeptcode,status,lasteditedclaimdate):
        cursor = self.mysql.connection.cursor()
        expensedate = datetime.datetime.strptime(expensedate, "%d/%m/%y %H:%M:%S")
        chargetodefaultdept = bool(chargetodefaultdept)
        cursor.execute('''INSERT INTO projectexpenseclaims VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ''',(claimID,projectid,EmployeeID,currencyid,expensedate,amount,purpose,chargetodefaultdept,alternativedeptcode,status,lasteditedclaimdate))
        self.mysql.connection.commit()
        cursor.close()
        

    def editClaim(self, ClaimID, EmployeeID, ExpenseDate,Amount,Purpose,ChargeToDefaultDept,AlternativeDeptCode,Status, CurrencyID):
        cursor = self.mysql.connection.cursor()
        ExpenseDate = datetime.datetime.strptime(ExpenseDate, "%d/%m/%y %H:%M:%S")
        cursor.execute("UPDATE projectexpenseclaims \
            SET ExpenseDate = %s,Amount = %s,Purpose = %s,ChargeToDefaultDept = %s,AlternativeDeptCode = %s,Status = %s, LastEditedClaimDate = CURDATE(), CurrencyID = %s\
                WHERE  ClaimID = %s AND EmployeeID = %s",\
                (ExpenseDate,Amount,Purpose,bool(ChargeToDefaultDept),AlternativeDeptCode,Status, CurrencyID, ClaimID, EmployeeID))
        self.mysql.connection.commit()
        cursor.close()
        return "edited"
    
    def deleteClaim(self, claimID, EmployeeID):
        cursor = self.mysql.connection.cursor()
        cursor.execute("DELETE FROM projectexpenseclaims WHERE claimID = %s AND employeeID = %s",(claimID,EmployeeID))
        self.mysql.connection.commit()
        cursor.close()
        return "deleted"
    
