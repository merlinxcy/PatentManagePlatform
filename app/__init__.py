#! -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# 初始化配置
app.secret_key = 'HDCFYUYUFfyudtydffyfyufuguuguigufg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:test@127.0.0.1/test'


# 初始化登陆组件
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# 初始化数据库ORM
db = SQLAlchemy(app)# utf-8解决中文乱码
# db.init_app(app)

# 初始化蓝图 ISSUE:001
from auth import auth as auth_blueprint
from main import main as main_blueprint
from admin import admin as admin_blueprint
app.register_blueprint(auth_blueprint,static_folder='static', template_folder='templates')
app.register_blueprint(main_blueprint,static_folder='static', template_folder='templates')
app.register_blueprint(admin_blueprint,static_folder='static', template_folder='templates')