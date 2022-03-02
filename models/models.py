# -*- coding: utf-8 -*
"""
      ┏┓       ┏┓
    ┏━┛┻━━━━━━━┛┻━┓
    ┃      ☃      ┃
    ┃  ┳┛     ┗┳  ┃
    ┃      ┻      ┃
    ┗━┓         ┏━┛
      ┗┳        ┗━┓
       ┃          ┣┓
       ┃          ┏┛
       ┗┓┓┏━━━━┳┓┏┛
        ┃┫┫    ┃┫┫
        ┗┻┛    ┗┻┛
    God Bless,Never Bug
"""

from sqlalchemy import func, text

from app import db, config

BIND_KEY = config['DB_NAME']


class SuperCharger(db.Model):
    """
    超充站列表
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'super_charger'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, comment='名稱')
    city = db.Column(db.String(10), nullable=False, comment='縣市')
    tpc = db.Column(db.Integer, comment='tpc數量')
    ccs2 = db.Column(db.Integer, comment='ccs2數量')
    floor = db.Column(db.String(10), comment='樓層')
    business_hours = db.Column(db.String(30), comment='營業時間')
    park_fee = db.Column(db.String(10), comment='停車費率')
    charger_fee = db.Column(db.String(10), comment='充電費率')
    version = db.Column(db.String(10), comment='版本')

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')
