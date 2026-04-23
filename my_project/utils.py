def is_valid_password(password):
    if len(password) < 6:
        return False
    return True

def format_username(username):
    return username.strip().lower()