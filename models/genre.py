#!/usr/bin/env python3
""" Genre model """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base import Base, BaseTune


class Genre(BaseTune, Base):
    """album"""

    __tablename__ = "genres"

    name = Column(String(50))

    artists = relationship("Artist", back_populates="genres")
