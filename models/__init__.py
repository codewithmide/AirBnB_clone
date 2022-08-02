#!/usr/bin/python3
"""
A unique FileStorage instance for the website
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
