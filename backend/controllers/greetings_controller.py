from flask import Blueprint

greetings_bp = Blueprint('greetings_bp', __name__)

@greetings_bp.route('/', methods = ['GET'])
def greetings():
    return 'Hello World!'