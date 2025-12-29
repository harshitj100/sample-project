```python
def register():
    username = input("Enter username: ")
    if username in users:
        print("User already exists")
        return None
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match")
        return None
    users[username] = {"password": password}
    print("Registration successful")
    return username
```