import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
# def return_a_string():
#     return 'string'

@app.route('/', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/users', methods=['GET'])
def get_users():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    return "\n".join([
            str(user) for user in repository.all()
        ])

# == Your Routes End ==

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
