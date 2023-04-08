from sqlalchemy import Column, ForeignKey, String, Integer, Date, CHAR, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import *
from config.config import *
import os

class Database:
    def __init__(self, data=None):
        self.params = self.set_params()
        self.engine = create_engine(f'postgresql://{self.params[0]}:{self.params[1]}@localhost:{self.params[3]}/'
                                    f'{self.params[2]}')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.data = data

    def add_all(self, document_path):
        try:
            self.create_metadata()
            customer_id = self.add_customer(self.data['customer'])
            placer_id = self.add_placer(self.data['placer'])
            maindata_id = self.add_maindata(self.data['maindata'], customer_id, placer_id)
            self.add_lots(self.data['lots'], maindata_id)

            """Delete xml after parsing"""
            os.remove(document_path)
        except OperationalError as err:
            print(err)


    def set_params(self):
        return get_data()

    def create_metadata(self):
        Base.metadata.create_all(self.engine)

    def add(self, obj):
        self.session.add(obj)
        self.session.flush()
        id = obj.id
        try:
            self.session.commit()
        except IntegrityError as err:
            self.session.rollback()
            print(err)
        self.session.close()
        return id

    def add_customer(self, data):
        customer = self.session.query(Customer).filter(Customer.inn == data['inn'],
                                                       Customer.fullname == data['fullname']).first()
        if customer:
            return customer.id
        else:
            customer = Customer(data)
            return self.add(customer)

    def add_placer(self, data):
        placer = self.session.query(Placer).filter(Placer.inn == data['inn'],
                                                   Placer.fullname == data['fullname']).first()
        if placer:
            return placer.id
        else:
            placer = Placer(data)
            return self.add(placer)

    def add_maindata(self, data, customer_id, placer_id):
        main_data = self.session.query(Main_data).filter(Main_data.guid == data['guid']).first()
        if main_data:
            return main_data.id
        else:
            main_data = Main_data(data, customer_id, placer_id)
            return self.add(main_data)

    def add_lots(self, data, maindata_id):
        for row in data:
            lot = Lots(row, maindata_id)
            self.session.add(lot)
        try:
            self.session.commit()
        except IntegrityError as err:
            self.session.rollback()
            print(err)

    def placer_by_id(self, id):
        placer = self.session.query(Placer).filter(Placer.id == id).first()
        if placer:
            return placer.id
        else:
            return "no data"

    def customer_by_id(self, id):
        customer = self.session.query(Customer).filter(Customer.id == id).first()
        if customer:
            return customer.id
        else:
            return "no data"

    def maindata_by_id(self, id):
        data = self.session.query(Main_data).filter(Main_data.id == id).first()
        if data:
            return data.id
        else:
            return "no data"


"""Create a base class"""
Base = declarative_base()
"""Tables"""
"""1.Main_data"""


class Main_data(Base):
    __tablename__ = "main_data"
    id = Column(Integer, primary_key=True)
    region = Column(String)
    notice_number = Column(String)
    name = Column(String)
    guid = Column(String)
    create_datetime = Column(Date)
    publication_datetime = Column(Date)
    modification_datetime = Column(Date)
    version = Column(Integer)
    status = Column(CHAR)
    purchase_codename = Column(String)
    bitmask = Column(String)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    placer_id = Column(Integer, ForeignKey("placers.id"))

    def __init__(self, maindata, customer_id, placer_id):
        self.region = maindata['region']
        self.notice_number = maindata['notice_number']
        self.name = maindata['name']
        self.guid = maindata['guid']
        self.create_datetime = maindata['create_datetime']
        self.publication_datetime = maindata['publication_datetime']
        self.modification_datetime = maindata['modification_datetime']
        self.version = maindata['version']
        self.status = maindata['status']
        self.purchase_codename = maindata['purchase_codename']
        self.bitmask = maindata['bitmask']
        self.customer_id = customer_id
        self.placer_id = placer_id


"""2.Placers"""


class Placer(Base):
    __tablename__ = "placers"
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    shortname = Column(String)
    inn = Column(String)
    kpp = Column(String)
    ogrn = Column(String)
    legal_address = Column(String)
    postal_address = Column(String)
    bitmask = Column(String)

    def __init__(self, placer):
        self.fullname = placer['fullname']
        self.shortname = placer['shortname']
        self.inn = placer['inn']
        self.kpp = placer['kpp']
        self.ogrn = placer['ogrn']
        self.legal_address = placer['legal_address']
        self.postal_address = placer['postal_address']
        self.bitmask = placer['bitmask']


"""3.Customer"""


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    shortname = Column(String)
    inn = Column(String)
    kpp = Column(String)
    ogrn = Column(String)
    legal_address = Column(String)
    postal_address = Column(String)
    bitmask = Column(String)

    def __init__(self, customer):
        self.fullname = customer['fullname']
        self.shortname = customer['shortname']
        self.inn = customer['inn']
        self.kpp = customer['kpp']
        self.ogrn = customer['ogrn']
        self.legal_address = customer['legal_address']
        self.postal_address = customer['postal_address']
        self.bitmask = customer['bitmask']


"""4.Lots"""


class Lots(Base):
    __tablename__ = "lots"
    id = Column(Integer, primary_key=True)
    guid = Column(String)
    subject = Column(String)
    order_number = Column(Integer)
    initial_price = Column(Float)
    currency = Column(String)
    bitmask = Column(String)
    maindata_id = Column(Integer, ForeignKey("main_data.id"))

    def __init__(self, lots, maindata_id):
        self.guid = lots['guid']
        self.subject = lots['subject']
        self.order_number = lots['order_number']
        self.initial_price = lots['initial_price']
        self.currency = lots['currency']
        self.bitmask = lots['bitmask']
        self.maindata_id = maindata_id


