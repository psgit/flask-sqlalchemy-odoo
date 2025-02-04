from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base
from configparser import ConfigParser

config = ConfigParser()
config.readfp(open(r'db.cfg'))
db_connect_string = config.get('Database', 'connect_string')

engine = create_engine(db_connect_string, client_encoding='utf8')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()

class Bank(Base):
    __tablename__ = 'res_bank'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    state = Column(String)
    country = Column(String)
    street = Column(String)
    street2 = Column(String)
    zip = Column(String)
    city = Column(String)
    email = Column(String)
    phone = Column(String)
    bic = Column(String)

class Company(Base):
    __tablename__ = 'res_company'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Partner(Base):
    __tablename__ = 'res_partner'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    title = Column(String)
    lang = Column(String)
    website = Column(String)
    function = Column(String)
    type = Column(String)
    street = Column(String)
    street2 = Column(String)
    zip = Column(String)
    city = Column(String)
    email = Column(String)
    phone = Column(String)
    mobile = Column(String)
    company_name = Column(String)

class User(Base):
    __tablename__ = 'res_users'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    partner_id = Column(Integer,ForeignKey('res_partner.id'))
    partner = relationship(
        Partner,
        backref=backref('res_partners',
                        uselist=True,
                        cascade='delete,all'))