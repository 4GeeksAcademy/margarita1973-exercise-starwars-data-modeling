import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users (Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(10), nullable=False)

    def to_dict(self):
        return {}

class Planets (Base):
    __tablename__ = 'planets'
    id = Column (primary_key=True, nullable=False) 
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
    mass = Column(Integer)
    hair_color = Column (String(10))
    skin_color = Column (String(10))
    eye_color = Column (String(10))
    birth_year = Column (Date)
    gender = Column (String(10))
    created = Column (Date)
    edited = Column (Date)
    homeworld = Column (String(50), ForeignKey(Planets.url))

    def to_dict(self):
        return {}

class Favorites(Base): 
    __tablename__= 'favorites'
    id =Column (Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey (Users.id))
    planet_name = Column(String(30), ForeignKey(Planets.name))
    people_name = Column(String(30), ForeignKey(People.name))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
