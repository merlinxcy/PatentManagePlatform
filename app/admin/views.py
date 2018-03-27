#! -*- coding:utf-8 -*-
from flask import session,redirect,url_for,request,render_template,jsonify

from . import admin,username,password
from ..models import TradePerchaseModel,TradeMarketModel,PersonRegisterModel,CompanyRegisterModel,PersonInfoModel,CompanyInfoModel,PatentApplyModel,FeeApplyModel,PeixunApplyModel,TradeApplyModel,db


def login_check():
    if 'flag' in session:
        if session['flag'] == 'admin':
            return True
    return False


@admin.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if login_check():
        return render_template('admin/admin.html')
    if request.method == 'GET':
        return render_template('admin/login.html')
    if request.method == 'POST':
        if request.form['username'] == username and request.form['password'] == password:
            session['flag'] = 'admin'
            return redirect(url_for('admin.admin'))
    return render_template('admin/login.html')


@admin.route('/admin_logout', methods=['GET', 'POST'])
def admin_logout():
    if login_check():
        session.pop('flag', None)
        return redirect(url_for('admin.admin_login'))
    return redirect(url_for('admin.admin_login'))


@admin.route('/admin/patent_apply_manager')
def patent_apply_manager():
    if login_check() == False:
        return render_template('admin/login.html')
    else:
        u = PatentApplyModel.query.all()

        return render_template('admin/patent_apply_manager.html', userinfo=u)


@admin.route('/admin/fee_apply_manager')
def fee_apply_manager():
    if login_check() == False:
        return render_template('admin/login.html')
    else:
        u = FeeApplyModel.query.all()
        return render_template('admin/fee_apply_manager.html', userinfo=u)


@admin.route('/admin/peixun_apply_manager')
def peixun_apply_manager():
    if login_check() == False:
        return render_template('admin/login.html')
    else:
        u = PeixunApplyModel.query.all()
        return render_template('admin/peixun_apply_manager.html', userinfo=u)


@admin.route('/admin/register_manager')
def register_manager():
    if login_check() == False:
        return render_template('admin/login.html')
    else:
        u = PersonRegisterModel.query.filter_by(register_status=0).all()
        return render_template('admin/register_manager.html', userinfo = u)


@admin.route('/admin/api/register_manager/check', methods=['POST'])
def register_manager_check():
    if login_check() == True:
        id = request.form.get('id')
        if id:
            # 将注册表转移到用户信息表，并更新状态
            PersonRegisterModel.query.filter_by(id=id).update({'register_status': 1})
            db.session.commit()
            # 同步
            query = PersonRegisterModel.query.filter_by(id=id).first()
            id = query.id
            name = query.name
            phone = query.phone
            location = query.location
            card_type = query.card_type
            card_num = query.card_num
            address = query.address
            mail_address = query.address
            obj = PersonInfoModel(id=id, name=name, phone=phone, location=location,
                                  card_type=card_type, card_num=card_num, address=address,
                                  mail_address=mail_address)
            db.session.add(obj)
            db.session.commit()
            return 'ok'
        else:
            return 'error'
    else:
        return 'no auth'


@admin.route('/admin/api/register_manager/get',methods=['POST'])
def register_manager_get():
    if login_check() == True:
        id = request.form.get('id')
        if id:
            obj = PersonRegisterModel.query.filter_by(id=id).first()
            if obj:
                name = obj.name
                phone = obj.phone
                location = obj.location
                card_type = obj.card_type
                card_num = obj.card_num
                address = obj.address
                mail_address = obj.mail_address
                result={'name':name,'phone':phone,'location':location,
                        'card_type':card_type,'card_num':card_num,
                        'address':address,'mail_address':mail_address}
                return jsonify(result)
            else:
                return 'error'
        else:
            return 'error'
    else:
        return 'no auth'


@admin.route('/admin/company_register_manager.html')
def company_register_manager():
    if login_check() == False:
        return render_template('admin/login.html')
    else:
        u = CompanyRegisterModel.query.filter_by(register_status=0).all()
        return render_template('admin/company_register_manager.html',userinfo=u)


@admin.route('/admin/api/company_register_manager/check', methods=['POST'])
def company_register_manager_check():
    if login_check() == True:
        id = request.form.get('id')
        if id:
            # 将注册表转移到用户信息表，并更新状态
            CompanyRegisterModel.query.filter_by(id=id).update({'register_status': 1})
            db.session.commit()
            # 同步
            query = CompanyRegisterModel.query.filter_by(id=id).first()
            id = query.id
            name = query.name
            card_type = query.card_type
            card_num = query.card_num
            company_location = query.company_location
            location_code = query.location_code
            address = query.address
            mail_address = query.mail_address
            per_phone = query.per_phone
            per_name = query.per_name
            obj = CompanyInfoModel(id=id,name=name,card_type=card_type,
                                  card_num=card_num,company_location=company_location,
                                  location_code=location_code,address=address,
                                  mail_address=mail_address,per_phone=per_phone,
                                  per_name=per_name)
            db.session.add(obj)
            db.session.commit()
            return 'ok'
        else:
            return 'error'
    else:
        return 'no auth'


@admin.route('/admin/api/company_register_manager/get',methods=['POST'])
def company_register_manager_get():
    if login_check() == True:
        id = request.form.get('id')
        if id:
            obj = CompanyRegisterModel.query.filter_by(id=id).first()
            if obj:
                name = obj.name
                card_type = obj.card_type
                card_num = obj.card_num
                company_location = obj.company_location
                location_code = obj.location_code
                address = obj.address
                mail_address = obj.mail_address
                per_phone = obj.per_phone
                per_name = obj.per_name
                result={'name':name,'card_type':card_type,'card_num':card_num,
                        'company_location':company_location,'location_code':location_code,
                        'address':address,'mail_address':mail_address,'per_phone':per_phone,'per_name':per_name}
                return jsonify(result)
            else:
                return 'error'
        else:
            return 'error'
    else:
        return 'no auth'


@admin.route('/admin/api/patent_apply_manager/get', methods=['POST'])
def patent_apply_manager_get():
    if login_check():
        id = request.form.get('id')
        if id:
            obj = PatentApplyModel.query.filter_by(id=id).first()
            name = obj.name
            type = obj.type
            main_per_name = obj.main_per_name
            first_per_name = obj.first_per_name
            first_per_phone = obj.first_per_phone
            first_per_card_num = obj.first_per_card_num
            first_per_address = obj.first_per_address
            date = obj.date
            priority = obj.priority
            description = obj.description
            check_status = obj.check_status
            result = {'name': name, 'type': type, 'main_per_name': main_per_name,
                      'first_per_name': first_per_name, 'first_per_phone': first_per_phone,
                      'first_per_card_num': first_per_card_num, 'first_per_address': first_per_address,
                      'date': date, 'priority': priority, 'description': description, 'check_status': check_status}
            return jsonify(result)
        else:
            return 'error'
    else:
        return 'no auth'


@admin.route('/admin/api/patent_apply_manager/action', methods=['POST'])
def patent_apply_manager_action():
    if login_check():
        id = request.form.get('id')
        action = request.form.get('action')
        if id and action:
            if action == '1checked':
                PatentApplyModel.query.filter_by(id=id).update({'check_status': '1checked'})
            elif action == '2checked':
                PatentApplyModel.query.filter_by(id=id).update({'check_status': '2checked'})
            elif action == 'reject':
                PatentApplyModel.query.filter_by(id=id).update({'check_status': 'reject'})
            else:
                return 'error'
            db.session.commit()
            return 'ok'
        else:
            return 'error'
    else:
        return 'no auth'


@admin.route('/admin/api/fee_apply_manager/get', methods=['POST'])
def fee_apply_manager_get():
    if login_check():
        id = request.form.get('id')
        if id:
            obj = FeeApplyModel.query.filter_by(id=id).first()
            patent_id = obj.patent_id
            name = obj.name
            phone = obj.phone
            date = obj.date
            description = obj.description
            check_status = obj.check_status
            # patent
            obj = PatentApplyModel.query.filter_by(id=patent_id).first()
            patent_name = obj.name
            result = {'name': name, 'phone':phone, 'date': date, 'description': description,
                      'check_status': check_status, 'patent_name': patent_name, 'patent_id': patent_id}
            return jsonify(result)
        return 'error'
    return 'no auth'


@admin.route('/admin/api/fee_apply_manager/check', methods=['POST'])
def fee_apply_manager_action():
    if login_check():
        id = request.form.get('id')
        action = request.form.get('action')
        if id and action:
            if action == 'checked':
                FeeApplyModel.query.filter_by(id=id).update({'check_status': 'checked'})
            elif action == 'reject':
                FeeApplyModel.query.filter_by(id=id).update({'check_status': 'reject'})
            else:
                return 'error'
            db.session.commit()
            return 'ok'
        else:
            return 'error'
    return 'no auth'


@admin.route('/admin/api/peixun_apply_manager/check', methods=['POST'])
def peixun_apply_manager_action():
    if login_check():
        id = request.form.get('id')
        action = request.form.get('action')
        if id and action:
            if action == 'checked':
                PeixunApplyModel.query.filter_by(id=id).update({'check_status': 'checked'})
            elif action == 'reject':
                PeixunApplyModel.query.filter_by(id=id).update({'check_status': 'reject'})
            else:
                return 'error'
            db.session.commit()
            return 'ok'
        else:
            return 'error'
    return 'no auth'


@admin.route('/admin/api/peixun_apply_manager/get', methods=['POST'])
def peixun_apply_manager_get():
    if login_check():
        id = request.form.get('id')
        if id:
            obj = PeixunApplyModel.query.filter_by(id=id).first()
            username = obj.username
            phone = obj.phone
            card_num = obj.card_num
            address = obj.address
            date = obj.date
            reason = obj.reason
            content = obj.content
            check_status = obj.check_status
            result = {'username': username, 'phone': phone, 'card_num': card_num,
                      'address': address, 'date': date, 'reason': reason,
                      'content': content, 'check_status': check_status}
            return jsonify(result)
        return 'error'
    return 'no auth'


@admin.route('/admin/trade_apply_manager.html', methods=['GET'])
def trade_apply_manager():
    if login_check():
        userinfo = []
        obj = TradeApplyModel.query.all()
        for i in obj:
            patent_id = i.patent_id
            patent_name = PatentApplyModel.query.filter_by(id=patent_id).first().name
            apply_per_name = i.apply_per_name
            id = i.id
            userinfo.append({'patent_name':patent_name,'apply_per_name':apply_per_name,'id':id})
        return render_template('admin/trade_apply_manager.html', userinfo=userinfo)
    else:
        return render_template('admin/login.html')


@admin.route('/admin/api/trade_apply_manager/get', methods=['POST'])
def trade_apply_manager_get():
    if login_check():
        if request.form.get('id'):
            id = request.form.get('id')
            obj = TradeApplyModel.query.filter_by(id=id).first()
            patent_id = obj.patent_id
            apply_per_name = obj.apply_per_name
            apply_per_phone = obj.apply_per_phone
            date = obj.date
            apply_description = obj.apply_description
            check_status = obj.check_status
            result = {'patent_id':patent_id, 'apply_per_name':apply_per_name,
                      'apply_per_phone':apply_per_phone,'date':date,
                      'apply_description':apply_description,'check_status':check_status}
            return jsonify(result)
        else:
            return 'error'
    else:
        return 'no auth'


@admin.route('/admin/api/trade_apply_manager/check', methods=['POST'])
def trade_apply_manager_check():
    if login_check():
        id = request.form.get('id')
        if id:
            TradeApplyModel.query.filter_by(id=id).update({'check_status': 'checked'})
            db.session.commit()
            # TradeMarketModel
            obj1 =  TradeApplyModel.query.filter_by(id=id).first()
            obj2 = PatentApplyModel.query.filter_by(id=obj1.patent_id).first()
            patent_id = obj1.patent_id
            patent_name = obj2.name
            main_per_name = obj1.apply_per_name
            description = obj1.apply_description
            apply_date = obj1.date
            status = 'onsale'
            obj = TradeMarketModel(patent_id=patent_id, patent_name=patent_name,
                                  main_per_name=main_per_name, description=description,
                                  apply_date=apply_date,status=status)
            db.session.add(obj)
            db.session.commit()
            return 'ok'
        else:
            return 'error'
    else:
        return 'no auth'


@admin.route('/admin/trade_perchase_manager.html', methods=['GET','POST'])
def trade_perchase_manager():
    if login_check() == False:
        return render_template('admin/login.html')
    else:
        info = TradePerchaseModel.query.filter_by(check_status='checking').all()
        tmp =[]
        for i in info:
            perchase_per_name = i.perchase_per_name
            patnent_id = i.patent_id
            date = i.date
            patent_name = PatentApplyModel.query.filter_by(id=i.patent_id).first().name
            tmp.append({'patent_name':patent_name,'perchase_per_name':perchase_per_name,'date':date,'id':patnent_id})
        return render_template('admin/trade_perchase_manager.html', info=tmp)


@admin.route('/admin/api/trade_perchase_manager/check',methods=['POST'])
def trade_perchase_manager_check():
    if login_check():
        id = request.form.get('id')
        if id:
            patent_id = TradePerchaseModel.query.filter_by(id=id).first().patent_id
            TradePerchaseModel.query.filter_by(patent_id=patent_id).update({'check_status':'checked'})
            TradeMarketModel.query.filter_by(patent_id=patent_id).update({'status':'saled'})
            db.session.commit()
            print 'ok'
            return 'ok'
        else:
            return 'error'
    else:
        return 'no auth'


@admin.route('/admin/head.html')
def head():
    return render_template('admin/head.html')


@admin.route('/admin/blank.html')
def blank():
    return render_template('admin/blank.html')


@admin.route('/admin/left.html')
def left():
    return render_template('admin/left.html')


@admin.route('/admin', methods=['GET'])
def admin():
    if login_check() == False:
        return render_template('admin/login.html')
    else:
        return render_template('admin/admin.html')


# @admin.route('/admin_logout', methods=['GET'])
# def admin_logout():
#     session.pop('flag', None)
#     return redirect(url_for('admin.admin_login'))


