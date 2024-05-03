from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            user = User(row["id"], row["name"], row["email"], row["username"], row["password"])
            users.append(user)
        return users
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (name, email, username, password) VALUES (%s, %s, %s, %s)', [user.name, user.email, user.username, user.password])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE FROM users WHERE id =%s',[id])
        return None