import json

from flask import Blueprint ,request ,jsonify ,render_template
import redis
from flask_mail import  Message
from app.ext import db, mail, cache
from app.user.models import User
from app.home.models import Area
HOST = '127.0.0.1'
PORT = 6379
DB = 0
pool = redis.ConnectionPool(host=HOST,port=PORT,db=DB,decode_responses=True)
rds = redis.Redis(connection_pool=pool)


user = Blueprint('user',__name__ )

@user.route('/login/')
def login():
    User.query.all()
    return render_template('reigster.html')

@user.route('/register/',methods=['GET','POST'])
def register():
    result = {}
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        email = request.values.get('email')
        if username and password and email :
            user = User.query.filter(User.username == username or User.email == email).all()
            if user:
                result.update(msg='账户或者邮箱已经存在',status=-2)
            else:
                user = User(username=username,password=password,email=email)
                db.session.add(user)
                db.session.commit()
            msg = Message('Hello',
                          body='用户您好',
                          html=render_template('activate.html',username=username),
                          sender='18971367155@163.com',
                          recipients=['18971367155@163.com'])
            # cache.set(username=username)
            mail.send(msg)
            rds.set('username',username,ex=10*60)
        else:
            result.update(msg='必要参数不能为空',status=-1)
    else:
        result.update(msg='错误的请求方式',status=400)
    return jsonify(result)

@user.route('/activate/')
def activate_account():
    result = {}
    username = request.values.get('username')
    if username == rds.get('username'):
        user = User.query.filter(User.username == username).first()
        if user:
            user.is_active = True
            db.session.add(user)
            db.session.commit()
            result.update(statys=200,msg='激活成功')
        else:
            result.update(status=-4,msg='激活用户不存在')
    else:
        result.update(status=-3,msg='激活链接失效，亲重新激活')
    return jsonify(result)


@user.route('/1/',methods=['POST','GET'])
def test_send():
    msg = Message('激活邮件',
                 body = '11111',
                 sender = '18971367155@163.com',
                 recipients = ['18971367155@163.com'])
    mail.send(msg)
    return '请激活'

keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
@user.route('/add/')
def add_json_data():
    with open(r'E:\Flaskproject\Tpp\app\json\area.json','r',encoding='utf-8') as f:
        data = json.load(f)

        obj = data.get('returnValue')

        for key in keys:
            cities = obj.get(key)
            for city in cities:
                db.session.add(Area(name=city.get('regionName'),
                                    pingyin=city.get('pinYin'),
                                    parent_id=city.get('parentId'),
                                    area_id=city.get('cityCode'),
                                    key=key,
                                    ))
                db.session.commit()
    return 'success'