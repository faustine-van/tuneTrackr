#!/usr/bin/python3
"""
initialize the models package
"""
from models.storage.db import DBStorage

dbStorage = DBStorage()
dbStorage.reload()
