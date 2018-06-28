from flask import Blueprint, jsonify
from sqlalchemy import func
from sqlalchemy.util import to_list

from app.home.models import Area , Movies ,Cinemas
# from app.utils.json_utils import to_list

home = Blueprint('home', __name__)

@home.route('/1/')
def home111():
    Area.query.all()
    return '111'

@home.route('/moves/',methods=['POST'])
def movies():
    result = {}
    try:
        movie = {}
        counts = Movies.query.with_entities(Movies.flag,func.count('*')).group_by(Movies.flag).all()
        hot_movies = Movies.query.filter(Movies.flag == 1).limit(5).all()
        show_movies = Movies.query.filter(Movies.flag == 2).limit(5).all()
        movie.update(counts=counts,hot_movies=to_list(hot_movies),show_movies=to_list(show_movies))
        result.update(atatus=200,msg='success',data=movie)
    except:
        result.update(atatus=404,msg='fail')

    return '111'