"""Defines the schema and relationships of the application objects."""
from enum import Enum

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SqlEnum

Base = declarative_base()

class ExampleEnum(Enum):
    """You can define simple sets of enumerated values as Python enums rather than a table."""
    pass

class ExampleEntity(Base):
    """See http://docs.sqlalchemy.org/en/rel_1_1/orm/extensions/declarative/basic_use.html"""
    __tablename__ = "ExampleEntity"

