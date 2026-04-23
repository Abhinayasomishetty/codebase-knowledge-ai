from register import register
from login import login
from logout import logout
from utils import format_username

def handle_register(username, password):
    username = format_username(username)
    return register(username, password)

def handle_login(username, password):
    username = format_username(username)
    return login(username, password)

def handle_logout(username):
    username = format_username(username)
    return logout(username)