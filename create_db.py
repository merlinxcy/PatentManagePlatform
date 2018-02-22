#!-*- coding: utf-8 -*-
from app import *

if __name__ == '__main__':
    db.init_app(app) # 解决
    db.create_all() #Issue 002

