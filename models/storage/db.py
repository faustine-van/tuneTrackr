#!/usr/bin/python3
"""class DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base import Base
from models.user import User, Role
from config import Config
from models.genre import Genre
from models.album import Album
from models.artist import Artist
from models.track import Track

cfg = Config()
classes = {
    "User": User,
    "Role": Role,
    "Track": Track,
    "Album": Album,
    "Genre": Genre,
    "Artist": Artist,
}


class DBStorage:
    """working with Database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        user = cfg.DB_USER
        passw = cfg.DB_PASS
        host = cfg.DB_HOST
        db = cfg.DB_TUNETRACKR
        uri = f"mysql+mysqldb://{user}:{passw}@{host}/{db}"
        self.__engine = create_engine(uri)

    def all(self, cls=None) -> list:
        """Returns all objects of a given class from the database.

        Args:
            cls (optional): The class of objects to retrieve.
              If not provided, all objects from all classes will be returned.

        Returns:
            list: A list of objects of the specified class,
                  or all objects if cls is None.
                  Returns an empty list if no objects are found.
        """
        result = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    result[key] = obj
        return result

    def get(self, cls, id) -> dict:
        """Returns the object with the specified ID from the database.

        Args:
            cls: The class of the object to retrieve.
            id: The ID of the object to retrieve.

        Returns:
            object: The object with the specified ID, or None if not found.
        """
        if cls not in classes.values():
            return None
        objs = models.dbStorage.all(cls)
        for obj in objs.values():
            if obj.id == id:
                return obj
        return None

    def search(self, cls, attrs={}) -> dict:
        """Searches for objects in the database based on specified attributes.

        Args:
            attrs (dict): A dictionary containing attributes and their
                            corresponding values to search for.

        Returns:
            dict: A dictionary containing objects that match the
                    specified attributes. If no objects match the search
                    criteria, an empty dictionary is returned.
        """
        if attrs is None:
            return None
        if cls not in classes.values():
            return None
        results = {}
        objs = models.dbStorage.all(cls)
        for obj in objs.values():
            match = True
            for key, val in attrs.items():
                if getattr(obj, key) != val:
                    match = False
                    break
            if match:
                results[obj.id] = obj
        return results

    def count(self, cls=None) -> int:
        """Counts the number of objects in the database.

        Returns:
            int: The total number of objects in the database.
        """

        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.dbStorage.all(clas).values())
        else:
            count = len(models.dbStorage.all(cls).values())

        return count

    def new(self, obj):
        """Adds a new object to the database.

        Args:
            obj: The object to add to the database.
        """
        self.__session.add(obj)

    def save(self):
        """Saves changes to the database."""
        self.__session.commit()

    def reload(self):
        """Reloads data from the database session."""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine)
        session = scoped_session(sess_factory)
        self.__session = session

    def remove(self, obj=None):
        """Removes an object from the database session.

        Args:
            obj (optional): The object to remove from the
                database session. If not provided, removes all objects.
        """
        if object is not None:
            self.__session.delete(obj)

    def close(self):
        """Closes the database session."""
        self.__session.remove()
