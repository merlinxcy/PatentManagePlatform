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


class PersonInfoModel(db.Model):
    __tablename__ = 'person_info'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10))
    phone = db.Column(db.String(13))
    location = db.Column(db.String(10))
    card_type = db.Column(db.String(5))
    card_num = db.Column(db.String(20))
    address = db.Column(db.String(150))
    mail_address = db.Column(db.String(50))

class CompanyInfoModel(db.Model):
    __tablename__ = 'company_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    card_type = db.Column(db.String(5))
    card_num = db.Column(db.String(20))
    company_location = db.Column(db.String(10))
    location_code = db.Column(db.String(10))
    address = db.Column(db.String(150))
    mail_address = db.Column(db.String(50))
    per_phone = db.Column(db.String(13))
    per_name = db.Column(db.String(10))

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


class CompanyRegisterModel(db.Model):
    __tablename__ = 'company_register'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    card_type = db.Column(db.String(5))
    card_num = db.Column(db.String(20))
    company_location = db.Column(db.String(10))
    location_code = db.Column(db.String(10))
    address = db.Column(db.String(150))
    mail_address = db.Column(db.String(50))
    per_phone = db.Column(db.String(13))
    per_name = db.Column(db.String(10))
    register_status = db.Column(db.Integer, default=0)


# 用户视图数据model
class PatentApplyModel(db.Model):
    __tablename__ = 'patent_apply_record'
    id = db.Column(db.Integer, primary_key=True)
    account_username = db.Column(db.String(50))
    account_type = db.Column(db.String(10))
    name = db.Column(db.String(20))
    type = db.Column(db.String(20))
    main_per_name = db.Column(db.String(20))
    first_per_name = db.Column(db.String(20))
    first_per_phone = db.Column(db.String(15))
    first_per_card_num = db.Column(db.String(50))
    first_per_address = db.Column(db.String(100))
    date = db.Column(db.String(20))
    priority = db.Column(db.Integer,default=0)
    description = db.Column(db.String(200))
    check_status = db.Column(db.String(20))


class PeixunApplyModel(db.Model):
    __tablename__ = 'peixun_apply_record'
    id = db.Column(db.Integer,primary_key=True)
    account_username = db.Column(db.String(50))
    account_type = db.Column(db.String(10))
    username = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    card_num = db.Column(db.String(35))
    address = db.Column(db.String(50))
    date = db.Column(db.String(30))
    reason = db.Column(db.String(200))
    content = db.Column(db.String(200))
    check_status = db.Column(db.String(10), default='checking')


class FeeApplyModel(db.Model):
    __tablename__ = 'fee_apply_record'
    id = db.Column(db.Integer, primary_key=True)
    account_username = db.Column(db.String(50))
    account_type = db.Column(db.String(10))
    patent_id = db.Column(db.String(20))
    name = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    date = db.Column(db.String(20))
    description = db.Column(db.String(200))
    check_status = db.Column(db.String(20),default='checking')


class TradeApplyModel(db.Model):
    __tablename__ = 'trade_apply_record'
    id = db.Column(db.Integer, primary_key=True)
    patent_id = db.Column(db.Integer)
    apply_per_name = db.Column(db.String(30))
    apply_per_phone = db.Column(db.String(30))
    date = db.Column(db.String(30))
    apply_description = db.Column(db.String(300))
    check_status = db.Column(db.String(30),default='checking')


class TradePerchaseModel(db.Model):
    __tablename__ = 'trade_perchase_record'
    id = db.Column(db.Integer, primary_key=True)
    patent_id = db.Column(db.Integer)
    perchase_per_name = db.Column(db.String(30))
    perchase_per_phone = db.Column(db.String(30))
    date = db.Column(db.String(30))
    check_status = db.Column(db.String(30),default='checking')


class TradeMarketModel(db.Model):
    __tablename__ = 'trade_market'
    id = db.Column(db.Integer,primary_key=True)
    apply_date = db.Column(db.String(30))
    patent_id = db.Column(db.Integer)
    patent_name = db.Column(db.String(100))
    main_per_name = db.Column(db.String(50))
    description = db.Column(db.String(300))
    status = db.Column(db.String(30))


#############################################################################

@login_manager.user_loader
def load_user(user_id):
    return UserLoginModel.query.get(int(user_id))