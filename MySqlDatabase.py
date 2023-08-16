import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='logindata',
                                         user='root',
                                         password='password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)

def closeDatabase():
    connection.close()
    print("MySQL connection is closed")

def Add_Data(usr, passw):
    mySql_insert_query = """INSERT INTO data (username, password) 
                                VALUES (%s, %s) """
    record = (usr, passw)
    try:
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "SignUp Successful")
        cursor.close()
        return True
    except mysql.connector.Error as error:
        print("Failed to insert record into data table {}".format(error))
        return False

#def check_Data(usr, passw):

#def check_data(usr, passw):
