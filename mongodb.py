from pymongo import MongoClient
def connectDatabse():
    client = MongoClient("mongodb+srv://raymondshell921:6OJbDyNHQBb7od9T@cluster0.ham5env.mongodb.net/")
    db = client.pythonProject
    collection = db.loginSystem
    return collection

def signUpUser(database, loginUser):
    username = loginUser.get_username()
    password = loginUser.get_password()
    date = loginUser.get_signUpDate()
    admin = loginUser.get_admin()
    try:
        database.insert_one({"_id": username, "password": password, "date": date, "admin": admin})
        return True
    except Exception as Error:
        print(Error)
        return False

def logIn(database, loginUser):
    username = loginUser.get_username()
    password = loginUser.get_password()
    result = database.find_one({'_id': username, 'password': password})
    if result == None:
        return False
    else:
        return True
def adminCheck(database, loginUser):
    username = loginUser.get_username()
    result = database.find_one({'_id': username, 'admin': True})
    if result == None:
        return False
    else:
        return True