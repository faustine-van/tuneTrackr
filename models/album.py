#!/usr/bin/env python3
""" Album model """
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship
from models.base import Base, BaseTune


class Album(BaseTune, Base):
    """album"""

    __tablename__ = "albums"

    title = Column(String(255))
    release_date = Column(DateTime)
    label = Column(String(128))
    popularity = Column(Integer, default=0)
    total_tracks = Column(Integer, default=0)
    artist_id = Column(String, ForeignKey("artists.id"))

    artists = relationship("Artist", back_populates="albums")
    tracks = relationship("Track", back_populates="albums")
