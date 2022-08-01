#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
"""
The BaseModel module
"""


# the date and time format
fdateAndTime = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """
    A class BaseModel that defines all common attributes/methods for other classes:
    Public instance attributes:
    id: string - assign with an uuid when an instance is created
    The goal is to have a unique id for each BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        This method initializes all attributes under the BaseModels
        """
