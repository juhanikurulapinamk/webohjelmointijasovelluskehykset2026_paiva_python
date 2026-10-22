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

    @staticmethod
    # User.get_all()
    def get_all():
        
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            cur = con.cursor()
            cur.execute("SELECT first_name, last_name, username, id FROM users")
            users = cur.fetchall()
            cur.close()
            users_list = []
            
            for row in users:
                users_list.append(
                    User(row[0], row[1], row[2], _id=row[3])
                )
            return users_list

    def save(self):
        if self._id is None:
            self._add()
        else:
            self._update()

    

        

    def _add(self):
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO users(first_name, last_name, username) VALUES(?, ?, ?)",
                        (self.firstname, self.lastname, self.username))
            con.commit()
            self._id = cur.lastrowid
            cur.close()

    @staticmethod
    def get_by_id(user_id):
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user = cursor.fetchone()
            if user is None:
                raise NotFoundException()
            cursor.close()
            return User(user[1], user[2], user[3], _id=user[0])
    
    def _update(self):
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE users SET first_name = ?, last_name = ?, username = ?  WHERE id = ?",
                        (self.firstname, self.lastname, self.username, self._id))
            con.commit()
            cur.close()

    # tämä edellyttää käyttäjän hakemista tietokannasta ennen poistoa
    def remove(self):
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE id = ?", (self._id, ))
            con.commit()
            cur.close()

    @staticmethod
    def remove_by_id(_id):
        with sqlite3.connect("tuntiharjoitus1.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE id = ?", (_id, ))
            con.commit()
            rows_affected = cur.rowcount
            cur.close()
            return rows_affected
            
                
        