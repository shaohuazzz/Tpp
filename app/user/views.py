from flask import Blueprint ,request ,jsonify ,render_template
from flask_mail import  Message
from app.ext import db, mail, cache
from app.user.models import User

user = Blueprint('user',__name__)

@user.route('/login/')
def login():
    User.query.all()
    return '111'

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
            cache.set(username=username)
            mail.send(msg)
        else:
            result.update(msg='必要参数不能为空',status=-1)
    else:
        result.update(msg='错误的请求方式',status=400)
    return jsonify(result)

@user.route('/1/',methods=['POST','GET'])
def test_send():
    msg = Message('激活邮件',
                 body = '11111',
                 sender = '18971367155@163.com',
                 recipients = ['18971367155@163.com'])
    mail.send(msg)
    return '请激活'