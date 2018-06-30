from flask import Blueprint, request, jsonify
from app.movies.schema import movies_schema
from app.cinema.schema import cinemas_schema
from app.utils.json_utils import to_list
from app.cinema.models import Cinema

cinema_blue = Blueprint('cinema_blue', __name__)

@cinema_blue.route('/list/')
def cinemas():
    result = {}
    try:
        page = request.values.get('page',default=1,type=int)
        size = request.values.get('size',default=10,type=int)
        sort = request.values.get('sort',default=0,type=int)
        dist = request.values.get('dist')
        city = request.values.get('city')
        keyword = request.values.get('keyword')
        if city:
            query = Cinema.query.filter(Cinema.city == city)
            if dist:
                query = query.filter(Cinema.district == dist)
            if keyword:
                query = query.filter(Cinema.name.like('%'+keyword+'%'))
            if sort:
                if sort == 1:
                    query = query.order_by(Cinema.score.desc())
                else:
                    query = query.order_by(Cinema.score)
            paginate = query.paginate(page=page,per_page=size,error_out=False)
            result.update(status=200, msg='success', cinemas=to_list(paginate.items))
        else:
            result.update(status=-1, msg='no param city')

    except Exception as e:
        result.update(status=404,msg='fail')
    return jsonify(result)
