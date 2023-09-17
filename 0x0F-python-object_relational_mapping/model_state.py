#!/usr/bin/python3
""" contains state class and base, an instance of declarative_base() """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """ Class with id and name attributes """

    __tablename__ = 'states'
    id = Column(Integer,unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)