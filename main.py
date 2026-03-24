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
    with open("clients.txt", "a") as file:  #opens file in append 
        file.write(f"{username}, {password}, {email}\n")

   

def login():
    username = input("Username: ") 
    password = input("Password: ")
    file = open("clients.txt", "r") #file will be in read 

    for line in file: #loops through the lines in the file
        saved_username, saved_password, saved_email = line.rstrip().split(", ") #removes new line
        if username == saved_username and password == saved_password: #compares the users input to saved details
            print("Welcome Back!")
            file.close()
            return

    print("Invalid login detailes has been entered. Please try again")

   

def main():
    while True:
        print("\n1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        option = input("What will you like to do? ")

        if option == "1":
            sign_up()
        elif option == "2":
            login()
        elif option == "3":
            print("You have successfully Logged Out!")
            break #stops the program 
        else:
            print("This option does not exist!")


if __name__ == "__main__":

             main()
    





        


