from application import Client
def sign_up():
    username = input("Username: ") #allows client to enter username
    password = input("Password: ") #allows client to enter password
    email = input("Enter your email address: ") #allows client to enter email

    user = Client(username, password, email)
    print("Your account has now been created! ")
    print(user)
if __name__ == "__main__":
    sign_up()
