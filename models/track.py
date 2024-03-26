#!/usr/bin/python3
""" Track model """
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship
from models.base import Base, BaseTune

class Track(BaseTune, Base):
    """album"""
    __tablename__ = 'tracks'

    name = Column(String(255))
    artist_id = Column(String(60), ForeignKey('artists.id'))
    album_id = Column(String, ForeignKey('albums.id'))
    release_date = Column(DateTime)
    popularity = Column(Integer, default=0)
    track_rank = Column(Integer, default=0)
    track_position = Column(String, default=0)

    artists = relationship("Artist", back_populates="tracks")
    albums = relationship("Album", back_populates="tracks")
