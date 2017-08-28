import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(String(90),nullable = False)
    rid = Column(Integer, primary_key = True)

class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(90),nullable = False)
    mid = Column(Integer, primary_key = True)
    course = Column(String(300))
    description = Column(String(300))
    price = Column(String(10))
    restaurant_id = Column(Integer,ForeignKey('restaurant.rid'))
    restaurant = relationship(Restaurant)

# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.mid,
            'price': self.price,
            'course': self.course,
        }


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)