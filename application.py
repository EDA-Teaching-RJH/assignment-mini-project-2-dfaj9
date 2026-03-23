class User:  #allows the user to be given a name
    def __init__(self, name):
        if not name:
            raise ValueError("No name has been entered! ")
        self.name = name
        
