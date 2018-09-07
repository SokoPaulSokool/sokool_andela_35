from flask import Blueprint, request, jsonify, json
from api.models.users_model import UserList, User

api_users = Blueprint('users', __name__)

all_users = UserList()


class MessageResponse:
    @staticmethod
    def send(message, code):
        return jsonify({"message": message}), code


@api_users.route('/api/add-user', methods=['POST'])
def add_user():
    """adds user to users list"""
    if request.method == 'POST':
        data = request.get_json()
        if not data.get('name'):
            return MessageResponse.send("either name is not set or empty", 406)
        if not data.get('email'):
            return MessageResponse.send("either email is not set or empty", 406)
        if not data.get('password'):
            return MessageResponse.send("either password is not set or empty", 406)

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        newuser = User(name, email, password)
        all_users.add_user(newuser)
        message = "User with name " + newuser.username+" has been created"
        return MessageResponse.send(message, 201)


@api_users.route('/api/get-users', methods=['GET'])
def get_user():
    """gets all users"""
    if request.method == 'GET':
        return MessageResponse.send(all_users.get_all_users(), 200)


@api_users.route('/api/add-user', methods=['DELETE'])
def delete_user():
    """deletes user from users list"""
    if request.method == 'DELETE':
        return "DELETE", 201
