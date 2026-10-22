

import sqlite3

from custom_exceptions.not_found_exception import NotFoundException
from models import User


class UsersSQLiteRepository:
    def __init__(self, con):
        self.connection = con

    


    def get_all(self):
        cur = self.connection.cursor()
        cur.execute("SELECT first_name, last_name, username, id FROM users")
        users = cur.fetchall()
        cur.close()
        users_list = []
        
        for row in users:
            users_list.append(
                User(row[0], row[1], row[2], _id=row[3])
            )
        return users_list
    
    def _add(self, user):
        try:
            cur = self.connection.cursor()
            
            cur.execute("INSERT INTO users(first_name, last_name, username) VALUES(?, ?, ?)",
                        (user.firstname, user.lastname, user.username))
            self.connection.commit()
            user._id = cur.lastrowid
            cur.close()
        except Exception as e:
            self.connection.rollback()
            raise e

    def _update(self, user):
        try:    
            cur = self.connection.cursor()
            cur.execute("UPDATE users SET first_name = ?, last_name = ?, username = ?  WHERE id = ?",
                        (user.firstname, user.lastname, user.username, user._id))
            self.connection.commit()
            cur.close()
        except Exception as e:
            self.connection.rollback()
            raise e

    def save(self, user):
            if user._id is None:
                self._add(user)
            else:
                self._update(user)

    def get_by_id(self, user_id):
            
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        if user is None:
            raise NotFoundException()
        cursor.close()
        return User(user[1], user[2], user[3], _id=user[0])


    def remove(self, _id):
        try:    
            cur = self.connection.cursor()
            cur.execute("DELETE FROM users WHERE id = ?", (_id, ))
            self.connection.commit()
            cur.close()
        except Exception as e:
            self.connection.rollback()
            raise e