from flask import Blueprint, jsonify
from sqlalchemy import func
from app.utils.json_utils import to_list

from app.home.models import Area , Movies ,Cinemas


home = Blueprint('home', __name__)

@home.route('/1/')
def home111():
    Area.query.all()
    return '111'

keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

@home.route('/areas/')
def get_ares():
    result = {}
    ares = {}
    try:
        for key in keys:
            area_list =Area.query.filter(Area.key == key).all()
            if area_list:
                ares[key] = to_list(area_list)
        result.update(msg='success',status=200,ares=ares)
    except Exception as e:
        result.update(msg="查询失败",status=404)
    return jsonify(result )




@home.route('/moves/')
def movies():
    result = {}
    try:
        movie = {}
        counts = Movies.query.with_entities(Movies.flag,func.count('*')).group_by(Movies.flag).all()
        hot_movies = Movies.query.filter(Movies.flag == 1).limit(5).all()
        show_movies = Movies.query.filter(Movies.flag == 2).limit(5).all()
        movie.update(counts=counts,hot_movies=to_list(hot_movies),show_movies=to_list(show_movies))
        result.update(status=200,msg='success',data=movie)
    except Exception as e:
        result.update(status=404,msg='fail')
    return jsonify(result)