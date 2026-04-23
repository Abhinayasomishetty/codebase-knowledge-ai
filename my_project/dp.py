# simple in-memory database

users_db = {}

def add_user(username, password):
    if username in users_db:
        return False
    users_db[username] = password
    return True

def validate_user(username, password):
    if username in users_db and users_db[username] == password:
        return True
    return False

def user_exists(username):
    return username in users_db