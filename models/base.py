#!/usr/bin/env python3
""" Base model """
from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models


FORMAT = "%Y-%m-%dT%H:%M:%S"
Base = declarative_base()


class BaseTune:
    """Basic class

    Args:
        id (int):
        create_at (datetime): indication when created
        updated_at (datetime): indicating when last updated
    """

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(),
                        onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """initialize of BaseTune class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, val in kwargs.items():
                if key != "__class__":
                    setattr(self, key, val)
            if kwargs.get("created_at", None) and isinstance(self.created_at,
                                                             str):
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    FORMAT)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and isinstance(self.updated_at,
                                                             str):
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    FORMAT)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """representation of Base class"""
        return f"[{self.__class__.__name__}] (ID: {self.id})"

    def save(self):
        """add and save objects in database"""
        self.updated_at = datetime.utcnow()
        models.dbStorage.new(self)
        models.dbStorage.save()

    def to_json(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(FORMAT)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(FORMAT)
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict
