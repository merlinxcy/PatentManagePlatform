#! -*-coding:utf-8 -*-
from flask import render_template, redirect, url_for, request, session,flash
from flask_login import login_user, logout_user, login_required, current_user

from . import main
from .forms import PeixunApplyForm,PatentApplyForm,FeeApplyForm,TradeApplyForm,TradePerchaseForm
from ..models import *


def check_jihuo_status(mail_address):
    com_obj = CompanyRegisterModel.query.filter_by(mail_address=mail_address).first()
    per_obj = PersonRegisterModel.query.filter_by(mail_address=mail_address).first()
    if com_obj:
        if com_obj.register_status == 1:
            return True
        else:
            return False
    if per_obj:
        if per_obj.register_status == 1:
            return True
        else:
            return False
    return False


def check_user_type(mail_address):
    if check_jihuo_status(session['username']):
        com_obj = CompanyInfoModel.query.filter_by(mail_address=mail_address).first()
        per_obj = PersonInfoModel.query.filter_by(mail_address=mail_address).first()
    else:
        com_obj = CompanyRegisterModel.query.filter_by(mail_address=mail_address).first()
        per_obj = PersonRegisterModel.query.filter_by(mail_address=mail_address).first()
    if com_obj:
        return 'company'
    elif per_obj:
        return 'person'
    else:
        return 'person'


@main.route('/main/user_center.html',methods=['GET'])
@login_required
def user_center():
    return render_template('houtai/main.html')


@main.route('/main', methods=['GET'])
@login_required
def main_handler():
    return render_template('houtai/main.html')


@main.route('/main/left.html', methods=['GET'])
@login_required
def left():
    return render_template('houtai/left.html')


@main.route('/main/blank.html', methods=['GET'])
@login_required
def blank():
    return render_template('houtai/blank.html')


@main.route('/main/head.html', methods=['GET'])
@login_required
def head():
    username = session['username']
    return render_template('houtai/head.html', username=username)


@main.route('/main/patent_apply.html', methods=['GET', 'POST'])
@login_required
def patent_apply():
    form = PatentApplyForm()
    if check_jihuo_status(session['username']) == False:
        flash('请等待管理员认证')
        return render_template('houtai/blank.html')
    if request.method == 'POST':
        account_username = session['username']
        account_type = check_jihuo_status(account_username)
        name = form.name.data
        type = form.type.data
        main_per_name = form.main_per_name.data
        first_per_name = form.first_per_name.data
        first_per_phone = form.first_per_phone.data
        first_per_card_num = form.first_per_card_num.data
        first_per_address = form.first_per_address.data
        date = form.date.data
        priority = form.priority.data
        description = form.description.data
        check_status = 'checking'
        obj = PatentApplyModel(account_username=account_username,account_type=account_type,
                               name=name,type=type,main_per_name=main_per_name,
                               first_per_name=first_per_name,first_per_address=first_per_address,
                               first_per_phone=first_per_phone,first_per_card_num=first_per_card_num,
                               date=date,priority=priority,description=description,
                               check_status=check_status)
        db.session.add(obj)
        db.session.commit()
        flash('提交成功')
    return render_template('houtai/patent_apply.html', form=form)


@main.route('/main/patent_record.html', methods=['GET'])
@login_required
def patent_record():
    if check_jihuo_status(session['username']) == False:
        flash('请等待管理员认证')
        return render_template('houtai/blank.html')
    obj = PatentApplyModel.query.filter_by(account_username=session['username']).all()
    return render_template('houtai/patent_record.html', info=obj)


@main.route('/main/peixun_record.html', methods=['GET'])
@login_required
def peixun_record():
    if check_jihuo_status(session['username']) == False:
        flash('请等待管理员认证')
        return render_template('houtai/blank.html')
    obj = PeixunApplyModel.query.filter_by(account_username=session['username']).all()
    return render_template('houtai/peixun_record.html', info=obj)


@main.route('/main/peixun_apply.html', methods=['GET', 'POST'])
@login_required
def peixun_apply():
    form = PeixunApplyForm()
    if check_jihuo_status(session['username']) == False:
        flash('请等待管理员认证')
        return render_template('houtai/blank.html')
    if request.method == 'POST':
        if form.validate_on_submit():
            account_username = session['username']
            user_type = check_user_type(session['username'])
            username = form.username.data
            phone = form.phone.data
            card_num = form.card_num.data
            address =form.address.data
            date = form.date.data
            reason = form.reason.data
            content = form.content.data
            obj = PeixunApplyModel(account_username=account_username, account_type=user_type, username=username, phone=phone,
                                   card_num=card_num, address=address, date=date, reason=reason,content=content)
            db.session.add(obj)
            db.session.commit()
            flash('提交成功')
            return render_template('houtai/peixun_apply.html', form=form)
    return render_template('houtai/peixun_apply.html', form=form)


@main.route('/main/fee_apply.html', methods=['GET','POST'])
@login_required
def fee_apply():
    form = FeeApplyForm()
    if check_jihuo_status(session['username']) == False:
        flash('请等待管理员认证')
        return render_template('houtai/blank.html')
    # get the patent id
    patent_id_obj = PatentApplyModel.query.filter_by(account_username=session['username'],check_status='2checked').all()
    if request.method == 'POST':
        if form.validate_on_submit():
            account_username = session['username']
            user_type = check_user_type(session['username'])
            patent_id = form.patent_id.data
            name = form.name.data
            phone = form.phone.data
            date = form.date.data
            description = form.description.data
            obj = FeeApplyModel(account_username=account_username,account_type=user_type,patent_id=patent_id,
                                name=name,phone=phone,date=date,description=description)
            db.session.add(obj)
            db.session.commit()
            flash('提交成功')
            return render_template('houtai/fee_apply.html', form=form, info=patent_id_obj)
        else:
            flash('提交失败，请查看专利号是否已经审查')
    return render_template('houtai/fee_apply.html', form=form, info=patent_id_obj)


@main.route('/main/fee_record.html', methods=['GET'])
@login_required
def fee_record():
    if check_jihuo_status(session['username']) == False:
        flash('请等待管理员认证')
        return render_template('houtai/blank.html')
    obj = FeeApplyModel.query.filter_by(account_username=session['username']).all()
    return render_template('houtai/fee_record.html', info=obj)


@main.route('/main/trade_apply.html', methods=['GET', 'POST'])
@login_required
def trade_apply():
    if check_jihuo_status(session['username']) == False:
        flash('请等待管理员认证')
        return render_template('houtai/blank.html')
    form = TradeApplyForm()
    # get my own patent id in order to trade
    obj = PatentApplyModel.query.filter_by(account_username=session['username'],check_status='2checked').all()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            phone = form.phone.data
            date = form.date.data
            patent_id = form.patent_id.data
            obj1 = PatentApplyModel.query.filter_by(id=patent_id,check_status='2checked',account_username=session['username']).first()
            if not obj1:
                flash('交易专利号不合法，请检查专利号是否存在或通过审查')
                flash('请重新提交')
                render_template('houtai/trade_apply.html', form=form)
            else:
                tmp = PatentApplyModel.query.filter_by(id=patent_id).first()
                description = tmp.description
                obj2 = TradeApplyModel(apply_per_name=username,patent_id=patent_id,apply_per_phone=phone,date=date,apply_description=description)
                db.session.add(obj2)
                db.session.commit()
                flash('提交成功')
                render_template('houtai/trade_apply.html', form=form, info=obj)
    return render_template('houtai/trade_apply.html',form=form, info=obj)


@main.route('/main/trade_perchase.html', methods=['GET', 'POST'])
@login_required
def trade_perchase():
    if check_jihuo_status(session['username']) == False:
        flash('请等待管理员认证')
        return render_template('houtai/blank.html')
    form = TradePerchaseForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            phone = form.phone.data
            date = form.date.data
            patent_id = form.patent_id.data
            obj1 = TradeApplyModel.query.filter_by(id=patent_id,check_status='checked').first()
            if not obj1:
                flash('交易专利号不合法，请检查专利号是否存在或通过审查')
                flash('请重新提交')
                render_template('houtai/trade_perchase.html', form=form)
            else:
                obj2 = TradePerchaseModel(perchase_per_name=username,patent_id=patent_id,date=date,perchase_per_phone=phone)
                db.session.add(obj2)
                db.session.commit()
                TradeMarketModel.query.filter_by(patent_id=patent_id).update({'status':'perchased'})
                db.session.commit()
    if request.args.get('id'):
        id = request.args.get('id')
    else:
        id = None
    return render_template('houtai/trade_perchase.html',form=form, id=id)


@main.route('/main/trade_market.html', methods=['GET', 'POST'])
@login_required
def trade_market():
    if check_jihuo_status(session['username']) == False:
        flash('请等待管理员认证')
        return render_template('houtai/blank.html')
    tradeinfo = TradeMarketModel.query.filter_by(status='onsale').all()
    print tradeinfo
    return render_template('houtai/trade_market.html', tradeinfo=tradeinfo)


@main.route('/main/user_info.html', methods=['GET'])
@login_required
def user_info():
    # check user
    user_type = check_user_type(session['username'])
    if user_type == 'person':
        if check_jihuo_status(session['username']):
            userinfo = PersonInfoModel.query.filter_by(mail_address=session['username']).first()
        else:
            userinfo = PersonRegisterModel.query.filter_by(mail_address=session['username']).first()
    else:
        if check_jihuo_status(session['username']):
            userinfo = CompanyInfoModel.query.filter_by(mail_address=session['username']).first()
        else:
            userinfo = CompanyRegisterModel.query.filter_by(mail_address=session['username']).first()
    return render_template('houtai/user_info.html', userinfo=userinfo, user_type=user_type)


@main.route('/a/a/a/doing', methods=['GET'])
def doing():
    return render_template('doing.html')


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

