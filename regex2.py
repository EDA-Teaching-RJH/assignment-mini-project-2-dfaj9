import re
def valid_email(email):
        if re.search(r"^\w+@\w.+\.ac.uk$", email): #regex for common emails and uni emails
          return True
        return False

def strong_password(password):
    if re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$", password):  #this does a lowercase, uppercase, special charachter, length and number check
       return True
    return False