# -*- coding: utf-8 -*-
__author__ = 'Edward'
from sqlalchemy import Column,String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class User(Base):
    __tablename__='user'
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    books=relationship('Book')
class Book(Base):
    __tablename__='book'
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    user_id=Column(String(20),ForeignKey('user.id'))
engine=create_engine('mysql+pymysql://root:151480@localhost:3306/test')
DBsession=sessionmaker(bind=engine)
session=DBsession()
new_user=User(id='35',name='Bob')
new_book=Book(id='15',name='Ana')
session.add(new_user)
session.add(new_book)
session.commit()
session.close()
session=DBsession()
user=session.query(User).filter(User.id=='33').first()
print('type:',type(user))
print(user.name)
session.close()
