from app.ext import ma
from app.home.models import Movies


class MovieSchema(ma.ModelSchema):
    class Meta:
        model = Movies


# 单个对象转化成字典
movie_schema = MovieSchema()
# 多个对象进行转化列表
movies_schema = MovieSchema(many=True)