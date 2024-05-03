class User:
    def __init__(self, id, name, email, username, password):
        self.id = id
        self.name = name 
        self.email = email
        self.password = password
        self.username = username

    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User(name: {self.name}, email: {self.email}, username: {self.username}, password: {self.password})"