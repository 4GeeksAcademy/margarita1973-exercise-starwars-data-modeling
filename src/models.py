import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(10), nullable=False)

    def to_dict(self):
        return {}

class Planet (Base):
    __tablename__ = 'planet'
    id = Column (Integer, primary_key=True, nullable=False) 
    name = Column (String(30), unique=True, nullable=False)
    url = Column(String(50), unique= True, nullable=False)
    diameter= Column(Integer)
    rotation_period =Column (Integer)
    orbital_period = Column (Integer)
    gravity = Column (String(20))
    population = Column (Integer)
    climate = Column (String(30))
    terrain  = Column (String(30))
    surface_water = Column (Integer)
    created = Column (Date)
    edited = Column(Date)

    def to_dict(self):
        return {}
    
    
class People (Base):
    __tablename__ = 'people'
    id =Column(Integer, primary_key=True)
    name = Column (String(30), unique=True, nullable=False)
    url= Column (String(50), unique=True, nullable=False)     
    height= Column (Integer)
    mass = Column (Integer)
    hair_color = Column (String(10))
    skin_color = Column (String(10))
    eye_color = Column (String(10))
    birth_year = Column (Date)
    gender = Column (String(10))
    created = Column (Date)
    edited = Column (Date)
    homeworld = Column (Integer, ForeignKey(Planet.id))

    def to_dict(self):
        return {}

class Favorites(Base): 
    __tablename__= 'favorites'
    id =Column (Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey (User.id))
    planet_id = Column(Integer, ForeignKey(Planet.id))
    people_id = Column(Integer, ForeignKey(People.id))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
