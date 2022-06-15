import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testtest",
  password="waraphon552546",
  database="testtest"
)

mycursor = mydb.cursor(dictionary=True)

#sql = "SELECT name,hw_name,status,value,id FROM hardware"
sql = "SELECT * FROM hardware"

mycursor.execute(sql)

data = mycursor.fetchall()
print(data)
for i in data:
  print(i)

print(data[2]['name'])



