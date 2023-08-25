#!/usr/bin/python3
"""
Model class for states
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


meta_data = MetaData()
Base = declarative_base(metadata=meta_data)

class State(Base):
    """
    Class model for state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
