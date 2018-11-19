from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    surname = Column(String(20))
    password = Column(String(20))
    money = Column(Integer)
    bank = Column(String(40))

class Transaction(Base):
    __tablename__='transactions'
    id = Column(Integer, primary_key = True)
    sender = Column(Integer, ForeignKey('user.id'))
    receiver = Column(Integer, ForeignKey('user.id'))
    ammount = Column(Integer)
    transaction_date = Column(Date)

    sender_r = relationship("User", foreign_keys=[sender])
    receiver_r = relationship("User", foreign_keys=[receiver])