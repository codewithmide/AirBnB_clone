#!/usr/bin/python3
"""
A unique FileStorage instance for the website
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
