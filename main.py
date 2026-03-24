from application import Client
def sign_up():
    username = input("Username: ") #allows client to enter username
    password = input("Password: ") #allows client to enter password
    email = input("Enter your email address: ") #allows client to enter email

    user = Client(username, password, email) 
    store_client(username, password, email) #saves the clients details into a text file
    print("Your account has now been created! ")
    print(user)
def store_client(username, password, email):
    with open("clients.txt", "a") as file: 
        file.write(f"{username}, {password}, {email}\n")
if __name__ == "__main__":
    sign_up()



