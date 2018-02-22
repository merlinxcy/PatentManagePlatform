#！-*- coding:utf-8 -*-
from . import db,login_manager #ISSUE:001
from flask_login import UserMixin

# 登陆视图数据model
class UserLoginModel(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.Text)
    account_type = db.Column(db.Integer, default=0)#0为普通用户,1为企业用户


# class PersonInfoModel(db.Model):
#     __tablename__ = 'person_info'
#
#
# class CompanyInfoModel(db.Model):
#     __tablename__ = 'company_info'
#
#
# class AdminLoginModel(db.Model):
#     __tablename__ = 'admins'


class PersonRegisterModel(db.Model):
    __tablename__ = 'person_register'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    phone = db.Column(db.String(13))
    location = db.Column(db.String(10))
    card_type = db.Column(db.String(5))
    card_num = db.Column(db.String(20))
    address = db.Column(db.String(150))
    mail_address = db.Column(db.String(50))
    register_status = db.Column(db.Integer, default=0)


# class CompanyRegisterModel(db.Model):
#     __tablename__ = 'company_register'
#
#
# # 用户视图数据model
# class PatentApplyModel(db.Model):
#     pass

@login_manager.user_loader
def load_user(user_id):
    return UserLoginModel.query.get(int(user_id))