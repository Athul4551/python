import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="athul",
    password="Athul@123",
    database="Mydb1"
)
print("connectod sucessfully!")
connection.close()