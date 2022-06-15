import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testtest",
  password="waraphon552546",
  database="testtest"
)

mycursor = mydb.cursor(dictionary=True)

sql = "UPDATE hardware SET ID ='10' WHERE id = '5'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"record updated.")