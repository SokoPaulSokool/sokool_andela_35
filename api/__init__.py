from flask import Flask
from api.users_api import api_users

app = Flask(__name__)

app.register_blueprint(api_users)
