from flask_mysqldb import MySQL 
import json

class Connector:
    def __init__(self, app):
        self.mysql = MySQL(app)
    
    def retrieve(self, EmployeeID):
        cursor = self.mysql.connection.cursor()
        cursor.execute(" SELECT * FROM employee WHERE EmployeeID = %s ",(EmployeeID,))
        d = cursor.fetchall()
        json_data = self.jsonData(cursor, d)
        cursor.close()
        return json.dumps(json_data)