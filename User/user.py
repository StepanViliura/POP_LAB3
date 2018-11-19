
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    surname = Column(String(20))
    password = Column(String(20))
    money = Column(Integer)
    bank = Column(String(40))

class UserBasic(object):
    def __init__(self, first_name, mid_name, last_name):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.mid_name}'

class UserAccount(UserBasic):
    def __init__(self, first_name, mid_name, last_name, moneyAmout, bank):
        UserBasic.__init__(self, first_name, mid_name, last_name)
        self.moneyAmout = moneyAmout
        self.bank = bank
