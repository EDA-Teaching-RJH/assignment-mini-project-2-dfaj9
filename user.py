from application import User
class Student(User):
    def__init__(self, name, email, degree, ids):
        super().__init__(name)
        self.email = email
        self.degree = degree
        self.ids = ids

    def__str__(self):
        return f"{self.name} name,{self.email} email,{self.degree} degree,{self.ids} ids"
