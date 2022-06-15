import mysql.connector

def con():
    mydb = mysql.connector.connect(
    host="localhost",
    user="testtest",
    password="waraphon552546",
    database="testtest"
)
    return mydb

class Users_data:
    def getData():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT name FROM users "
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data


    def get_users_ByID(ID):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users WHERE ID = {}".format (ID)
        mycursor.execute(sql)

    
    def insert_hardware(name, hw_name,status,value ):
       
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)

        sql = "INSERT INTO hardware (name ,hw_name ,status ,value) VALUE ( '{}','{}','{}',{})".format(
            name, hw_name,status,value
        )
        mycursor.execute(sql)
        mydb.commit()

        

    def update_users(id ,username ,password ,name ,lastname ,address ):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE users SET id = '{}', usersname = '{}' ,password = '{}' ,name = '{}' ,lastname = '{}' ,address = '{}'".format(
           id ,username ,password ,name ,lastname ,address 
        )
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid

        

    def delete_users(id):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM users WHERE id = {}".format(
            id
        )
        mycursor.execute(sql)
        mydb.commit()
        return True

    
    

    

