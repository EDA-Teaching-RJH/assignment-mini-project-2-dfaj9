from regex2 import valid_email, strong_password

def test_email():
    assert valid_email("Human@kent.ac.uk") == True #this will check if the condition is true, pass expected
    assert valid_email("baller129@canterbury.ac.uk") == True #expected pass

def test2_email():
    assert valid_email("Human@gmail.co.uk") == False #this is an expected fail, as only .ac is used
    assert valid_email("baller129") == False #expected fail, as no @ or domain



def test_password():
    assert strong_password("Wegoharder99@vro") == True #expected pass, meets all password requirements
    assert strong_password("bAlly1@Grave99") == True #expected pass 

def test2_password():
    assert strong_password("baller") == False #expected fail, length of characters not enough
    assert strong_password("123456789123") == False #expected fail, only numbers 
    assert strong_password("ballerfoottygame99") == False #expected fail, no uppercase or special character
    assert strong_password("Passwordisstrong@") == False #expected fail, no numbers
    
