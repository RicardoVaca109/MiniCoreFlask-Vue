from flask import Blueprint

shark_bp = Blueprint('shark_bp', __name__)

@shark_bp.route("/shark", methods = ['GET'])
def shark():
    return 'Tiburon '