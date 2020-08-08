#!/usr/bin/python3
"""
this module defines State with a declaritive Base
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
