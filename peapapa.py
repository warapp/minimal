import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testtest",
  password="waraphon552546",
  database="testtest"
)

mycursor = mydb.cursor(dictionary=True)

sql = "DELETE FROM hardware WHERE id = 44"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"record delete.")