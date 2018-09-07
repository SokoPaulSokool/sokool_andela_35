from flask import Blueprint, request, jsonify, json

api_users = Blueprint('users', __name__)


@api_users.route('/api/add-user', methods=['POST'])
def add_user():
    """adds user to users list"""
    if request.method == 'POST':
        return "POST", 201


@api_users.route('/api/get-users', methods=['GET'])
def get_user():
    """gets all users"""

    if request.method == 'GET':
        return "GET", 201


@api_users.route('/api/add-user', methods=['DELETE'])
def delete_user():
    """deletes user from users list"""
    if request.method == 'DELETE':
        return "DELETE", 201
