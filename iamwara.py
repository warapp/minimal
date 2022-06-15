import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="testtest",
  password="waraphon552546",
  database="testtest"
)

mycursor = mydb.cursor(dictionary=True)

sql = "INSERT INTO hardware (name ,hw_name ,status ,value) VALUE ( 'B3','pump','off','0.40')"

mycursor.execute(sql)

mydb.commit()

ID = 'mycursor.lastrwid'

print(f"ID : {ID}")

sql = "SELECT * FROM hardware WHERE id = {} ".format(ID)


'mycursor.lastrwid'

data = mycursor.fetchall()
print(data)
for i in data:
  print(i)
