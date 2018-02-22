#! -*-coding:utf-8 -*-
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user

from . import main


@main.route('/main', methods=['GET', 'POST'])
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
    return render_template('houtai/head.html')


@main.route('/main/patent_apply.html', methods=['GET'])
@login_required
def patent_apply():
    return render_template('houtai/patent_apply.html')


@main.route('/main/patent_record.html', methods=['GET'])
@login_required
def patent_record():
    return render_template('houtai/patent_record.html')


@main.route('/main/peixun_record.html', methods=['GET'])
@login_required
def peixun_record():
    return render_template('houtai/peixun_record.html')


@main.route('/main/peixun_apply.html', methods=['GET'])
@login_required
def peixun_apply():
    return render_template('houtai/peixun_apply.html')