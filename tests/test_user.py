from lib.user import User

def test_user_constructs():
    user = User(1,'Niamh', 'niamh@me.com','niamhb','niamh123!')
    assert user.id == 1
    assert user.name == 'Niamh'
    assert user.email == 'niamh@me.com'
    assert user.password == 'niamh123!'
    assert user.username == 'niamhb'

def test_eq():
    user1 = User(1,'Niamh', 'niamh@me.com','niamhb','niamh123!')
    user2 = User(1,'Niamh', 'niamh@me.com','niamhb','niamh123!')
    assert user1 == user2

def test_user_repr():
    user = User(1,'Niamh', 'niamh@me.com','niamhb','niamh123!')
    assert str(user) == "User(name: Niamh, email: niamh@me.com, username: niamhb, password: niamh123!)"