import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="testtest",
    password="waraphon552546",
    database="testtest"
)

mycursor = mydb.cursor(dictionary=True)
sql = "SELECT * FROM hardware WHERE id = (SELECT MIN(id) FROM hardware)"
mycursor.execute(sql) 
data = mycursor.fetchall()
mycursor.close()
mydb.close()
print(data)
    


    