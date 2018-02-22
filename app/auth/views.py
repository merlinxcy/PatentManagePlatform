#! -*-coding:utf-8 -*-
import hashlib
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user

from . import auth
from ..models import UserLoginModel,PersonRegisterModel,db
from forms import UserLoginForm,RegisterCompanyForm,RegisterPersonForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # 在测试的过程中发现如果不加csrf token验证一直为false
            username = form.username.data
            password = form.password.data
            md5 = hashlib.md5()
            md5.update(password)
            password = md5.hexdigest()
            user = UserLoginModel.query.filter_by(username=username).first()
            if user:
                db_password = user.password
                if db_password and db_password == password:
                    flash('登录成功')
                    login_user(user)
                    return redirect(url_for('main.main_handler'))
                else:
                    flash('登录凭证有错误')
                    return redirect(url_for('auth.login'))
            else:
                flash('登录凭证有错误')
                return redirect(url_for('auth.login'))
    else:
        return render_template('login/login.html', form=form)


@auth.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash('你已经登出')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET'])
def register():
    return render_template('login/register.html')


@auth.route('/register_person',methods=['GET','POST'])
def register_person():
    form = RegisterPersonForm()
    if request.method == 'POST':
        # print(form.validate_on_submit())
        # for i in form:
        #     print i
        if form.validate_on_submit():
            # print PersonRegisterModel.query.filter_by(mail_address=form.email.data).first()
            # print UserLoginModel.query.filter_by(username=form.email.data)
            UserLoginModel.query.filter_by(username=form.email.data)
            if PersonRegisterModel.query.filter_by(mail_address=form.email.data).first() or\
            UserLoginModel.query.filter_by(username=form.email.data).first():
                flash('用户已经存在')
                return redirect(url_for('auth.register_person'))
            # return form.email.data
            length = len(PersonRegisterModel.query.all())
            id = length+1
            # orm for register
            name = form.name.data
            phone = form.phone.data
            location = form.location.data
            card_type = form.card_type.data
            card_num = form.card_num.data
            address = form.address.data
            mail_address = form.email.data
            obj = PersonRegisterModel(id=int(id),name=name,phone=phone,
                                     location=location,card_type=card_type,
                                     card_num=card_num,address=address,mail_address=mail_address,
                                     register_status=0)
            db.session.add(obj)
            db.session.commit()
            # orm for login
            length = len(UserLoginModel.query.all())
            id = length
            username = mail_address
            password = form.password.data
            md5 = hashlib.md5()
            md5.update(password)
            password = md5.hexdigest()
            obj = UserLoginModel(username=username,password=password)
            db.session.add(obj)
            db.session.commit()
            flash('个人用户注册成功')
            return redirect(url_for('auth.login'))
        return 'post'
    else:
        return render_template('login/register_person.html', form=form)


@auth.route('/register_company', methods=['GET','POST'])
def register_company():
    form = RegisterCompanyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return form.email.data
        return 'post'
    else:
        return render_template('login/register_company.html',form=form)



