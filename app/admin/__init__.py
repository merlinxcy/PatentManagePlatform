#! -*- coding:utf-8 -*-
from flask import Blueprint


admin = Blueprint('admin', __name__)
username = 'admin_oth'
password = 'zxcasdqwe123'
import views
import errors
