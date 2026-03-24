class User:  #allows the user to be given a name
    def __init__(self, username, password, email):
        if not username: #These statements checks to see if information are missing
            raise ValueError("A username is needed!") 
        if not password:
            raise ValueError("A password is needed!")
        if not email:
            raise ValueError("An Email is needed!")
        
        self.username = username #saves the users username
        self.password = password #saves the users password
        self.email = email #saves the users email address

    def __str__(self):
        return f"{self.username} username,{self.email} email"  #Displays the username and email of a user

class Client(User): #client class inherits user class traits
    def __init__(self, username, password, email):
        super().__init__(username, password, email)

    def display_client(self, clients):
        for client in clients: #This will loop through all clients then display them
            print(client)



import re
def valid_email(email):
        if re.search(r"^\w+@\w.+\.ac.uk$", email): #regex for common emails and uni emails
            print("This email address is valid!")
        else:
            print("This email address is invalid! ")

def strong_password(password):
    if re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$", password):  #this does a lowercase, uppercase, special charachter, length and number check
        print("This Password is strong!") #if user password has all, it is strong
    else:
        print("This Password is weak!")

    




       
