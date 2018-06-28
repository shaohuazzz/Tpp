from flask import Blueprint, jsonify

from app.home.models import Area
# from app.utils.json_utils import to_list

home = Blueprint('home', __name__)

@home.route('/1/')
def home111():
    Area.query.all()
    return '111'
