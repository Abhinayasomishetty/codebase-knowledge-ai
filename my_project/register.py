from db import add_user, user_exists

def register(username, password):
    if user_exists(username):
        return "User already exists"

    if len(password) < 6:
        return "Weak password"

    if add_user(username, password):
        return f"{username} registered successfully"
    else:
        return "Registration failed"