import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(String(90),nullable = false)
    rid = Column(Integer, primary_key = True)

class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(90),nullable = false)
    mid = Column(Integer, primary_key = True)
    course = Column(String(300))
    description = Column(String(300))
    price = Column(String(10))
    restaurant_id = Column(Integer,ForeignKey('restaurant.rid'))
    restaurant = relationship(Restaurant)

engine = create_  engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)