username = "admin"
password = "password"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if username == input_username and password == input_password:
    print("Login succesfull")
else:
    print("Invalid credentials")