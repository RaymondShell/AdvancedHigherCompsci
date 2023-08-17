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
        cursor = connection.cursor(buffered=True)
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)

def closeDatabase():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")

def Add_Data(usr, passw):
    passwordLength = len(passw)
    mySql_insert_query = """INSERT INTO data (username, password, pwordlength) 
                                VALUES (%s, %s, %s) """
    record = (usr, passw, passwordLength)
    try:
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "SignUp Successful")
        return True
    except mysql.connector.Error as error:
        print("Failed to insert record into data table {}".format(error))
        if error.errno == 1062:
            return "EXISTS"
        print("Failed to insert record into data table {}".format(error))
        return False

def check_Data(usr, passw):

    print(usr, passw)
    try:
        cursor.execute("SELECT username, password FROM data WHERE username='%s' AND password='%s'"% (usr, passw))
        connection.commit()
        print(cursor.rowcount, "Login Confirmed")
        return True
    except mysql.connector.Error as error:
        print("Username And Password Combo Not Found {}".format(error))
        return False

#def check_data(usr, passw):
