from data import users


def register():
    username = input("Enter username: ")
    if username in users:
        print("User already exists")
        return None
    password = input("Enter password: ")
    users[username] = {"password": password}
    print("Registration successful")
    return username


def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]["password"] == password:
        print("Login successful")
        return username
    print("Invalid credentials")
    return None
