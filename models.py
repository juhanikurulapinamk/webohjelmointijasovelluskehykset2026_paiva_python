import sqlite3

from custom_exceptions.not_found_exception import NotFoundException


class User:
    def __init__(self, firstname, lastname, username, _id=None):
        self._id = _id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username

    @property
    def id(self):
        return self._id

    
            
                
        