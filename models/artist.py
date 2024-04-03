#!/usr/bin/env python3
""" Artist model """
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from models.base import Base, BaseTune


class Artist(BaseTune, Base):
    """album"""

    __tablename__ = "artists"

    name = Column(String(128))
    follower = Column(Integer, default=0)
    popularity = Column(Integer, default=0)
    genre_id = Column(String(60), ForeignKey("genres.id"))
    nb_album = Column(Integer, default=0)
    monthly_listener = Column(Integer, default=0)

    genres = relationship("Genre", back_populates="artists")
    albums = relationship("Album", back_populates="artists")
    tracks = relationship("Track", back_populates="artists")
