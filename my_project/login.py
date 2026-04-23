from db import validate_user

def login(username, password):
    if validate_user(username, password):
        return "Login successful"
    else:
        return "Invalid credentials"