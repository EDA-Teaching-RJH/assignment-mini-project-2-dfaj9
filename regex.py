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