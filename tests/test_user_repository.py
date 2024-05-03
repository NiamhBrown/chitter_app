from lib.user_repository import UserRepository
from lib.user import User

def test_return_all_users(db_connection):
    db_connection.seed("seeds/chitter_tables.sql") 
    repository = UserRepository(db_connection)
    users = repository.all()
    assert str(users) == "[User(name: Niamh, email: niamh@me.com, username: niamhb, password: niamh123!), User(name: Grace, email: grace@me.com, username: gracee, password: grace123!)]"

def test_create_user(db_connection):
    db_connection.seed("seeds/chitter_tables.sql") 
    repository = UserRepository(db_connection)
    repository.create(User(None,'Angelo', 'angelo@me.com', 'angeloc', 'angelo123!'))
    result = repository.all()
    assert str(result) == "[User(name: Niamh, email: niamh@me.com, username: niamhb, password: niamh123!), User(name: Grace, email: grace@me.com, username: gracee, password: grace123!), User(name: Angelo, email: angelo@me.com, username: angeloc, password: angelo123!)]"

def test_delete(db_connection):
    db_connection.seed("seeds/chitter_tables.sql") 
    repository = UserRepository(db_connection)
    repository.delete(1)
    result = repository.all()
    assert str(result) == "[User(name: Grace, email: grace@me.com, username: gracee, password: grace123!)]"
