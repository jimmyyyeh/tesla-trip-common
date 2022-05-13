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


class User(db.Model):
    """
    使用者
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, nullable=False, server_default=text('1'), comment='角色')
    username = db.Column(db.String(30), nullable=False, unique=True, comment='帳號')
    password = db.Column(db.String(100), nullable=False, comment='密碼')
    nickname = db.Column(db.String(30), nullable=False, comment='暱稱')
    email = db.Column(db.String(100), nullable=False, comment='電子郵件')
    birthday = db.Column(db.Date, comment='生日')
    sex = db.Column(db.Integer, nullable=False, comment='性別')
    charger_id = db.Column(db.Integer, db.ForeignKey('super_charger.id'), comment='管理超充 id')
    is_verified = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='是否已驗證')
    point = db.Column(db.Integer, nullable=False, server_default=text('0'), comment='積分')

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')


class PointLog(db.Model):
    """
    使用者
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'point_log'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment='使用者 id')
    type = db.Column(db.Integer, nullable=False, comment='分類')
    point = db.Column(db.Integer, nullable=False, comment='點數快照')
    change = db.Column(db.Integer, nullable=False, comment='增減數')

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')


class Car(db.Model):
    """
    車輛資料
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment='使用者 id')
    model = db.Column(db.String(10), comment='型號')
    spec = db.Column(db.String(30), comment='規格')
    manufacture_date = db.Column(db.Date, comment='出廠日期')
    has_image = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='是否擁有圖片')

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')


class CarModel(db.Model):
    """
    車種型號
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'car_model'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(10), comment='型號')
    spec = db.Column(db.String(30), comment='規格')

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')


class AdministrativeDistrict(db.Model):
    """
    行政區列表
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'administrative_district'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(10), nullable=False, comment='縣市')
    area = db.Column(db.String(10), nullable=False, comment='區域')

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')


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


class Trip(db.Model):
    """
    旅程
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'trip'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment='使用者 id')
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False, comment='車輛 id')
    mileage = db.Column(db.Integer, comment='滿電里程')
    consumption = db.Column(db.Float, comment='平均電力')
    total = db.Column(db.Float, comment='電量總計')
    start = db.Column(db.String(30), nullable=False, comment='起點')
    end = db.Column(db.String(30), nullable=False, comment='終點')
    start_battery_level = db.Column(db.Integer, comment='起點電量')
    end_battery_level = db.Column(db.Integer, comment='終點電量')
    is_charge = db.Column(db.Boolean, server_default=text('0'), comment='是否充電')
    charger_id = db.Column(db.Integer, db.ForeignKey('super_charger.id'), comment='超充站 id')
    charge = db.Column(db.Integer, comment='充電%數')
    fee = db.Column(db.Integer, comment='充電費用')
    trip_date = db.Column(db.Date, nullable=False, comment='旅程日期')

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')


class TripRate(db.Model):
    """
    旅程評分
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'trip_rate'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment='使用者 id')
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'), nullable=False, comment='旅程 id')

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')


class Product(db.Model):
    """
    產品
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, comment='名稱')
    point = db.Column(db.Integer, nullable=False, comment='點數')
    stock = db.Column(db.Integer, nullable=False, comment='庫存')
    charger_id = db.Column(db.Integer, db.ForeignKey('super_charger.id'), nullable=False, comment='超充站 id')
    is_launched = db.Column(db.Boolean, nullable=False, server_default=text('0'), comment='是否上架')

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')


class RedeemLog(db.Model):
    """
    兌換紀錄
    """
    __bind_key__ = BIND_KEY
    __tablename__ = 'redeem_log'
    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment='賣方 id')
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment='買方 id')
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False, comment='產品 id')

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), comment='建立時間')
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                                comment='更新時間')
