

from contextlib import closing
import sqlite3

from repositories.factories import create_users_repository


def get_users_repository(route_handler_func):
    def wrapper(*args, **kwargs):
        with closing(sqlite3.connect("tuntiharjoitus1.db")) as con:
            users_repository = create_users_repository(con)
            return route_handler_func(users_repository, *args, **kwargs)
    return wrapper