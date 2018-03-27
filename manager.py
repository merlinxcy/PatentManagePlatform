#! coding:utf-8
from app import *
import sys

reload(sys)
sys.setdefaultencoding('utf8')# linux system zhuangyong


if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host='0.0.0.0')

